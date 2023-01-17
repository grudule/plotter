import numpy as np
import matplotlib.pyplot as plt 
import random

class Plotter():
    def __init__(self,output,title, x_data, y_data,x_interval=None, saving_png = True, font_size = 18,step_yticks=10,step_xticks=0.2 ,**kwargs):
        """_summary_

        Args:
            output (_type_): ouput path where you want to save file
            x_data (array): data you want to plot in x-axis
            y_data (dict): dict with string keys corresponding to the name of the data and values are array/list of data
            x_interval (tuple): tuple of (x_min, x_max, sample number)
            saving_png (bool, optional): if you want to save png. Defaults to True.
            font_size (int): size of font you want
        kwargs : 
            x_axis_title
            y_axis_title
            step_xticks
            step_yticks
            thickness_line
        """
        self.step_yticks = step_yticks
        self.step_xticks = step_xticks
        self.title = title
        self.output = output
        if x_interval is not None : 
            self.x_data = np.linspace(x_interval[0], x_interval[1], x_interval[2])
        else : 
            self.x_data = x_data
        self.y_data = y_data
        self.fig, self.ax = plt.subplots(1, 1)
        self.font_size = font_size
        self.saving_png = saving_png
        for key in kwargs.keys():
            self.__setattr__(key, kwargs[key])
        self._font_changer()
        self._plotting()
    
    def _font_changer(self):
        font = {
            'weight' : 'normal',
            'size'   : self.font_size
            }

        plt.rc('font', **font)
        plt.clf()
    
    def _plotting(self):
        
        self.fig.set_tight_layout(True)
        line = 0
        y_max = 0
        y_min = 0
        for keys, values in self.y_data.items():
            if hasattr(self, "thickness_line"):
                plt.plot(self.x_data, values, linewidth=self.thickness_line,figure=self.fig, label=keys)
            else:
                plt.plot(self.x_data, values, figure=self.fig, label=keys)
            line += 1
            if y_max < np.amax(values):
                y_max = np.amax(values)
            if y_min > np.amin(values):
                y_min = np.amin(values)
        if line > 1:
            plt.legend()
        plt.title(self.title)
        plt.xticks(np.arange(np.amin(self.x_data), np.amax(self.x_data)+0.05*np.amax(self.x_data), step=self.step_xticks))
        plt.yticks(np.arange(y_min, y_max+0.05*y_max,step=self.step_xticks))
        plt.grid()
        self._change_axis()
        if self.saving_png : 
            self._save_png()
        plt.show()
    
    def _change_axis(self):
        if hasattr(self, "x_axis_title"):
            plt.xlabel(f'{self.x_axis_title}')
        if hasattr(self, "y_axis_title"):
            plt.ylabel(f'{self.y_axis_title}')

    def _save_png(self):
        number = random.randint(0,100)
        plt.savefig(self.output + f"graph{number}.pdf", dpi=1600)