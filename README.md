# CZ Hub Take Home Test
### Author: Bo-Yen Chang

## Overview
This repository contains the solutions for the CZ Hub Associated R&D Engineer position take-home test. Each directory within this repository corresponds to an exercise that tackles different aspects of image acquisition, real-time data processing, and image analysis using Python and various scientific libraries.

The exercises are designed to simulate the types of challenges encountered in lab automation and data analysis. They include image acquisition from a simulated microscope, real-time image processing, and quantitative analysis of cell images.

## Contents
- `Exercise1/`: Python script and multi-dimensional .tif dataset for automated image acquisition.
- `Exercise2/`: Python script for real-time image analysis and modified .tif dataset reflecting specified pixel modifications.
- `Exercise3/`: Python script for segmenting cell nuclei from images, measuring their eccentricity, and an eccentricity histogram in .png format.

## Exercise 1: Automated Image Acquisition
- **Objective**: Acquire a multi-dimensional .tif dataset with predefined z-slices and channels, representing a typical automated microscopy session.
- **Implementation**: Utilized `pycromanager` for control of the acquisition process. The script handles z-stacks, multi-channel acquisition, and grid positioning.
- **Output**: A multi-dimensional .tif dataset with the correct dimensions and metadata.

## Exercise 2: Real-time Image Processing
- **Objective**: Perform a timelapse acquisition and process images in real-time to identify and modify pixels with specific characteristics.
- **Implementation**: Extended the acquisition pipeline to inspect and modify each image based on pixel value conditions using `scikit-image`.
- **Output**: A modified .tif dataset where each image has been processed to set neighboring pixels within a radius of 15 pixels to zero if a pixel value of exactly 700 counts is detected.

## Exercise 3: Image Analysis and Eccentricity Measurement
- **Objective**: Segment cell nuclei from a series of images and plot their eccentricity as a metric of cell health.
- **Implementation**: Used the `cellpose` segmentation model to segment nuclei and `scikit-image` to measure their eccentricity. Plotted the results using `matplotlib`.
- **Output**: A histogram representing the eccentricity of cell nuclei, saved as a .png file.

## Installation
To run the scripts in this repository, ensure that you have Python installed along with the following packages: `pycromanager`, `scikit-image`, `cellpose`, `opencv-python-headless`, and `matplotlib`. They can be installed via pip:

```bash
pip install pycromanager scikit-image cellpose opencv-python-headless matplotlib
```

## Usage
Navigate to each exercise directory and run the corresponding script using Python. For implementation, please refer to the jupyter notebooks in each directory 

## Acknowledgments
- Exercise 1 was inspired by examples from the [Pycro-Manager acquisitions tutorial](https://micro-manager.org/apidoc/mmcorej/latest/mmcorej/CMMCore.html).
- Real-time image processing techniques in Exercise 2 were conceptualized with the assistance of [ChatGPT](https://chat.openai.com/).
- Cell segmentation in Exercise 3 was facilitated by the [Cellpose model](https://github.com/MouseLand/cellpose), and image processing was conducted using [scikit-image](https://scikit-image.org/docs/stable/api/skimage.io.html).

## Author
Bo-Yen Chang

Email: changboyen@berkeley.edu

---

Please feel free to reach out if you have any questions or need further clarification on the exercises and their implementations. 

