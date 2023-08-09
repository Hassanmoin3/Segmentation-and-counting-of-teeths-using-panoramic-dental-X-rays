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

## Dataset:

Due to size limit issues, the dataset used for this project cannot be uploaded directly to GitHub. Instead, you can access the dataset from [Tufts University's Dental Dataset](http://tdd.ece.tufts.edu/). Follow the steps below:

1. Visit [this link](http://tdd.ece.tufts.edu/) and fill out the form to gain access to the dataset.
2. After downloading the dataset, you will encounter four folders: "Expert", "Radiographs", "Segmentation", "Student".
3. For this project, we will only be utilizing the images from `/Radiograph/Images1` and the masks from `Segmentation/Orig_Masks`. Please ignore the rest of the folders.
4. Place the images and the masks into a folder named `Data` in the cloned repository.
5. Adjust the paths in the provided scripts according to where you've placed your data.

## Contributing:

We appreciate contributions! If you have improvements or suggestions, please open an issue or submit a pull request.
