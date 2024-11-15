<!-- This file is a placeholder for customizing description of your plugin
on the napari hub if you wish. The readme file will be used by default if
you wish not to do any customization for the napari hub listing.

If you need some help writing a good description, check out our
[guide](https://github.com/chanzuckerberg/napari-hub/wiki/Writing-the-Perfect-Description-for-your-Plugin)
-->

## Description

This plugin provides a reader for swc files. It can load swc files to napari viewer as points layers and lines layers. The size of points and lines are using the radius of the swc file. You can load an example swc from https://neuromorpho.org/dableFiles/jacobs/CNG%20version/204-2-6nj.CNG.swc

![image](https://github.com/user-attachments/assets/1c9e5788-0e74-48ab-be0b-0fb74b35192c)

## Features

- Load swc file(s) to napari viewer
- Display swc file(s) in napari viewer as points layers and lines layers
- Size of points and lines are using the radius of the swc file
- You can load an example swc from https://neuromorpho.org/dableFiles/jacobs/CNG%20version/204-2-6nj.CNG.swc or load it under `File` -> `Open Sample` -> `napari-swc-reader`

**Limitations:**
- Only support swc file(s) following specs http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html 7 columns
- Cannot write swc file(s) to disk but you can access the raw swc data from the napari layers from `metadata` attribute with key `raw_swc`

## Getting Help

If you have any questions about the plugin, please [open an issue](https://github.com/LaboratoryOpticsBiosciences/napari-swc-reader/issues).

## Other Resources

Checkout this cool other ressources working with swc files and napari:
- https://skeleton-analysis.org/stable/index.html
