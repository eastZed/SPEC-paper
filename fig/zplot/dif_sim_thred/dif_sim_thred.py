#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 16
ylabelTextSize = 16
xtitleTextSize = 16
ytitleTextSize = 16

legendTextSize = 16
legendSize = 14
legendSkip = 200

# 定义绘画区域大小、线条粗细、轴样式
dimension = [460, 100]
lineWidth = 2
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'dif_sim_thred'
dataname1 = 'dif_sim_thred_load_ratio.data'
dataname2 = 'dif_sim_thred_acc.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[500, 500])

# 读取源数据table
t = table(file=dataname1)
t2 = table(file=dataname2)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 100])
d2 = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[76, 80])
# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     #     xtitle='Epoch',
          xtitle='Similarity Threshold',
         ytitle='Load Ratio (%)', doylabels=True, ytitleshift=[0,0], 
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','',25], xlabelrotate=0,
         xlabelshift=[0, -5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['1', 0], ['0.9', 1], ['0.8', 2],
                   ['0.7', 3], ['0.6', 4], ['0.5', 5],['0.4', 6],
                   ['0.3', 7], ['0.2', 8], ['0.1', 9], ['0', 10]
                   ],
         
         )
axis(drawable=d2, style='y', ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
     #     xtitle='Similarity Threshold',
         ytitle='Accuracy (%)', doylabels=True, ytitleshift=[500,0], 
         ylabelshift=[485,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','',1], xlabelrotate=0,
     #     xlabelshift=[0, -20],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['1', 0], ['0.9', 1], ['0.8', 2],
                   ['0.7', 3], ['0.6', 4], ['0.5', 5],['0.4', 6],
                   ['0.3', 7], ['0.2', 8], ['0.1', 9], ['0', 10]
                   ]
         )


p = plotter() # 画笔
L = legend() # 图例


series_list = ['loadratio']
fillcolors    = ['lightsalmon', 'lightblue',  'lightgrey']
legend_names = ['Load ratio', 'Accuracy']


for i in range(len(series_list)):
     p.verticalbars(drawable=d, table=t,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[i],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[i],
                    cluster=[i, len(series_list)])

stylelst = ['triangle', 'circle', 'square', 'triangle']
series_list = ['acc']
pointscolor = ['dodgerblue', 'wheat']
linecolor = ['black', 'black', 'black', 'black']
for i in range(len(series_list)):
     p.line(drawable=d2, table=t2, xfield='rownumber', yfield=series_list[i], linecolor='dodgerblue', linewidth=3)
     p.points(drawable=d2, table=t2, xfield='rownumber', yfield=series_list[i], shift=[0, 0], size=6, legend=L, legendtext = legend_names[1], style=stylelst[i], fill=True, fillcolor=pointscolor[i],
     linecolor=linecolor[i])
     

# # additional text
# x_start = 8
# x_step = 97
# y_starts = [-16, -16]
# NormalizedTextSize=10
# texts_lst = ['Arxiv', 'Products']
# for i in range(2):
#      c.text(coord=[d.left()+x_start+i*x_step+42, d.bottom()+y_starts[i]], rotate=0,text=texts_lst[i], size=NormalizedTextSize, anchor='c,h')

# c.text(coord=[d.left()+100, d.bottom()-18], rotate=0,text='Threshold', size=xtitleTextSize, anchor='c,h')

# # additional line
# line_xstart = 12
# line_step = 95
# line_len = 80
# line_ystarts = [-14, -14]
# for i in range(2):
#      c.line(coord=[[d.left()+line_xstart+i*line_step, d.bottom()+line_ystarts[i]], [d.left()+line_xstart+i*line_step+line_len, d.bottom()+line_ystarts[i]]])

#### legend
L.draw(canvas=c, coord=[d.left()+80, d.top()+14], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize, order=[0, 1, 2, 3])

c.render()