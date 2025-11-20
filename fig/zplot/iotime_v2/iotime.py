#! /usr/bin/env python

from zplot import *
import types

if not hasattr(types, 'ListType'):
    types.ListType = list

# 定义字体大小
xlabelTextSize = 8
ylabelTextSize = 8
xtitleTextSize = 8
ytitleTextSize = 8

legendTextSize = 8
legendSize = 8
legendSkip = 90

# 定义绘画区域大小、线条粗细、轴样式
dimension = [110, 50]
lineWidth = 0.8
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'iotime'
dataname1 = 'iotime_ds1.data'
dataname2 = 'iotime_ds2.data'

# 直接读取数据文件
def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        # 跳过注释行
        for line in lines:
            if line.startswith('#'):
                continue
            parts = line.strip().split()
            if len(parts) >= 8:  # 确保有足够的数据列
                data.append([float(x) for x in parts[1:]])  # 跳过第一列（名称）
    return data

# 读取数据
data1 = read_data(dataname1)  # [[0, 3.467387073, 2.532412529, ...], [0, 2.127592006, 1.542820365, ...]]
data2 = read_data(dataname2)

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)
t2 = table(file=dataname2)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 4])
d2 = drawable(canvas=c, dimensions=dimension, coord=[190,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 5])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='(a) RTE',
         ytitle='I/O Time (s)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 1], xlabelrotate=0,
         xlabelshift=[0, 0],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-13B', 0],['OPT-30B',1]],
         ymanual=[['0', 0], ['1', 1], ['2', 2], ['3', 3]]
         )
axis(drawable=d2, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='(b) COPA',
         ytitle='I/O Time (s)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 2], xlabelrotate=0,
         xlabelshift=[0, 0],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-13B', 0],['OPT-30B',1]],
         ymanual=[['0', 0], ['2', 2], ['4', 4]]
         )

p = plotter() # 画笔
L = legend() # 图例


series_list = ['rc', 'as_', 'ash2o', 'ash2olfu', 'ours', 'hyperinfer', 'oracle']
#fillcolors    = ['lightblue', 'darkseagreen', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
fillcolors    = ['lightgrey',  'wheat', 'darkseagreen','lightblue','lightsalmon', 'lightcoral','dodgerblue' ]
legend_names = ['ReComp', 'AS-like', 'AS+H2O+LRU', 'AS+H2O+LFU', 'IMPRESS',  'HyperInfer', 'Oracle']


for i in range(1, len(series_list)):
     p.verticalbars(drawable=d, table=t,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[i],
                    cluster=[i, len(series_list)])

for i in range(1, len(series_list)):
     p.verticalbars(drawable=d2, table=t2,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    # legend = L, legendtext=legend_names[i],
                    cluster=[i, len(series_list)])

# 需要标注的 series 索引（在 series_list 中的索引）
# series_list = ['rc', 'as_', 'ash2o', 'ash2olfu', 'ours', 'hyperinfer', 'oracle']
# 最后两个是 hyperinfer (5) 和 oracle (6)
value_series_indices = [5, 6]

barwidth = 0.6
n = len(series_list)
# cluster_width 和 step 可以根据实际效果微调
cluster_width = barwidth * 1.1
step = cluster_width / n

# ---------- 左侧子图 d（对应 dataname1 / data1） ----------
for row_idx in range(len(data1)):
    # x 轴 rownumber：你的坐标是 [0, t.getmax('rownumber')+0.6]，所以这里用 0,1,2,... 对应 OPT-13B, OPT-30B ...
    x = row_idx

    for s_idx in value_series_indices:
        # 对应到 data1 里的列索引：
        # data1[row] 里第 0 列是 series_list[1]，所以是 s_idx - 1
        # col_idx = s_idx - 1
        col_idx = s_idx
        y_val = float(data1[row_idx][col_idx])

        # 计算该 cluster 中这一根 bar 的 x 位置（数据坐标）
        x_center = x
        x_left = x_center - cluster_width / 2.0
        x_pos = x_left + s_idx * step + step / 2.0 + 0.025  # 0.05 是微调值，可以根据实际效果调整

        # 文本 y 位置：柱子顶部往上偏一点
        y_pos = y_val + 0.5   # 0.05 可按图的大小改成 0.1/0.2

        # 将数据坐标映射为画布坐标
        cx, cy = d.map([x_pos, y_pos])

        # 在画布坐标上画文字
        c.text(coord=[cx, cy],
               text='%.2f' % y_val,  # 这里是保留两位小数，你也可以用 '%.1f' 或 '%d'
               anchor='c',
               size=5.5,
               rotate = 90)

# ---------- 右侧子图 d2（对应 dataname2 / data2） ----------
for row_idx in range(len(data2)):
    x = row_idx

    for s_idx in value_series_indices:
        # col_idx = s_idx - 1
        col_idx = s_idx
        y_val = float(data2[row_idx][col_idx])

        x_center = x
        x_left = x_center - cluster_width / 2.0
        x_pos = x_left + s_idx * step + step / 2.0 + 0.025

        y_pos = y_val + 0.7

        cx, cy = d2.map([x_pos, y_pos])

        c.text(coord=[cx, cy],
               text='%.2f' % y_val,
               anchor='c',
               size=5.5,
               rotate = 90)

#### legend
# L.draw(canvas=c, coord=[d.left()-7, d.top()+7], skipnext=1, 
#      skipspace=legendSkip,hspace=2, fontsize=legendTextSize,  
#      width=legendSize, height=legendSize, order=[0, 1, 2, 3,4, 5])
L.draw(canvas=c, coord=[d.left()-7, d.top()+20], skipnext=2, 
     skipspace=legendSkip, hspace=2, fontsize=legendTextSize,  
     width=legendSize, height=legendSize, order=[0, 1, 2, 3, 4, 5])

c.render()