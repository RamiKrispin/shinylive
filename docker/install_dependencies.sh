#!/bin/bash

#Environment variables
QUARTO_VERSION=$1 
CONDA_ENV=$2 
PYTHON_VER=$3

# Install dependencies
apt-get update && apt-get install -y --no-install-recommends \
    jq \
    libxml2-dev \
    zlib1g \
    g++-11 \
    libz-dev \
    freetype2-demos \
    libpng-dev \
    libtiff-dev \
    libjpeg-dev \
    make \
    fontconfig \
    libfribidi-dev \
    libharfbuzz-dev \
    libfontconfig1-dev \
    git \
    vim \
    curl \
    sudo \
    wget \
    && rm -rf /var/lib/apt/lists/*

#Italling Quarto
QUARTO_VERSION=$1
TEMP_QUARTO="$(mktemp)" &&
wget --no-check-certificate -O "$TEMP_QUARTO" https://github.com/quarto-dev/quarto-cli/releases/download/v$QUARTO_VERSION/quarto-${QUARTO_VERSION}-linux-amd64.deb &&
sudo dpkg -i "$TEMP_QUARTO"
rm -f "$TEMP_QUARTO"

# Install miniconda
sudo apt update && apt-get install -y --no-install-recommends \
    software-properties-common \
    && sudo add-apt-repository -y ppa:deadsnakes/ppa \
    && sudo apt update 

wget --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && export PATH=/opt/conda/bin:$PATH \
    && conda init bash \
    && conda install conda-build

. /root/.bashrc \
    && conda create -y --name $CONDA_ENV python=$PYTHON_VER 

echo "conda activate $CONDA_ENV" >> ~/.bashrc

# Installing Python libraries
. /root/.bashrc conda activate $CONDA_ENV \
&& conda info --envs \
&& pip install shiny \
&& pip install pandas \
&& pip install numpy \
&& pip install matplotlib \
&& pip install plotly \
pip install statsmodels
