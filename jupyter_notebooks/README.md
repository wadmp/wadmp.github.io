## Introduction
[Project Jupyter](https://jupyter.org/) provides an ecosystem of tools for interactive programming in your web browser.

We use Jupyter "notebooks" to improve the WebAccess/DMP documentation.

> You do not need to be a programmer to use Jupyter notebooks!

Benefits of using a Jupyter notebook:
* Use hosted Jupyter servers (like [Binder](https://mybinder.org/), [Colab](https://colab.research.google.com/notebooks/intro.ipynb), etc.) to avoid having to install anything locally;
* Combine documentation and code, and optionally example output;
* Rapid prototyping of scripts or apps to consume the public WA/DMP APIs;
* Leverage lots of Python or Javascript GUI libraries, including interactive widgets.

## Viewing Notebooks

GitHub renders Jupyter Notebooks (.ipynb files) automatically.

You can also view notebooks in [nbviewer](https://nbviewer.jupyter.org/)

## Running Locally
Install Jupyter Notebook and/or JupyterLab following the instructions [here](https://jupyter.org/install.html).

### Interactive widgets
Some notebooks use interactive [widgets](https://jupyter.org/widgets) for more powerful data visualisation.

If you are running in Jupyter Notebook (>= version 5.3) you don't need to change any code.

If you are running in Jupyter Lab, you will also need to install the JupyterLab *extensions* which are required by the notebook.

For example, the [geolocate](https://github.com/wadmp/wadmp.github.io/blob/master/jupyter_notebooks/geolocate.ipynb) notebook uses [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/index.html), which requires 2 extensions:
* @jupyter-widgets/jupyterlab-manager
* jupyter-leaflet

You can do this in several ways:
1. Using the "Extension Manager" feature in the Jupyter Lab user interface;
2. In a terminal, run `jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet`;
3. Run the shell command in the Notebook itself, using the `!` syntax: `!jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet`.

> Note that in order to use JupyterLab extensions, you need to have Node.js and npm installed.

## Running on Binder
You can run all of these notebooks on [Binder](https://mybinder.org/):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/wadmp/wadmp.github.io/master?filepath=jupyter_notebooks)

> Note that Binder builds are persisted automatically.
> i.e. If the GitHub repository is changed, the first build on Binder may take some time (you can watch the Build Log).
> But subsequent launches on Binder will automatically use the existing build.

### Interactive widgets
All scripts should work on Binder.

In the top level GitHub directory, we provide a `postBuild` file and an `environment.yml` file. These are used by Binder to build the environment.

## Running on Colab
You can run some of these notebooks on Google [Colab](https://colab.research.google.com/notebooks/intro.ipynb) (aka Colaboratory).

### Interactive widgets
At the moment, interactive widgets *are not supported* on Colab:
* https://github.com/googlecolab/colabtools/issues/60
* https://github.com/jupyter-widgets/ipyleaflet/issues/195

## Developing new notebooks
We encourage all WA/DMP users to develop their own notebooks. Please submit a Pull Request using the GitHub repo.

### Recommendations:
1. For Python libraries, use `!pip install ...` in the notebok itself, rather than using a separate requirements.txt file.
2. For any interactive widgets, please list what JupyterLab extensions are required in a note at the top of the script.
3. If you do not want to include the output of your cells, particularly if it contains sensitive information like user credentials, remember to clear all output before saving the notebook and commiting to GitHub.

## Other References:
* https://www.nature.com/articles/d41586-018-07196-1
* https://www.dataschool.io/cloud-services-for-jupyter-notebook
