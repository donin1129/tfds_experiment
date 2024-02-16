# Custom tfds Experiment

## Overview

After searching online, it seems there is a lack of supporting material to show how to build a custom tfds. 

This project presents an experimental set up for building a custom dataset using the TensorFlow Datasets (tfds) library. 

The goal is to showcase a way of building custom datasets using tfds locally or by downloading the tar.gz file.

## Table of Contents

- [Installation](#installation)
- [Explanation](#explanation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [License](#license)

## Installation

To get started, you'll need to install the required dependencies. It is recommended to create a virtual environment first.

```bash
virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Explanation

In this project, there are two folders. One is `oxford_iiit_pet_dataset` and the other is `dataset_experiment`. 

The `oxford_iiit_pet_dataset` folder is a direct copy from [tensorflow_datasets oxford_iiit_pet repository](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/datasets/oxford_iiit_pet). It serves as an example of reference how to start manipulating your own dataset. 

The `dataset_experiment` folder is an example of my manipulation to provide a custom tfds dataset. Mindful that it might not be of the best practice. 

## Usage
To make a downloadable dataset
1. Go to `./dummy_data` and create two `tar.gz` files, one named `images.tar.gz` by zipping the `./dummy_data/images` directory and the one named `annotations.tar.gz` by zipping the `./dummy_data/annotations` directory. 
   - On Windows, you can use 7zip, by using `tar` as `Archive format` and then use 7zip again by using `gzip` as `Archive format` on the artifact created from the earlier step. 
2. Take the two artifact `images.tar.gz` and `annotations.tar.gz` and use any file server of your choice to serve them. 
3. Go to `./dataset_experiment/experimental_dataset_builder.py` and set `_BASE_URL`. Be mindful that `images.tar.gz` must be downloadable from `_BASE_URL/images.tar.gz` and `annotations.tar.gz` must be downloadable from `_BASE_URL/annotations.tar.gz`

To make a local generated dataset
1. Go to `./dataset_experiment/main.py` and it provides an example of how to build dataset from local path. 
2. Put in the directory path for to replace `"./dummy_data"` in line `builder.set_local_path("./dummy_data")`. Be mindful about the directory structure, but you can also design your own structure by revising the code in `dataset_builder.py`.

You should be able to run the `./dataset_experiment/main.py` for the methods you are looking for and the built dataset can be found wherever you configure tfds default directory location. By default, it should be at `{User}/experimental`, where `{User}` is the generic user folder on your os. 

The dataset is named `experimental` because the dataset_builder.py file is named `experimental_dataset_builder.py`. If you want change the name of your dataset, then refactor the file name to `{NAME_OF_YOUR_DATASET}_dataset_builder.py`. 

## Disclaimer
I might make mistakes. Not follow best practices. I am not responsible for what you do with this repository. Please use with your own critical judgement. If you want to make a comment on how to follow the better practice, I would love to learn more. Please feel free to open a ticket :D

## License
This project is licensed under the MIT License.