import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import os

# 全局设置字体为 Arial，字体大小为 14（可以根据需要调整）
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 20



# 数据定义
# OPT-6.7b
# recomp
x11 = [60, 50, 25, 10, 5, 0]
y11 = [76.9, 76.9, 76.9, 76.9, 76.9, 76.9]
# as+h2o
x12 = [50, 25, 10, 5]
y12 = [76.9, 76.4, 75.5, 74]
# ours
x13 = [50, 25, 10, 5]
y13 = [77, 76.2, 76.9, 76.1]

# OPT-13b
# recomp
x21 = [60, 50, 25, 10, 5, 0]
y21 = [77, 77, 77, 77, 77, 77]
# as+h2o
x22 = [50, 25, 10, 5]
y22 = [76.8, 77, 76.3, 75.5]
# ours
x23 = [50, 25, 10, 5]
y23 = [77.2, 76.9, 76.4, 75.3]

# OPT-30b
# recomp
x31 = [60, 50, 25, 10, 5, 0]
y31 = [79.1, 79.1, 79.1, 79.1, 79.1, 79.1]
# as+h2o
x32 = [50, 25, 10, 5]
y32 = [78, 77, 76, 76]
# ours
x33 = [50, 25, 10, 5]
y33 = [78.1, 78.3, 77.5, 76.3]


# 开始绘图
# fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
fig, axes = plt.subplots(1, 3, figsize=(12 * 3.3 / 4, 3.2), sharey=False)

# 让 x 轴从大到小排列
for ax in axes:
    ax.invert_xaxis()


markersize = 12
linewidth = 3
fontsize = 20

# 第一个子图
axes[0].plot(x11, y11, 'k-', label='ReComp', linewidth=linewidth)  # 黑色线，不加点
axes[0].plot(x12, y12, 'o-', label='AS', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='dodgerblue')  # 蓝色线，带黑色边框的点
axes[0].plot(x13, y13, '^-', label='AS+H2O', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='lightsalmon')  # 红色线，带黑色边框的点
axes[0].set_title('OPT-6.7B', fontsize=fontsize)
axes[0].set_xlabel('Retention (%)')
axes[0].set_ylabel('Accuracy (%)')

# 第二个子图
axes[1].plot(x21, y21, 'k-', label='ReComp', linewidth=linewidth)  # 黑色线，不加点
axes[1].plot(x22, y22, 'o-', label='AS', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='dodgerblue')  # 蓝色线，带黑色边框的点
axes[1].plot(x23, y23, '^-', label='AS+H2O', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='lightsalmon')  # 红色线，带黑色边框的点
axes[1].set_title('OPT-13B', fontsize=fontsize)
axes[1].set_xlabel('Retention (%)')

# 第三个子图
axes[2].plot(x31, y31, 'k-', label='ReComp', linewidth=linewidth)  # 黑色线，不加点
axes[2].plot(x32, y32, 'o-', label='AS', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='dodgerblue')  # 蓝色线，带黑色边框的点
axes[2].plot(x33, y33, '^-', label='AS+H2O', linewidth=linewidth, markersize=markersize, markeredgecolor='k', markerfacecolor='lightsalmon')  # 红色线，带黑色边框的点
axes[2].set_title('OPT-30B', fontsize=fontsize)
axes[2].set_xlabel('Retention (%)')

# 调整布局和图例
# axes[0].legend()
axes[0].set_ylim(70, 90)
# x 轴刻度间隔
axes[0].xaxis.set_major_locator(ticker.MultipleLocator(15))  # 每隔 15 标记一个刻度
# y 轴刻度间隔
axes[0].yaxis.set_major_locator(ticker.MultipleLocator(15))
axes[1].set_ylim(70, 90)
axes[1].xaxis.set_major_locator(ticker.MultipleLocator(15))
axes[1].yaxis.set_major_locator(ticker.MultipleLocator(15))
axes[2].set_ylim(70, 90)
axes[2].xaxis.set_major_locator(ticker.MultipleLocator(15))
axes[2].yaxis.set_major_locator(ticker.MultipleLocator(15))


for ax in axes:
    ax.set_xlim(60, 0)
    # ax.legend()
    # 添加虚线网格
    ax.grid(True, linestyle='--', linewidth=0.7)  # 网格线样式为虚线，线宽为 0.7

# 创建一个统一的图例，横跨三个子图
# fig.legend(axes[0].get_lines(), ['ReComp', 'AS', 'AS+H2O'], loc='upper center', 
        #    bbox_to_anchor=(0.5, 1.08), ncol=3, frameon=False)
fig.legend(axes[0].get_lines(), ['ReComp', 'AS+H2O+LRU', 'HyperInfer'], loc='upper center', 
           bbox_to_anchor=(0.5, 1.06), ncol=3, frameon=False, fontsize=20, 
           markerscale=1.5, handlelength=3)
# plt.tight_layout(rect=[0, 0, 0, 3])
# 调整边距
# plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)



# 设置每个子图的外边框加粗
lwidth = 2
for ax in axes:
    ax.spines['top'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# 获取当前 py 文件名并替换扩展名为 .png
filename = os.path.splitext(os.path.basename(__file__))[0] + '.pdf'
plt.savefig(filename)
