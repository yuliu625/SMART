# to project path
cd /home/liuyu/workspace/code/smart

# data processing
conda activate pdf_env
nohup python make_pymupdf_dir.py >./pymupdf.log 2>&1 &
nohup python make_docling_dir.py >./docling.log 2>&1 &
nohup python make_vlm_dir.py >./vlm.log 2>&1 &

# vector store
conda activate smart_env
nohup python make_vector_store_dir.py >./vector_store.log 2>&1 &


# experiments
conda activate smart_env
nohup python run_single_agent_experiments.py >./single_agent.log 2>&1 &
nohup python run_sequential_workflow_experiments.py >./sequential_workflow.log 2>&1 &
nohup python run_final_mas_experiments.py >./final_mas.log 2>&1 &

# new experiments
conda activate smart_env
cd /home/liuyu/workspace/code/smart_
python run_cached_sequential_workflow_experiments.py
python run_cached_final_mas_experiments.py

