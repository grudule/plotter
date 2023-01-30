from plotter.plotter import Plotter
import numpy as np
from scipy.optimize import curve_fit


# Possible style for plot : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# Note empty string for style will create a classical line

# Possible markers for scatter : https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Possible fillstyle : https://matplotlib.org/3.2.2/gallery/lines_bars_and_markers/marker_fillstyle_reference.html
# myFile = np.genfromtxt(
#     r"C:\Users\Alexandre\Desktop\alex library python\plotter\Book1.csv", delimiter=',')
l = np.linspace(1, 1.6, 10000)
# x2 = (myFile[:, 0]*np.pi)/180
# print(x2, myFile[:, 0])
x_data = {"theorical":l,
          }
#dispersion_equation = np.sqrt( 1 + (0.696166*(λ2**2))/((λ2**2)-0.068404**2) + (0.407942*λ2**2)/((λ2**2)-0.116241**2) + (0.897479*λ2**2)/((λ2**2)-9.896161**2))


A = [0.696166, 0.407942, 0.897479]
lambda_i = [0.068404, 0.116241, 9.896161]
y = np.ones(1000)
y = 0.696166 * (0.068404**2 * (3*(l**2) + 0.068404**2))/(l**2-0.068404**2)**3 + 0.407942 * (0.116241**2 * (3*(l**2) + 0.116241**2))/(l**2-0.116241**2)**3 + 0.897479 *(9.896161**2 * (3*(l**2) + 9.896161**2))/(l**2-9.896161**2)**3
y = (-l/(3*(10**14)))*y
print(np.interp(0, y,l))
y_data = {
          "": (y,"theorical", "black", "", "full"), 
          "z": (0*l,"theorical", "black", "--", "full")
        }

Plotter("", "", x_data, y_data,
        x_axis_title="Longueur d'onde [µm]", y_axis_title="Indice de réfraction [-]",name_file="dev1 onde", fig_size=(6,4), sub_font_size=12, step_xticks=0.05)

#read Csv file
# myFile = np.genfromtxt(r"C:\Users\Alexandre\Desktop\alex library python\polarisation_reflexion.csv", delimiter=',')
# x_data = myFile[:, 0]
# x = np.linspace(0, 90, 15)
# cos_thetha2 = np.sqrt(1-(np.sin(x)/1.5)**2)
# y_TE = ((1*np.cos(x) - 1.5 * cos_thetha2) / (1.5 * cos_thetha2 + 1*np.cos(x)))**10
# y_TM = (cos_thetha2-1.5*np.cos(x))/(1.5*np.cos(x)+cos_thetha2)
# y_data = {"Onde TE": (myFile[:, 1]), "Onde TM": (myFile[:, 2], "black", "o", "none"), "Onde TM_th": (y_TM, "", "", "full", 0.3)}
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
# def reflected_intensity_TE(theta1, intensity, n2):
#     n1 = 1.0
#     numerator_TE = n1*np.cos(theta1)-n2*np.sqrt(1-(n1/n2*np.sin(theta1))**2)
#     denominator_TE = n1*np.cos(theta1)+n2*np.sqrt(1-(n1/n2*np.sin(theta1))**2)
#     y_TE = intensity*(numerator_TE / denominator_TE)**2
#     return y_TE

# popt, pcov = curve_fit(reflected_intensity_TE,x2, myFile[:, 1], p0=[100,1.5] )
# perr = np.sqrt(np.diag(pcov))

# bestInt = popt[0] #intensity
# best_Index = popt[1] # N2
# deltaIntensity = perr[0] #incertitude intensité
# deltaIndex = perr[1]
# print(best_Index, deltaIndex)
# y_TE_curved = reflected_intensity_TE(x1, bestInt, best_Index)

# popt, pcov = curve_fit(reflected_intensity_TM,x2, myFile[:, 2], p0=[100,1.5] )
# perr = np.sqrt(np.diag(pcov))

# bestInt = popt[0] #intensity
# best_Index = popt[1] # N2
# deltaIntensity = perr[0] #incertitude intensité
# deltaIndex = perr[1]
# print(best_Index, deltaIndex)
# y_TM_curved = reflected_intensity_TM(x1, bestInt, best_Index)

