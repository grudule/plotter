import numpy as np
import matplotlib.pyplot as plt
import random


class Plotter():
    def __init__(self, output_path, title, x_data, y_data, saving_png=True,name_file=None, title_font_size=18,sub_font_size=16,**kwargs):
        """Class Plotter automaticaly plot and save the png. Most of commun options are customizable (font size, title, axis name, etc...). 

        Args:
            output_path (str): ouput path where you want to save file
            title (str): name of your figure
            x_data (array/tuple): data you want to plot in x-axis, array of all x, or a tuple (x_min,x_max,number of element)
            y_data (dict): dict with string keys corresponding to the name of the data and values are array/list of data
            saving_png (bool, optional): if you want to save png. Defaults to True.
            name_file (bool, optional): name you want to save your file. Defaults to 
            title_font_size (int, optional):size for title font size. Defaults to 18.
            sub_font_size (int, optional):size for axis font size. Defaults to 18.

        kwargs : 
            x_axis_title (str): x axis title
            y_axis_title (str): y axis title
            step_xticks (float): step in x ticks 
            step_yticks (flaot): step in y ticks 
            thickness_line (float): thickness of the line
            fig_size (tuple) : (length, width). Defaults (10,8)
        """
        self.title = title 
        self.output_path = output_path
        if isinstance(x_data, tuple):
            self.x_data = np.linspace(x_data[0], x_data[1], x_data[2])
        else:
            self.x_data = x_data
        self.y_data = y_data
        self.saving_png = saving_png
        self.name_file = name_file
        self.title_font = {
            'weight': 'normal',
            'size': title_font_size
        }
        self.sub_font = {
            'weight': 'normal',
            'size': sub_font_size
        }
        for key in kwargs.keys():
            self.__setattr__(key, kwargs[key])
        if hasattr(self, "fig_size"):
            self.fig, self.ax = plt.subplots(1, 1, figsize=self.fig_size)
        else:
            self.fig, self.ax = plt.subplots(1, 1, figsize=(10, 8))
        self._font_changer()
        self._plotting()

    def _font_changer(self):
        plt.clf()

    def _plotting(self):

        self.fig.set_tight_layout(True)
        line = 0
        y_max = 0
        y_min = 0
        for keys, values in self.y_data.items():
            if hasattr(self, "thickness_line"):
                plt.plot(self.x_data, values, linewidth=self.thickness_line,
                         figure=self.fig, label=keys)
            else:
                plt.plot(self.x_data, values, figure=self.fig, label=keys)
            line += 1
            if y_max < np.amax(values):
                y_max = np.amax(values)
            if y_min > np.amin(values):
                y_min = np.amin(values)
        if line > 1:
            plt.legend()
        plt.title(self.title, **self.title_font)
        if hasattr(self, "step_xticks"):
            plt.xticks(np.arange(np.amin(self.x_data), np.amax(
                self.x_data)+0.02*np.amax(self.x_data), step=self.step_xticks))
        if hasattr(self, "step_yticks"):
            plt.yticks(np.arange(y_min, y_max+0.02 *
                       y_max, step=self.step_yticks))
        self._change_axis()
        if self.saving_png:
            self._save_png()
        plt.show()

    def _change_axis(self):
        if hasattr(self, "x_axis_title"):
            plt.xlabel(f'{self.x_axis_title}', **self.sub_font)
        if hasattr(self, "y_axis_title"):
            plt.ylabel(f'{self.y_axis_title}', **self.sub_font)

    def _save_png(self):
        if self.name_file is not None:
            plt.savefig(self.output_path + f"{self.name_file}.png", dpi=600)
        else:
            number = random.randint(0, 100)
            plt.savefig(self.output_path + f"graph{number}.png", dpi=600)
