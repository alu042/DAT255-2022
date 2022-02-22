# The building blocks of neural networks

A quick introduction to the building blocks of neural networks, and the construction and training of neural networks in PyTorch.

## Structure

```bash
├── LICENSE
├── README.md               <- The top-level README file
├── data                    <- Data used in the project
├── nbs                     <- Jupyter notebooks. 
├── environment-gpu.yml     <- The requirements file for reproducing the Python environment, GPU version
└── environment-cpu.yml     <- The requirements file for reproducing the Python environment, CPU version
``` 

## Run in Google Colab

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alu042/DAT255-2022/)


## Run locally

Install the necessary libraries:

If you have a PyTorch compatible GPU, then install 

```bash
conda env update -f environment-gpu.yml
```

If you want to use a CPU:

```bash
conda env update -f environment-cpu.yml
```


Install a Jupyter kernel:
```bash
conda activate pytorch
python -m ipykernel install --user --name pytorch --display-name "PyTorch"
conda deactivate
``` 

Finally, launch Jupyter Notebook or Jupyter Lab.
