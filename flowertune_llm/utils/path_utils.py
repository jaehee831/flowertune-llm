# import os
# from datetime import datetime

# def create_directories():
#     """필요한 디렉토리들을 생성합니다."""
#     dirs = [
#         'logs',
#         'results_plot'
#     ]
#     for dir_name in dirs:
#         os.makedirs(os.path.join('flowertune_llm', dir_name), exist_ok=True)

# def get_run_id(config):
#     """실행 ID를 생성합니다."""
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     model_name = config.model.name
#     return f"{model_name}_{timestamp}"
