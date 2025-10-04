#! /usr/bin/env python


from zplot import *


bartypes = [('solid', 1, 1),
            ('solid', 1, 5),
            ('solid', 1, 5),
            ('solid', 1, 5)]

xlabelTextSize =10
ylabelTextSize =10
xtitleTextSize = 10
ytitleTextSize = 10
legendTextSize = 12

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'overall_acc_ds4', dimensions=['6.5in', '3.2in'])

##################################a###################################
t1 = table(file='opt67.data')

d1 = drawable(canvas=c, xrange=[-0.5, t1.getmax('rownumber')+0.5], coord=['0.5in', '0.7in'],
             yrange=[0, 100],dimensions=['1.6in', '1.2in'])

axis(drawable=d1, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='retention', ytitle='Accuracy (%)', doylabels=True,ytitleshift=[0,0],
         linewidth=1,
         xaxisposition=0.5, yauto=[0,100,20],
         xlabelrotate=0,
         xlabelshift=[0,0],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xtitleshift=[0,0],
         xmanual=[['50%', 0], ['40%', 1], ['30%', 2], ['20%', 3],['10%',4]]
         )

p = plotter()
L = legend()

series_list = ['a','b','c']
fillcolors    = ['lightblue', 'lightsalmon', 'wheat',  'lightgrey']
legend_names = ['Recomp','AS','AS+CPU']


               
shiftx=[0, 0,0,0]
stylelst = ['circle', 'circle','triangle','triangle']
pointscolor = ['dodgerblue', 'lightsalmon','red','black']
for i in range(len(series_list)):
     p.points(drawable=d1, table=t1, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0], linecolor=pointscolor[i], size=6, legend=L, legendtext = legend_names[i], style=stylelst[i], fill=True, fillcolor=pointscolor[i])
     p.line(drawable=d1, table=t1, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)


    
c.text(coord=[d1.left()+52, d1.top()-115], rotate=0, text='(a)', size=10, color= 'black', anchor='l,h')


##############################Batchsize#################################
t2 = table(file='opt13.data')

d2 = drawable(canvas=c, xrange=[-0.5, t2.getmax('rownumber')+0.5],  coord=['2.5in', '0.7in'],
             yrange=[0, 100],dimensions=['1.6in', '1.2in'])

axis(drawable=d2, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='retention', ytitle='', doylabels=True,ytitleshift=[0,0],
         linewidth=1,
         xaxisposition=0.5, yauto=[0,100,20 ],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xtitleshift=[0,0], 
         xmanual=[['50%', 0], ['40%', 1], ['30%', 2], ['20%', 3],['10%',4]]
         )

p = plotter()
L = legend()

for i in range(len(series_list)):
     p.points(drawable=d2, table=t2, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0], linecolor=pointscolor[i], size=6, legend=L, legendtext = legend_names[i], style=stylelst[i], fill=True, fillcolor=pointscolor[i])
     p.line(drawable=d2, table=t2, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)

c.text(coord=[d2.left()+52, d2.top()-115], rotate=0, text='(b)', size=10, color= 'black', anchor='l,h')

##############################sequence#################################

t3 = table(file='opt30.data')

d3 = drawable(canvas=c, xrange=[-0.5, t3.getmax('rownumber')+0.5],  coord=['4.5in', '0.7in'],
             yrange=[0, 100],dimensions=['1.6in', '1.2in'])

axis(drawable=d3, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, yminorticcnt=0,
         xtitle='retention', ytitle='', doylabels=True,ytitleshift=[0,0],
         linewidth=1,
         xaxisposition=0.5, yauto=[0,100,20],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         xtitleshift=[0,0],
         xmanual=[['50%', 0], ['40%', 1], ['30%', 2], ['20%', 3],['10%',4]]
         )

p = plotter()
L = legend()

for i in range(len(series_list)):
     p.points(drawable=d3, table=t3, xfield='rownumber', yfield=series_list[i], shift=[shiftx[i], 0], linecolor=pointscolor[i], size=6, legend=L, legendtext = legend_names[i], style=stylelst[i], fill=True, fillcolor=pointscolor[i])
     p.line(drawable=d3, table=t3, xfield='rownumber', yfield=series_list[i], linecolor=pointscolor[i], linewidth=3)




c.text(coord=[d3.left()+52, d3.top()-115], rotate=0, text='(c)', size=10, color= 'black', anchor='l,h')

L.draw(canvas=c, coord=[d1.left()+80, d1.top()+15], width=8, height=8, fontsize=legendTextSize, skipnext=1, skipspace=120, vskip=5)

c.render()