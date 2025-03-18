# import matplotlib.pyplot as plt
# import pandas as pd
# import json
# import os

# class MetricsPlotter:
#     def __init__(self, run_id):
#         self.run_id = run_id
#         self.log_file = os.path.join('flowertune_llm', 'logs', f'{run_id}.json')
#         self.plot_dir = os.path.join('flowertune_llm', 'results_plot')
        
#     def load_metrics(self):
#         """로그 파일에서 메트릭 데이터 로드"""
#         metrics_list = []
#         with open(self.log_file, 'r') as f:
#             for line in f:
#                 if 'metrics' in line:
#                     try:
#                         metrics = json.loads(line.split('INFO')[1].strip())
#                         metrics_list.append(metrics)
#                     except:
#                         continue
#         return pd.DataFrame(metrics_list)
    
#     def plot_metrics(self):
#         """메트릭 그래프 생성"""
#         df = self.load_metrics()
        
#         plt.figure(figsize=(15, 10))
        
#         # 손실 그래프
#         plt.subplot(2, 1, 1)
#         plt.plot(df['round'], df['loss'], marker='o')
#         plt.title('Training Loss')
#         plt.xlabel('Round')
#         plt.ylabel('Loss')
        
#         # 학습률 그래프
#         plt.subplot(2, 1, 2)
#         plt.plot(df['round'], df['learning_rate'], marker='o', color='orange')
#         plt.title('Learning Rate')
#         plt.xlabel('Round')
#         plt.ylabel('Learning Rate')
        
#         plt.tight_layout()
        
#         # 그래프 저장
#         plot_path = os.path.join(self.plot_dir, f'{self.run_id}_metrics.png')
#         plt.savefig(plot_path)
#         plt.close()
