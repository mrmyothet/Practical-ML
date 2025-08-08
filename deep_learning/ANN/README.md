# Artifical Neural Network (ANN)

Please see this for Slides

- https://github.com/tharhtetsan/zero_2_hero_ml/tree/main/7_Deep_Learning/ANN

## Create anaconda for python

```bash
# create conda environment
conda create --name <environment_name> python=3.11.13

# remove
conda remove -n ENV_NAME --all

where python


```

## Create pipenv

```bash
pipenv install --python <your-python-path or version>

# remove pipenv
pipenv --rm

# check python version
pipenv run python --version

# check pipenv location
pipenv --py

# sync pipenv with conda
pipenv sync

pipenv install opencv-python
pipenv install python-dotenv
pipenv install tensorflow==2.17.0


# dev only for mac os
pipenv install --dev tensorflow-macos tensorflow-metal
pipenv install --dev ipython

# for tessting
pipenv install --dev matplotlib


# for Production run
# Installs only what’s in Pipfile.lock, ignoring dev packages
pipenv --rm # to test remove first
pipenv install --deploy --ignore-pipfile

# for dev
# Everything in Pipfile.lock
# Including [dev-packages]
pipenv install


# test code
pipenv run python
import matplotlib.pyplot as plt


```

### CUDA Toolkit 12.2 Update 2 Downloads

- Operating System - Linux
- Architecture - x86_64
- Distribution - WSL Ubuntu
- Version - 2.0
- Installer Type - deb (local)

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda-repo-wsl-ubuntu-12-2-local_12.2.2-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-12-2-local_12.2.2-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

- Your GPU (NVIDIA Quadro K2000) has CUDA compute capability 3.0.
- TensorFlow dropped support for GPUs with compute capability <3.5 starting from TensorFlow 2.1.
