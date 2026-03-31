#######################
# csv_generator
# Used to generate csv files for testing
#######################
from pathlib import Path
import csv
import random

header = ['id', 'feat_1', 'feat_2', 'feat_3', 'feat_4', 'feat_5', 
          'feat_6', 'feat_7', 'feat_8', 'feat_9', 'feat_10']
current_dir = str(Path(__file__).resolve().parent)
with open((current_dir + '/test_data_large.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    for i in range(1, 101):
        row = [
            i,                                     # ID
            round(random.uniform(0, 100), 2),      # feat_1: 浮点数 (0-100)
            random.randint(1000, 9999),            # feat_2: 4位整数
            random.choice(['A', 'B', 'C', 'D']),   # feat_3: 分类标签
            round(random.random(), 4),             # feat_4: 归一化概率 (0-1)
            random.randint(0, 1),                  # feat_5: 二值特征 (0/1)
            round(random.gauss(50, 10), 2),        # feat_6: 正态分布
            random.randint(18, 65),                # feat_7: 模拟年龄
            random.choice(['High', 'Med', 'Low']), # feat_8: 等级
            round(random.uniform(-1, 1), 3),       # feat_9: 负值到正值
            random.randint(100, 200)               # feat_10: 计数
        ]
        writer.writerow(row)

print("Generating Successful!")

###############################################