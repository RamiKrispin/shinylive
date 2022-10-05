#!/bin/bash
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

wget --no-check-certificate --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && export PATH=/opt/conda/bin:$PATH \
    && conda init bash \
    && conda install conda-build



#. /root/.bashrc && conda activate $CONDA_ENV && conda info --envs && pip install package_name == package_version