# Segmentation-and-counting-of-teeths-using-panoramic-dental-X-rays
This repo provides advanced teeth segmentation in dental X-rays using image processing &amp; ML. Designed for dentists and researchers, it automates teeth detection, simplifying diagnoses and aiding in-depth dental assessments.

This repository contains Google Colab notebooks for teeth segmentation in dental X-rays using different resolutions and architectures.

## Notebooks:

1. **256x256 Project Implementation.ipynb**: Segmentation using a 256x256 resolution.
2. **512x512 Project Implementation.ipynb**: Segmentation using a 512x512 resolution.
3. **256x256 Transformer Project Implementation.ipynb**: Segmentation using a 256x256 resolution with a Transformer-based architecture.

## Prerequisites:

- Google Colab account (Free tier should be sufficient for most tasks)
- Google Drive account to access data

## Instructions:

### 1. Setting up the Environment:
   - Clone this repository to your local machine or directly to Google Drive.
   - Open the desired notebook in Google Colab.

### 2. Data Loading:
   - Place your dental X-ray images in a folder on Google Drive.
   - Update the data path in the respective Colab notebook to point to your folder.

### 3. Running the Notebook:
   - Execute the cells in sequence. Make sure to authorize Google Colab to access your Google Drive when prompted.

### 4. Monitoring Training and Results:
   - The notebooks provide visual feedback and metrics as the models train.
   - After training, you can observe segmentation results on test data within the notebook and also see the watershed results.

## Contributing:

We appreciate contributions! If you have improvements or suggestions, please open an issue or submit a pull request.

