from plotter.plotter import Plotter
import numpy as np

# x_data = np.linspace(0, np.pi, 100)
# y_data = {"valeur intensité": (np.cos(x_data)**2)}
# Plotter("", "Graphique de la loi de Malus", x_data, y_data, x_axis_title="Angle relatif (rad)",
#         y_axis_title="Intensité relative", name_file="hallo", title_font_size =20, sub_font_size=17, step_xticks=0.2, step_yticks=0.05)

#read Csv file
myFile = np.genfromtxt(r"C:\Users\Alexandre\Desktop\alex library python\polarisation_reflexion.csv", delimiter=',')
x_data = myFile[:, 0]
y_data = {"Onde TE": myFile[:, 1], "Onde TM": myFile[:, 2]}
Plotter(output_path="", title="Coefficient de réflexion enfonction de la polarisation", x_data=x_data, y_data=y_data, name_file="graph_lab_polarisation",
        x_axis_title="Angle (°)", y_axis_title="Intensitée (V)")



#Plotter(output_path="", title="", x_data=x_data, y_data=y_data, name_file="",
#        x_axis_title="", y_axis_title="")
