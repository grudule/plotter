from plotter.plotter import Plotter
import numpy as np
from scipy.optimize import curve_fit
from symfit import parameters, variables, sin, cos, Fit

# Possible style for plot : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# Note empty string for style will create a classical line

# Possible markers for scatter : https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Possible fillstyle : https://matplotlib.org/3.2.2/gallery/lines_bars_and_markers/marker_fillstyle_reference.html
# myFile = np.genfromtxt(
#     r"C:\Users\Alexandre\Desktop\alex library python\plotter\Book1.csv", delimiter=',')
#y2 = np.polyval(np.poly1d(np.polyfit(x_1, y_1, 100)), x_1)

D = 12
n = 1.33
theta = np.linspace(0,np.pi/2, 10)
print(theta*180/np.pi)
x_positions = D* (((n**(2)-1)*np.sin(theta)**(3))/(n**(2)-np.sin(theta)**(2))**(3/2))
y_positions = -D* ((n**(2)*np.cos(theta)**(3))/(n**(2)-np.sin(theta)**(2))**(3/2))
x_data = {"empirique":x_positions,
          "reel":0
          }
y_data = {
          "": (y_positions,"empirique", "gray", "o", "full"),
          "position réelle" :(-12 ,"reel", "black", "o", "full")
        }
Plotter("", "", x_data, y_data,
        x_axis_title="Position horizontale [cm]", y_axis_title="Position verticale [cm]",name_file="dev2_optique", fig_size=(8,6), sub_font_size=16, ticks_font_size=12, annotation= [["0°", (x_positions[0],y_positions[0]),(0, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}], 
                                                                                                                                                                                                            ["10°", (x_positions[1],y_positions[1]),(1, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["20°", (x_positions[2],y_positions[2]),(2, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["30°", (x_positions[3],y_positions[3]),(3, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["40°", (x_positions[4],y_positions[4]),(4, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["50°", (x_positions[5],y_positions[5]),(5, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["60°", (x_positions[6],y_positions[6]),(7, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["70°", (x_positions[7],y_positions[7]),(10, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["80°", (x_positions[8],y_positions[8]),(13, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["90°", (x_positions[9],y_positions[9]),(14, 1),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}],
                                                                                                                                                                                                            ["Position réelle", (0,-12),(9, -12),{"facecolor":'black', "arrowstyle":"->","linewidth":0.5,}]])
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

#x1 = np.linspace(10*np.pi/180, 75*np.pi/180, 100)
# x2 = myFile[:, 0]*np.pi/180

# def reflected_intensity_TM(theta1, intensity, n2):
#     n1 = 1.0
#     numerator_TM = n1*np.sqrt(1-(n1/n2*np.sin(theta1))**2)-n2*np.cos(theta1)
#     denominator_TM = n1*np.sqrt(1-(n1/n2*np.sin(theta1))**2)+n2*np.cos(theta1)
#     y_TM = intensity*(numerator_TM / denominator_TM)**2
#     return y_TM

# popt, pcov = curve_fit(reflected_intensity_TM,x2, myFile[:, 2], p0=[100,1.5] )
# perr = np.sqrt(np.diag(pcov))

# bestInt = popt[0] #intensity
# best_Index = popt[1] # N2
# deltaIntensity = perr[0] #incertitude intensité
# deltaIndex = perr[1]
# print(best_Index, deltaIndex)
# y_TM_curved = reflected_intensity_TM(x1, bestInt, best_Index)



### curve fitting fft
# def fourier_series(x, f, n=0):
#     """
#     Returns a symbolic fourier series of order `n`.

#     :param n: Order of the fourier series.
#     :param x: Independent variable
#     :param f: Frequency of the fourier series
#     """
#     # Make the parameter objects for all the terms
#     a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n + 1)]))
#     sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n + 1)]))
#     # Construct the series
#     series = a0 + sum(ai * cos(i * f * x) + bi * sin(i * f * x)
#                      for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
#     return series

# x, y = variables('x, y')
# w, = parameters('w')
# model_dict = {y: fourier_series(x, f=w, n=3)}
# fit = Fit(model_dict, x=x_1, y=y_1)
# fit_result = fit.execute()
# y2 = fit.model(x=x_1, **fit_result.params).y
# print(fit_result)
