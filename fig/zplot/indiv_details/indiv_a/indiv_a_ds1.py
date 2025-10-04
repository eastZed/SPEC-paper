#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 14
ylabelTextSize = 14
xtitleTextSize = 14
ytitleTextSize = 14

legendTextSize = 8
legendSize = 8
legendSkip = 70

# 定义绘画区域大小、线条粗细、轴样式
dimension = [400, 70]
lineWidth = 1.2
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'indiv_a_ds1'
dataname1 = 'indiv_a_ds1.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[0, 100])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='Layer ID',
         ytitle='Ratio (%)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','', 25], xlabelrotate=0,
         xlabelshift=[0, -1],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
     #     xmanual=[['0', 1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10],
     #              ['11', 11], ['12', 12], ['13', 13], ['14', 14], ['15', 15], ['16', 16], ['17', 17], ['18', 18], ['19', 19], ['20', 20],
     #              ['21', 21], ['22', 22], ['23', 23], ['24', 24], ['25', 25], ['26', 26], ['27', 27], ['28', 28], ['29', 29], ['30', 30], ['31', 31], ['32', 32]
                  
     #              ]
         xmanual=[['0', 0], ['4', 4], ['8', 8], ['12', 12], ['16', 16], ['20', 20], ['24', 24],
                  ['28', 28], ['32', 32], ['36', 36], ['40', 40], ['44', 44]]
         )

p = plotter() # 画笔
L = legend() # 图例


series_list = ['layer',]
fillcolors    = ['lightblue', 'darkseagreen', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
legend_names = ['ReComp', 'Simi', 'Reorder', 'Scache']


for i in range(len(series_list)):
     p.verticalbars(drawable=d, table=t,
                    xfield='rownumber', 
                    yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[0],
                    barwidth=0.6, 
                    linewidth=lineWidth,
                    # legend = L, 
                    # legendtext=legend_names[i],
                    cluster=[i, len(series_list)])


#### legend
L.draw(canvas=c, coord=[d.left(), d.top()+10], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize,)

c.render()