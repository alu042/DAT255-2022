# DeepFruit: an example of a DAT255 mini-project

This is a simple example of a _DAT255 mini-project_. It is meant to indicate the expectations for the content and the presentation for the other students in the class. 

> Remember that a DAT255 mini-project are small. It should be doable to do the project and create a presentation of the work within 4-6 hours. 

> At the stage of the course when this mini-project example was used, we've only completed the first course module / week of the course. We will therefore not use techniques covered by later modules of the course to construct our fruit classifier. 

---

Here are the details about the DeepFruit mini-project (copied from the mini-project catalog):

**Title/Topic:** DeepFruit: The fruit classifier

**Goals:** (i) Train a computer vision model to classify pictures of fruits. (ii) Make a web-application where users can upload new pictures of fruits to get them classified. 

**Data set:** The Fruits-360 data set available at https://github.com/Horea94/Fruit-Images-Dataset and https://www.kaggle.com/moltean/fruits. 

**Methods:** After watching Lesson 1 of the fastai course, the project seems to be doable using the fastai vision module. The web application can for example be constructed using a Jupyter Notebook and Voilá, and be deployed via Binder, as demonstrated in the course.


## Project structure

```bash
├── LICENSE
├── README.md          <- The top-level README file
├── data               <- Data used in the project
│
├── models             <- Trained and serialized models
│
├── nbs                <- Jupyter notebooks. 
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
└── environment.yml    <- The requirements file for reproducing the 
                          Python environment
``` 


## Jupyter Notebooks

The project consists of four notebooks

| Notebook    |      1-Click Notebook      |
|:----------|------|
|  [1.0-asl-collect_and_explore_data.ipynb](https://nbviewer.org/github/) | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/)|
|  [2.0-asl-fruit_classifier.ipynb](https://nbviewer.org/github/) | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/)|
|  [3.1-asl-fruit_classifer_app_v1.ipynb](https://nbviewer.org/github/) | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/)|
|  [3.2-asl-fruit_classifer_app_v2.ipynb](https://nbviewer.org/github/) | [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/)|





## Installation instructions
To run the notebooks on your own computer, create a new conda environment using the [environment.yml](../environment.yml) file in this repository. I.e., write
```bash
conda update env
```
inside a folder containing `environment.yml`. You can then create a Jupyter Kernel for the environment by writing
```bash
conda activate dat255-fruit
python -m ipykernel install --user --name dat255-fruit --display-name "DAT255-fruit"
conda deactivate
```
then launch Jupyter or JupyterLab via `jupyter notebook` or `jupyter lab`.



## Video walk-through

_TBA_