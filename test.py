from plotter.plotter import *
x = [0,1,2]
y = [2,6,2]
output_path = ""
fig = Plotter(output_path,title="test", x_data= x, y_data= y, y_axis_title="yoh", font_size=16)
print(fig.y_axis_title)
