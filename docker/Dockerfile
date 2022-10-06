FROM ubuntu:22.10

# Setting environment variables
ARG CONDA_ENV=atsaf
ENV CONDA_ENV=$CONDA_ENV

ARG PYTHON_VER=3.10
ENV PYTHON_VER=$PYTHON_VER

ARG QUARTO_VERSION=1.1.149
ENV QUARTO_VERSION=$QUARTO_VERSION

# Copy files
RUN mkdir packages
COPY install_dependencies.sh packages/
RUN bash packages/install_dependencies.sh $QUARTO_VERSION $CONDA_ENV $PYTHON_VER

