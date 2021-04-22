# Github automation

In this repository I'm using python to automate the github actions.
>I automate those task because some are not user friendly and repetitive.

# Start data science projects with a template

For this template, we'll use cookiecutter.
According to the contributors, it's _a logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [The project homepage](http://drivendata.github.io/cookiecutter-data-science/)


### Requirements to use this template:
-----------
 - Git
 - A folder dedicated to all your data science projects including python, scala, notebooks files, etc...
 - Python 3
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip depending on how you manage your Python packages:

**Step 1** - Install Git if it's not already done <br>
Follow this link [Git Downloads](https://git-scm.com/downloads)

**Step 2** - Create the data science folder 
``` bash
$ mkdir my-data-science-projects
```

**Step 3** - Install python if it's not already done<br>
Follow this link [Python Downloads](https://www.python.org/downloads/)

**Step 4** - Install cookiecutter
``` bash
$ pip install cookiecutter
```
Once you've download cookiecutter, you're ready to start.

# Starting a new project 

Every time you'll start a new project, follow those steps:

Navigate first to your **data science projects** folder.
``` bash
$ cd my-data-science-projects
```
Clone this repository and set the environment
``` bash
$ git clone https://github.com/BriceFotzo/github_automation
```
Navigate to the repository and create a .env file to set environment variables
``` bash
$ cd github_automation
$ touch .env
```
In the .env file, set those variables:
>GITHUB_USER = '{username}'
>GITHUB_API = "https://api.github.com"
>GITHUB_TOKEN='ghp_XXXXXXXXXXXXXXXXXXXXXXX'
>GITHUB_URL='https://github.com/{username}'

Then run the following command to setup a new project with (project name, project repository name, your name, a license and a python version)
``` bash
$ py main.py
```
Once you're first repository is pushed, you can start developping.
Don't forget to add, commit and push changes every day or every important change (mainly when your code works!)

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```



