# to project path
cd /home/liuyu/workspace/code/smart_

# gateway
## new task
tmux new -s litellm_proxy
## attach
tmux a -t litellm_proxy
conda activate smart_env
export DASHSCOPE_API_KEY=
litellm --config "/home/liuyu/workspace/code/smart_/configs/litellm/normal_configs.yaml"


# experiments
## sequential workflow
#tmux new -s sw
tmux a -t sw
conda activate smart_env
cd /home/liuyu/workspace/code/smart_
python run_cached_sequential_workflow_experiments.py

## mas
#tmux new -s mas
tmux a -t mas
conda activate smart_env
cd /home/liuyu/workspace/code/smart_
python run_cached_final_mas_experiments.py

