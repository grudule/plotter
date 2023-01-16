import numpy as np
import matplotlib.pyplot as plt 
import random

class Plotter():
    def __init__(self,output,title, x_data, y_data,x_interval=None, saving_png = True, font_size = 18,**kwargs):
        """_summary_

        Args:
            output (_type_): ouput path where you want to save file
            x_data (_type_): data you want to plot in x-axis
            y_data (array/list: data you want to plot in y-axis
            x_interval (tuple): tuple of (x_min, x_max, sample number)
            saving_png (bool, optional): if you want to save png. Defaults to True.
            font_size (int): size of font you want
        kwargs : 
            x_axis_title
            y_axis_title
        """
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
            'family' : 'normal',
            'weight' : 'normal',
            'size'   : self.font_size
            }

        plt.rc('font', **font)
        plt.clf()
    
    def _plotting(self):
        
        self.fig.set_tight_layout(True)
        plt.plot(self.x_data, self.y_data, figure=self.fig)
        plt.title(self.title)
        self._change_axis()
        if self.saving_png : 
            self._save_png()
        plt.show()
    
    def _change_axis(self):
        if hasattr(self, "x_axis_title"):
            plt.xlabel(f'{self.x_axis_title}')
        if hasattr(self, "x_axis_title"):
            plt.xlabel(f'{self.x_axis_title}')
    
    def _save_png(self):
        number = random.randint(0,100)
        plt.savefig(self.output + f"graph{number}.png", dpi=1200)