# Dockerfile for Binder (mybinder.org) inspired by https://git.io/v1InG
FROM andrewosh/binder-base

MAINTAINER Daniel Himmelstein <daniel.himmelstein@gmail.com>

USER main

# Install requirements for Python 2
COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt

# Install requirements for Python 3
RUN /home/main/anaconda/envs/python3/bin/pip install --requirement requirements.txt

# Install vega nbextension for Jupyter
RUN jupyter nbextension install --sys-prefix --py vega
