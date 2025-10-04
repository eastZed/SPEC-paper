#! /usr/bin/env python

from zplot import *

# 定义字体大小
xlabelTextSize = 12
ylabelTextSize = 12
xtitleTextSize = 12
ytitleTextSize = 12

legendTextSize = 12
legendSize = 10
legendSkip = 112

# 定义绘画区域大小、线条粗细、轴样式
dimension = [460, 150]#[240, 150]
lineWidth = 0
axisstyle = 'box'
axisticstyle = 'in'

# 定义生成文件名、来源数据文件名
filename = 'pload_bottleneck'


 

# 创建整个画布
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, title=filename, dimensions=[400, 100])

# 读取源数据table
t1 = table(file='recomputation.data')
t1u = table(file='recomputation_u.data')
t2 = table(file='prefix_load_gpu.data')
t2u = table(file='prefix_load_gpu_u.data')
t3 = table(file='prefix_load_cpu.data')
t3u = table(file='prefix_load_cpu_u.data')
t4 = table(file='prefix_load_ssd.data')
t4u = table(file='prefix_load_ssd_u.data')
t5 = table(file='remain.data')
t5u = table(file='remain_u.data')


# 创建绘画框区域，定义横纵坐标轴的逻辑范围
d_btm = drawable(canvas=c, 
          xrange=[-0.8, t1u.getmax('rownumber')+0.8],
          yrange=[0, 150],
          dimensions=[320, 53], coord=[51, 65])#53

d_mid = drawable(canvas=c, 
          xrange=[-0.8, t1.getmax('rownumber')+0.8],
          yrange=[200, 1200],
          dimensions=[320, 50], coord=[51,123]) 


# 绘画边框和xy轴的文字
axis(drawable=d_btm, style='xy', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='Number of tokens in prefix',
         ytitle='TTFT (ms)', doylabels=True, ytitleshift=[-8,22],
         linewidth=1.2,
         #xaxisposition=0, yauto=['','',400], 
         xlabelrotate=0,
         xlabelshift=[0, -2.5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xmanual=[['128',0],['256', 1], ['512', 2], ['1k', 3], ['2k', 4], ['4k', 5],['8k',6]],
         ymanual=[['3', 30], ['9', 90]])

axis(drawable=d_mid, style='y', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         doylabels=True, ytitleshift=[0,0],
         linewidth=1.2,
         #xaxisposition=0, 
         #yauto=['','',400], xlabelrotate=0,
         xlabelshift=[0, -2.5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         ymanual=[['20', 200],['70', 700],['120',1200]],
         )

c.text(coord= [42,108],text = '15',size = 12, rotate=0)
c.text(coord= [51,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [51,120.6],text = '/',size = 8, rotate=-45)
c.line(coord= [[52, 173],[371, 173]] , linewidth=1.2)
c.line(coord= [[371, 65],[371, 174]] , linewidth=1.2)



p = plotter() # 画笔
L = legend() # 图例


series_list = ['defalt', 'b1','b2','b3']
fillcolors    = ['dodgerblue', 'lightsalmon', 'lightgrey', 'orange', 'lightsalmon','mediumseagreen','orange']
legend_names = ['ReComp', 'GPU load time', 'CPU load time', 'SSD load time','QueryComp']


for i in range(len(series_list)):#recomputation
     if i==0:
          p.verticalbars(drawable=d_btm, table=t5,
               xfield='rownumber', yfield=series_list[i], 
               fill=True,
               fillcolor=fillcolors[2],legendtext=legend_names[4],legend=L,
               barwidth=0.7, 
               linewidth=lineWidth,
               cluster=[i, len(series_list)])
     else:
               p.verticalbars(drawable=d_btm, table=t5,
               xfield='rownumber', yfield=series_list[i], 
               fill=True,
               fillcolor=fillcolors[2],
               barwidth=0.7, 
               linewidth=lineWidth,
               cluster=[i, len(series_list)])


for i in range(len(series_list)):##ssd
     if i== 0:
          p.verticalbars(drawable=d_btm, table=t4,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[4],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[3],
                    cluster=[i, len(series_list)])
     else:
          p.verticalbars(drawable=d_btm, table=t4,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[4],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    cluster=[i, len(series_list)])



for i in range(len(series_list)):###cpu
     if i== 0:
          p.verticalbars(drawable=d_btm, table=t3,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[5],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[2],
                    cluster=[i, len(series_list)])
     else:
          p.verticalbars(drawable=d_btm, table=t3,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[5],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    cluster=[i, len(series_list)])

for i in range(len(series_list)):#gpu
     if i==0:
          p.verticalbars(drawable=d_btm, table=t2,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[3],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    legend = L, legendtext=legend_names[1],
                    cluster=[i, len(series_list)])
     else:
          p.verticalbars(drawable=d_btm, table=t2,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[3],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    cluster=[i, len(series_list)])


for i in range(len(series_list)):#recomputation
     if i==0:
          p.verticalbars(drawable=d_btm, table=t1,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[0],
                    barwidth=0.7, 
                    linewidth=lineWidth,legendtext=legend_names[0],
                    legend = L, 
                    cluster=[i, len(series_list)])   
     else:
          p.verticalbars(drawable=d_btm, table=t1,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[0],
                    barwidth=0.7, 
                    linewidth=lineWidth,
                    cluster=[i, len(series_list)])               

######==========the upper 
for i in range(len(series_list)):#computation
     p.verticalbars(drawable=d_mid, table=t5u,
               xfield='rownumber', yfield=series_list[i], 
               fill=True,
               fillcolor=fillcolors[2],
               barwidth=0.7, 
               linewidth=0,
               cluster=[i, len(series_list)])



for i in range(len(series_list)):#ssd
     p.verticalbars(drawable=d_mid, table=t4u,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[4],
                    barwidth=0.7, 
                    linewidth=0,
                    #legend = L, 
                    cluster=[i, len(series_list)])


for i in range(len(series_list)):
          p.verticalbars(drawable=d_mid, table=t3u,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[5],
                    barwidth=0.7, 
                    linewidth=0,
                    cluster=[i, len(series_list)])

# for i in range(len(series_list)):
#           p.verticalbars(drawable=d_mid, table=t2u,
#                     xfield='rownumber', yfield=series_list[i], 
#                     fill=True,
#                     fillcolor=fillcolors[3],
#                     barwidth=0.7, 
#                     linewidth=0.5,
#                     cluster=[i, len(series_list)])

for i in range(len(series_list)):
          p.verticalbars(drawable=d_mid, table=t1u,
                    xfield='rownumber', yfield=series_list[i], 
                    fill=True,
                    fillcolor=fillcolors[0],
                    barwidth=0.7, 
                    linewidth=0,
                    cluster=[i, len(series_list)])               

c.text(coord= [262,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [262,120.6],text = '/',size = 8, rotate=-45)
c.text(coord= [282,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [282,120.6],text = '/',size = 8, rotate=-45)
c.text(coord= [304,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [304,120.6],text = '/',size = 8, rotate=-45)
c.text(coord= [324,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [324,120.6],text = '/',size = 8, rotate=-45)
c.text(coord= [339,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [339,120.6],text = '/',size = 8, rotate=-45)
c.text(coord= [346,116.6],text = '/',size = 8, rotate=-45)
c.text(coord= [346,120.6],text = '/',size = 8, rotate=-45)

L.draw(canvas=c, coord=[d_mid.left()+5, d_mid.top()+22], skipnext=2, 
     skipspace=legendSkip,hspace=4, fontsize=legendTextSize,  
     width=legendSize, height=legendSize,order=[4,1,3,0,2])

c.render()