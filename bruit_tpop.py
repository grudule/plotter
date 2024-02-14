import glob
from plotter.plotter import Plotter
import numpy as np
import pandas as pd


path = r"D:\drive\OneDrive - Université Laval\Cours laval\2. Année 2\H2023\travaux pratique optique\données bruit"
csv_liste = glob.glob(path + r"\*.csv")
mean11 = []
mean12 = []
std12 = []
mean13 = []
mean21 = []
mean22 = []
mean23 = []
for i in csv_liste:
    myFile = np.genfromtxt(i, delimiter=',')
    x_data = myFile[2:, 0]
    y_data1 = myFile[2:, 1]
    y_data2 = myFile[2:, 2]
    y_data1 = y_data1/np.amax(y_data1)
    y_data2 = y_data2/np.amax(y_data2)
    part2_index = np.where(x_data == 0)
    part3_index = np.where(x_data == 95.6000E-03)
    y_data1_part1 = y_data1[2:part2_index[0][0]]
    y_data1_part2 = y_data1[part2_index[0][0]:part3_index[0][0]]
    y_data1_part3 = y_data1[2+part3_index[0][0]:]
    y_data2_part1 = y_data2[2:part2_index[0][0]]
    y_data2_part2 = y_data2[part2_index[0][0]:part3_index[0][0]]
    y_data2_part3 = y_data2[2+part3_index[0][0]:]
    
    mean11.append(np.mean(y_data1_part1))
    mean12.append(np.mean(y_data1_part2))
    mean13.append(np.mean(y_data1_part3))
    mean21.append(np.mean(y_data2_part1))
    mean22.append(np.mean(y_data2_part2))
    mean23.append(np.mean(y_data2_part3))
    x_data = {"empirique":x_data,
          }
print(mean12)
std12 = np.std(mean12)
print(std12)
mean_part1_y1 = np.mean(mean11)
mean_part2_y1 = np.mean(mean12)
mean_part3_y1 = np.mean(mean13)
mean_part1_y2= np.mean(mean21)
mean_part2_y2 = np.mean(mean22)
mean_part3_y2 = np.mean(mean23)
mean_up_value_y1 = np.mean(np.concatenate((mean11, mean13)))
std_up_value_y1 = np.std(np.concatenate((mean11, mean13)))
mean_down_value_y1 = np.mean(mean12)
std_down_value_y1 = np.std(mean12)
print(mean_part1_y1-mean_part2_y1, mean_up_value_y1, std_up_value_y1,mean_down_value_y1, std_down_value_y1)
part1y1means = np.full((334), fill_value=mean_part1_y1)
part2y1means = np.full((334), fill_value=mean_part2_y1)
part3y1means = np.full((334), fill_value=mean_part3_y1)
y1 = np.concatenate((part1y1means, part2y1means, part3y1means))
part1y2means = np.full((334), fill_value=mean_part1_y2)
part2y2means = np.full((334), fill_value=mean_part2_y2)
part3y2means = np.full((334), fill_value=mean_part3_y2)
y2 = np.concatenate((part1y2means, part2y2means, part3y2means))

x = np.linspace(0, 1, 1002)
x_data = {"empirique":x
          }
y_data = {
          "phototransistor signal": (y1,"empirique", "gray", "-", "full", 2.5),
          "input signal" :(y2 ,"empirique", "black", "-", "full", 2.5)
          
        }
Plotter("", "", x_data, y_data,
    x_axis_title="temps [s]", y_axis_title="Intensité relative [-]",name_file="tpop_bruit", fig_size=(10,6), 
    sub_font_size=16, ticks_font_size=12,step_yticks = 0.05,step_xticks = 0.2 , normalize=True,annotation= [["", (0.325, 0.995),(0.325, 0.937),11,{"facecolor":'black', "arrowstyle":"<->","linewidth":2}], [r"$\Delta$"+ "\u2248 0.05",(0, 0),(0.22, 0.95), 13]]) 

