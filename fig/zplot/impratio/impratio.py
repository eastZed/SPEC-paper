import matplotlib.pyplot as plt
import ast
from collections import defaultdict

# 全局设置字体大小
plt.rcParams.update({
    'xtick.labelsize':65,  # 设置xticks字体大小
    'ytick.labelsize':65,  # 设置yticks字体大小
    'axes.labelsize':65,   # 设置xlabel和ylabel字体大小
    'font.family': 'Arial',
})

# 读取txt文件并解析成字典
with open('6.7b_sele_load_0.5_0_chunk_hit_rte.txt', 'r') as file:
    data = file.read()
    chunk_dict = ast.literal_eval(data)

# 第一幅图：chunkid vs 读了多少token
# 每个chunkid作为不同的key
token_counts = {}
for (prefixid, layerid, chunkid), (access_count, token_count) in chunk_dict.items():
    unique_chunkid = f"{prefixid}-{layerid}-{chunkid}"
    if token_count > 0:
        token_counts[unique_chunkid] = token_count / access_count / 64 * 100

# 按token_count降序排列
sorted_token_counts = dict(sorted(token_counts.items(), key=lambda item: item[1], reverse=True))

# 计算平均比例
impratios = list(sorted_token_counts.values())
sele_impratios = [v for v in impratios if v<100]
print(f'avg ratio of all non-zero chunk = {sum(impratios) / len(impratios)}')
print(f'avg ratio of all non-zero and not-100 chunk = {sum(sele_impratios) / len(sele_impratios)}')
print(f'len of sele_impratios = {len(sele_impratios)}, len of impratios = {len(impratios)} takes up {len(sele_impratios) / len(impratios)* 100}%')

# 绘制第一个图
# plt.figure(figsize=(10, 6))
# plt.bar(sorted_token_counts.keys(), sorted_token_counts.values(), color='skyblue')

# 绘制第一个图，减少横坐标的密集度
plt.figure(figsize=(15, 10))
plt.bar(range(len(sorted_token_counts)), sorted_token_counts.values(), color='#5B9BD5')

# 加粗图的四个边框
ax = plt.gca()  # 获取当前的Axes对象
for spine in ax.spines.values():
    spine.set_linewidth(7)  # 设置边框线宽，2可以调整为你想要的宽度
ax.tick_params(axis='x', pad=15)  # 调整x轴数字与坐标轴的距离，10可以调整为你想要的值
ax.tick_params(axis='y', pad=15)  # 调整y轴数字与坐标轴的距离

# 仅显示部分chunkid标签
step = max(1, len(sorted_token_counts) // 4)  # 每隔step个显示一个标签
plt.xticks(range(0, len(sorted_token_counts)+1, step), 
        #    list(sorted_token_counts.keys())[::step],
           range(0, len(sorted_token_counts)+1, step),
        #    rotation=45, 
        #    ha='right'
           )
plt.yticks([0, 25, 50, 75, 100], 
        #    list(sorted_token_counts.keys())[::step],
           [0, 25, 50, 75, 100],
        #    rotation=45, 
        #    ha='right'
           )

plt.xlabel('Chunk ID')
plt.ylabel('Ratio (%)')
# plt.title('Tokens Read per Chunk ID')
plt.xticks()
plt.tight_layout()
plt.savefig('impratio_per_chunk.pdf')
plt.close()

# 第二幅图：访问次数 vs 平均读了多少token
# 计算每个访问次数下的chunk的平均读了多少token
access_tokens = defaultdict(list)
for (prefixid, layerid, chunkid), (access_count, token_count) in chunk_dict.items():
    access_tokens[access_count].append(token_count/access_count / 64 * 100 if access_count>0 else 0)

# 计算平均值
avg_tokens_per_access = {access: sum(tokens)/len(tokens) for access, tokens in access_tokens.items()}

# 按访问次数升序排列
sorted_avg_tokens = dict(sorted(avg_tokens_per_access.items()))
print(f'sorted_avg_tokens = {sorted_avg_tokens}')

# 绘制第二个图
plt.figure(figsize=(15, 10))
plt.bar(sorted_avg_tokens.keys(), sorted_avg_tokens.values(), color='#FF2400')
# 加粗图的四个边框
ax = plt.gca()  # 获取当前的Axes对象
for spine in ax.spines.values():
    spine.set_linewidth(7)  # 设置边框线宽，2可以调整为你想要的宽度
ax.tick_params(axis='x', pad=15)  # 调整x轴数字与坐标轴的距离，10可以调整为你想要的值
ax.tick_params(axis='y', pad=15)  # 调整y轴数字与坐标轴的距离

plt.xlabel('Chunk access count')
plt.ylabel('Ratio (%)')
step = max(1, len(sorted_avg_tokens) // 5)
plt.xticks(list(sorted_avg_tokens.keys())[::step], 
           list(sorted_avg_tokens.keys())[::step],
            #  range(0, len(sorted_avg_tokens)+1, step),
        #    rotation=45, 
        #    ha='right'
           )
plt.yticks([0, 25, 50], 
        #    list(sorted_token_counts.keys())[::step],
           [0, 25, 50],
        #    rotation=45, 
        #    ha='right'
           )
# plt.title('Average Tokens Read per Access Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('impratio_accesscount.pdf')
plt.close()
