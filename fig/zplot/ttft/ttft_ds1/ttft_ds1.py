#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 10
ylabelTextSize = 10
xtitleTextSize = 10
ytitleTextSize = 10

legendTextSize = 10
legendSize = 10
legendSkip = 100

# 定义绘画区域大小、线条粗细、轴样式
dimension = [320, 80]
lineWidth = 1
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'ttft_ds1_ds2'
dataname1 = 'ttft_ds1.data'
dataname2 = 'ttft_ds2.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 4])
d2 = drawable(canvas=c, dimensions=dimension, coord=[150,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 4])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='TTFT (s)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 1], xlabelrotate=0,
         xlabelshift=[0, -2],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-6.7B', 0], ['OPT-13B', 1],['OPT-30B',2]])
axis(drawable=d2, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='TTFT (s)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 1], xlabelrotate=0,
         xlabelshift=[0, -2],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-6.7B', 0], ['OPT-13B', 1],['OPT-30B',2]])

p = plotter() # 画笔
L = legend() # 图例


series_list = ['rc', 'as_', 'ash2o', 'ash2olfu', 'ours']
fillcolors    = ['lightblue', 'darkseagreen', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
fillcolors    = ['lightgrey',  'wheat', 'lightblue', 'darkseagreen', 'lightsalmon'  ]
legend_names = ['ReComp', 'AS-like', 'AS+H2O+LRU', 'AS+H2O+LFU', 'IMPRESS']


for i in range(len(series_list)):
     p.verticalbars(drawable=d, table=t,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[i],
                    cluster=[i, len(series_list)])


#### legend
L.draw(canvas=c, coord=[d.left()+10, d.top()+10], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize, order=[0, 1, 2, 3,4])

c.render()