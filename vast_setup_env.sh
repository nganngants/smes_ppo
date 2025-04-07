#!/bin/bash

conda env create -f environment.yml

conda init

echo "conda activate smes_multimodal" >> ~/.bashrc
source ~/.bashrc

apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
