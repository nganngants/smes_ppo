##### Run this after activate the environment #####
pip uninstall bitsandbytes -y
pip install bitsandbytes==0.43.1
pip install h5py rouge_score
pip install flash-attn --no-build-isolation
pip install --upgrade transformers
pip uninstall deepspeed -y
pip install deepspeed==0.15.4
pip install gdown
pip install git+https://github.com/huggingface/trl.git
git config --global user.email "nganngants@gmail.com"
git config --global user.name "nganngants"

gdown --folder https://drive.google.com/drive/folders/1-CDVZQ-Q0URzvs7VvuzDoAww2XO6OTwm?usp=drive_link