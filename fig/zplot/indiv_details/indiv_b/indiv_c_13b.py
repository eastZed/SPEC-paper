#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 12
ylabelTextSize = 12
xtitleTextSize = 12
ytitleTextSize = 12

legendTextSize = 12
legendSize = 12
legendSkip = 100

# 定义绘画区域大小、线条粗细、轴样式
dimension = [175, 100]
lineWidth = 1.2
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'indiv_c_13b'
dataname1 = 'indiv_b_ckratio.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 400])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[25, 100])

# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='GPU hit ratio (%)', doylabels=True, ytitleshift=[0,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=25, yauto=['','', 25], xlabelrotate=14,
         xlabelshift=[-12, -5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['PIQA', 0], ['RTE',1],['COPA',2],['OpenBookQA',3]])

p = plotter() # 画笔
L = legend() # 图例


series_list = ['as_', 'sti']
fillcolors    = ['lightblue', 'lightcoral', 'wheat', 'lightsalmon', 'darkseagreen',  'lightgrey']
legend_names = ['+RO', 'All']


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
L.draw(canvas=c, coord=[d.left()+20, d.top()+10], skipnext=1, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize)

c.render()