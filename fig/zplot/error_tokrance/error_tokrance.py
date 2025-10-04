#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 16
ylabelTextSize = 16
xtitleTextSize = 16
ytitleTextSize = 16

legendTextSize = 16
legendSize = 10
legendSkip = 80

# 定义绘画区域大小、线条粗细、轴样式
dimension = [240, 180]
lineWidth = 2
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'error_tokrance'
dataname1 = 'error_tokrance.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[300, 300])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 100])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='Accuracy (%)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 25], xlabelrotate=0,
         xlabelshift=[0, -2.5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['0~5', 0], ['6~10', 1], ['11~15', 2]])

p = plotter() # 画笔
L = legend() # 图例


series_list = ['A', 'B']
fillcolors    = ['lightblue', 'lightsalmon', 'wheat',  'lightgrey']
legend_names = ['A', 'B']

# for i in range(len(series_list)):
#      p.verticalbars(drawable=d, table=t,
#                     xfield='rownumber', yfield=series_list[i], 
#                     fill=True,
#                     fillcolor=fillcolors[i],
#                     barwidth=0.6, 
#                     linewidth=lineWidth,
#                     legend = L, legendtext=legend_names[i],
#                     cluster=[i, len(series_list)])
               
shiftx=[0, 0]
stylelst = ['circle', 'triangle']
pointscolor = ['dodgerblue', 'lightsalmon']
for i in range(len(series_list)):
     p.points(drawable=d, table=t, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0], linecolor=pointscolor[i], size=6, legend=L, legendtext = legend_names[i], style=stylelst[i], fill=True, fillcolor=pointscolor[i])
     p.line(drawable=d, table=t, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)

# # additional text
# x_start = 8
# x_step = 97
# y_starts = [-16, -16]
# NormalizedTextSize=10
# texts_lst = ['Arxiv', 'Products']
# for i in range(2):
#      c.text(coord=[d.left()+x_start+i*x_step+42, d.bottom()+y_starts[i]], rotate=0,text=texts_lst[i], size=NormalizedTextSize, anchor='c,h')

# # additional line
# line_xstart = 12
# line_step = 95
# line_len = 80
# line_ystarts = [-14, -14]
# for i in range(2):
#      c.line(coord=[[d.left()+line_xstart+i*line_step, d.bottom()+line_ystarts[i]], [d.left()+line_xstart+i*line_step+line_len, d.bottom()+line_ystarts[i]]])

#### legend
L.draw(canvas=c, coord=[d.left()+40, d.top()+10], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize)

c.render()