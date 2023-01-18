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

#read Csv file
# myFile = np.genfromtxt(r"C:\Users\Alexandre\Desktop\alex library python\polarisation_reflexion.csv", delimiter=',')
# x_data = myFile[:, 0]
# x = np.linspace(0, 90, 15)
# cos_thetha2 = np.sqrt(1-(np.sin(x)/1.5)**2)
# y_TE = ((1*np.cos(x) - 1.5 * cos_thetha2) / (1.5 * cos_thetha2 + 1*np.cos(x)))**10
# y_TM = (cos_thetha2-1.5*np.cos(x))/(1.5*np.cos(x)+cos_thetha2)
# y_data = {"Onde TE": (myFile[:, 1],"black", "--o", "none"), "Onde TM": (myFile[:, 2], "black", "o", "none"), "Onde TM_th": (y_TM, "", "", "full", 0.3)}
# Plotter(output_path="", title="" ,x_data=x_data, y_data=y_data, name_file="graph_lab_polarisation",
#        x_axis_title="Angle [°]", y_axis_title="Intensitée [V]", color="Black", fig_size=(8,6))



#Plotter(output_path="", title="", x_data=x_data, y_data=y_data, name_file="",
#        x_axis_title="", y_axis_title="")
