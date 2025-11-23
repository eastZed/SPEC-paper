#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 8
ylabelTextSize = 8
xtitleTextSize = 8
ytitleTextSize = 8

legendTextSize = 7
legendSize = 8
legendSkip = 195

# 定义绘画区域大小、线条粗细、轴样式
dimension = [110, 50]
lineWidth = 0.8
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'acc_cov'
dataname1 = 'indiv_ds1.data'
dataname2 = 'indiv_ds2.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)
t2 = table(file=dataname2)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[80, 100])
d2 = drawable(canvas=c, dimensions=dimension, coord=[190,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[80, 100])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='(a) RTE', xtitleshift=[0,5],
         ytitle='Accuracy', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=75, yauto=[80,100, 5], xlabelrotate=0,
         xlabelshift=[0, 13],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-13B', 0],['OPT-30B',1]])
axis(drawable=d2, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='(b) COPA', xtitleshift=[0, 5],
         ytitle='Accuracy', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=75, yauto=[80,100, 5], xlabelrotate=0,
         xlabelshift=[0, 13],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-13B', 0],['OPT-30B', 1]])

p = plotter() # 画笔
L = legend() # 图例


series_list = ['his', 'hyperinfer']
fillcolors    = ['lightblue', 'darkseagreen', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
fillcolors    = ['wheat', 'darkseagreen','lightblue',  'lightsalmon', 'lightcoral',  ]
legend_names = ['HISTORY', 'LAYER-WISE']


for i in range(len(series_list)):
     p.verticalbars(drawable=d, table=t,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[i],
                    cluster=[i, len(series_list)])

for i in range(len(series_list)):
     p.verticalbars(drawable=d2, table=t2,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    cluster=[i, len(series_list)])


#### legend
L.draw(canvas=c, coord=[d.left(), d.top()+8], skipnext=1, 
     skipspace=legendSkip,hspace=2, fontsize=legendTextSize,  
     width=legendSize, height=legendSize, order=[0, 1, 2, 3,4])

c.render()