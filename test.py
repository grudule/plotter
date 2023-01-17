from plotter import plotter
import numpy as np
x_data = np.linspace(0,np.pi, 1000)
#x_data = (0,np.pi, 1000)
y_data = {"valeur intensité":np.cos(x_data)**2}
plotter.Plotter("", "Graphique de la loi de Malus",x_data,y_data, x_axis_title="Angle relatif (rad)", y_axis_title="Intensité relative", step_yticks=0.1)