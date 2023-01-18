from plotter.plotter import Plotter
import numpy as np



# Possible style for plot : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# Note empty string for style will create a classical line

# Possible markers for scatter : https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Possible fillstyle : https://matplotlib.org/3.2.2/gallery/lines_bars_and_markers/marker_fillstyle_reference.html

x_data = np.linspace(0, np.pi, 100)
y_data = {"valeur intensité": (np.cos(x_data)**2, "black", "", "full")}
Plotter("", "Graphique de la loi de Malus", x_data, y_data, x_axis_title="Angle relatif (rad)",
        y_axis_title="Intensité relative", name_file="hallo")


# Read UTF8 csv file template

# myFile = np.genfromtxt(r"path_to_your_file", delimiter=',')
# x_data = myFile[:, 0]
# y_data = {"name_of_data1": (myFile[:, 1],"<color>", "<type_of_line/marker_keep_it_empty_if_line>", "<fillstyle>"), "name_of_data2": (myFile[:, 1],"<color>", "<type_of_line/marker_keep_it_empty_if_line>", "<fillstyle>"),}
# Plotter(output_path="", title="" ,x_data=x_data, y_data=y_data, name_file="",
#        x_axis_title="", y_axis_title="")