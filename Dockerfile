# Dockerfile for Binder (mybinder.org) inspired by https://git.io/v1InG
FROM andrewosh/binder-base

MAINTAINER Daniel Himmelstein <daniel.himmelstein@gmail.com>

USER main

# Python 2 notebook updates and altair installation
RUN /home/main/anaconda2/bin/conda update --yes --quiet notebook
RUN /home/main/anaconda2/bin/conda install --yes --quiet --channel conda-forge altair
RUN /home/main/anaconda2/bin/pip install nameparser==0.5.1

# Python 3 notebook updates and altair installation
RUN /home/main/anaconda/bin/conda install --name python3 --yes --quiet --channel conda-forge altair
RUN /home/main/anaconda/envs/python3/bin/pip install nameparser==0.5.1
