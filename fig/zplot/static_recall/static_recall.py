#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 20
ylabelTextSize = 20
xtitleTextSize = 20
ytitleTextSize = 20

legendTextSize = 20
legendSize = 20
legendSkip = 80

# 定义绘画区域大小、线条粗细、轴样式
dimension = [320, 180]
lineWidth = 2.5
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'static_recall'
dataname1 = 'static_recall.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[80, 100])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='Ratio (%)', doylabels=True, ytitleshift=[5,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=80, yauto=['','', 5], xlabelrotate=0,
         xlabelshift=[0, -2],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['OPT-6.7B', 0], ['OPT-30B', 1]])

p = plotter() # 画笔
L = legend() # 图例


series_list = ['t10', 't20', 't30', 't40']
fillcolors    = ['lightblue', 'darkseagreen', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
legend_names = ['5%', '10%', '25%', '50%']


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
L.draw(canvas=c, coord=[d.left()+10, d.top()+15], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize, order=[0, 1, 2, 3])

c.render()