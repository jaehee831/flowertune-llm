# import logging
# import json
# import os
# from datetime import datetime

# class MetricsLogger:
#     def __init__(self, run_id, config):
#         self.run_id = run_id
#         self.log_file = os.path.join('flowertune_llm', 'logs', f'{run_id}.json')
        
#         # 설정 정보 저장
#         self.save_config(config)
        
#         # 로거 설정
#         logging.basicConfig(
#             filename=self.log_file,
#             level=logging.INFO,
#             format='%(asctime)s %(message)s'
#         )
#         self.logger = logging.getLogger(__name__)
    
#     def save_config(self, config):
#         """설정 정보를 로그 파일에 저장"""
#         with open(self.log_file, 'w') as f:
#             json.dump({
#                 'config': config,
#                 'timestamp': datetime.now().isoformat(),
#                 'metrics': []
#             }, f, indent=2)
    
#     def log_metrics(self, metrics):
#         """메트릭을 로그 파일에 추가"""
#         self.logger.info(json.dumps(metrics))
