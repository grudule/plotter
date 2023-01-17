from plotter.plotter import Plotter
import numpy as np
x_data = np.linspace(0, np.pi, 100)
y_data = {"valeur intensité": (np.cos(x_data)**2)}
Plotter("", "Graphique de la loi de Malus", x_data, y_data, x_axis_title="Angle relatif (rad)",
        y_axis_title="Intensité relative", name_file="hallo", title_font_size =20, sub_font_size=17, step_xticks=0.2, step_yticks=0.05)

# read Csv file
# myFile = np.genfromtxt(
#     r"C:\Users\Alexandre\Desktop\alex library python\plotter\Book1.csv", delimiter=',')
# x_data = myFile[:, 0]
# y_data = {"valeur": myFile[:, 1]}
# Plotter(output_path="", title="", x_data=x_data, y_data=y_data, name_file="",
#         x_axis_title="", y_axis_title="")
