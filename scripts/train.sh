
"""
python -u smes_ppo/train.py \
    --dataset_name trl-internal-testing/descriptiveness-sentiment-trl-style \
    --dataset_train_split descriptiveness \
    --learning_rate 3e-6 \
    --output_dir smes_ppo_logs \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --total_episodes 10000 \
    --model_name_or_path Qwen/Qwen2-0.5B-Instruct \
    --reward_model_path Qwen2-0.5B-Reward \
    --sft_model_path Qwen/Qwen2-0.5B-Instruct \
    --missing_eos_penalty 1.0 \
    --use_peft \
    --load_in_4bit=True

accelerate launch --config_file scripts/ds_config.json \
    examples/scripts/ppo/ppo.py \
    --dataset_name trl-internal-testing/descriptiveness-sentiment-trl-style \
    --dataset_train_split descriptiveness \
    --output_dir models/minimal/ppo \
    --num_ppo_epochs 1 \
    --num_mini_batches 1 \
    --learning_rate 3e-6 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --total_episodes 10000 \
    --model_name_or_path EleutherAI/pythia-1b-deduped \
    --sft_model_path EleutherAI/pythia-1b-deduped \
    --reward_model_path EleutherAI/pythia-1b-deduped \
    --local_rollout_forward_batch_size 1 \
    --missing_eos_penalty 1.0
"""
