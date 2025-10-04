#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 20
ylabelTextSize = 20
xtitleTextSize = 20
ytitleTextSize = 20

legendTextSize = 16
legendSize = 10
legendSkip = 140

# 定义绘画区域大小、线条粗细、轴样式
dimension = [240, 180]
lineWidth = 2.5
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'static_acc'
dataname1 = 'static_acc.data'

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[300, 300])

# 读取源数据table
t = table(file=dataname1)

# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[40, 60])
d2 = drawable(canvas=c, dimensions=dimension, coord=[50,50],
            xrange=[-0.6, t.getmax('rownumber')+0.6], yrange=[18, 34])
# 绘画边框和xy轴的文字
axis(drawable=d, style=axisstyle, ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='Accuracy (%)', doylabels=True, ytitleshift=[-2,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=40, yauto=['','', 5], xlabelrotate=0,
         xlabelshift=[0, -2.5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['50%', 0], ['25%', 1], ['10%', 2],['5%',3]])

axis(drawable=d2, style='y', ticstyle=axisticstyle,
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         # xtitle='Workload',
         ytitle='F1 Score (%)', doylabels=True, ytitleshift=[287,0], ylabelshift=[270,0],
         # linewidth=0.8,
         linewidth=lineWidth,
         xaxisposition=0, yauto=['','',4], xlabelrotate=0,
         xlabelshift=[0, -20],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['50%', 0], ['25%', 1], ['10%', 2],['5%',3]],
         )

p = plotter() # 画笔
L = legend() # 图例


series_list = ['A','B','C','D']
fillcolors    = ['lightblue', 'lightsalmon', 'wheat',  'lightgrey']
legend_names = ['ORI (OPT-6.7B)','SPI (OPT-6.7B)','ORI (OPT-30B)','SPI (OPT-30B)']


               
shiftx=[0, 0,0,0]
stylelst = ['circle', 'circle','triangle','triangle']
# pointscolor = ['dodgerblue', 'lightsalmon','red','black']
linecolor = ['black', 'black', 'black', 'black']
pointscolor = ['blue', 'dodgerblue','red','lightsalmon']

for i in range(2):
    p.line(drawable=d, table=t, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)
    p.points(drawable=d, table=t, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0],
             linecolor=linecolor[i], size=6, legend=L, legendtext=legend_names[i], style=stylelst[i],
             fill=True, fillcolor=pointscolor[i])
    
# 绘制C和D的数据
for i in range(2, 4):
    p.line(drawable=d2, table=t, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)
    p.points(drawable=d2, table=t, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0],
             linecolor=linecolor[i], size=6, legend=L, legendtext=legend_names[i], style=stylelst[i],
             fill=True, fillcolor=pointscolor[i])
    #### legend
L.draw(canvas=c, coord=[d.left()-10, d.top()+33], skipnext=2, 
     skipspace=legendSkip,hspace=5, fontsize=legendTextSize,
     width=legendSize, height=13, order=[0, 2, 1, 3])

c.render()