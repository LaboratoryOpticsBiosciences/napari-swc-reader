"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the Reader specification, but your plugin may choose to
implement multiple readers or even other plugin contributions. see:
https://napari.org/stable/plugins/guides.html?#readers
"""

import io

import numpy as np
import pandas as pd


def napari_get_reader(path):
    """A basic implementation of a Reader contribution.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]

    # if we know we cannot read the file, we immediately return None.
    if not path.endswith(".swc"):
        return None

    # otherwise we return the *function* that can read ``path``.
    return reader_function


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.
    The first layer will be a points layer, the second layer will be a shapes layer.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples. Each path will return two tuples, one for points and one for shapes.
    """
    # handle both a string and a list of strings
    paths = [path] if isinstance(path, str) else path

    result = []
    for _path in paths:
        with open(_path) as f:
            file_content = f.read()

        df = pd.read_csv(
            io.StringIO(file_content),
            sep=r"\s+",  # separator is any whitespace
            comment="#",
            # set columns names according to SWC format
            # http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html
            names=[
                "treenode_id",
                "structure_id",
                "x",
                "y",
                "z",
                "r",
                "parent_treenode_id",
            ],
            index_col=0,
        )

        radius = df["r"].values

        # for each node create a point
        nodes = df[["x", "y", "z"]].values

        add_kwargs_points = {
            "n_dimensional": True,
            "size": radius,
            "metadata": {"raw_swc": file_content},
        }
        result.append((nodes, add_kwargs_points, "points"))  # points layer

        # for each edge create a line
        edges = df["parent_treenode_id"].values

        # remove all soma nodes
        nodes = nodes[edges != -1]
        edges = edges[edges != -1]

        # for each id in edges, get the corresponding node according to its index
        prev_node = df.loc[edges][["x", "y", "z"]].values

        lines = np.array([nodes, prev_node])
        lines = np.moveaxis(lines, 0, 1)

        add_kwargs_shapes = {
            "shape_type": "line",
            "edge_width": radius,
            "metadata": {"raw_swc": file_content},
        }
        result.append((lines, add_kwargs_shapes, "shapes"))  # lines layer

    return result
