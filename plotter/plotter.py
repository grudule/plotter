import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


class Plotter():
    def __init__(self, output_path, title, x_data, y_data, saving_png=True, name_file=None,
                 title_font_size=18, sub_font_size=16, ticks_font_size = 10, 
                 normalize = False,
                 **kwargs):
        """Class Plotter automaticaly plot and save the png. Most of commun options are customizable (font size, title, axis name, etc...). 

        Args:
            output_path (str): ouput path where you want to save file
            title (str): name of your figure
            x_data (array/tuple): data you want to plot in x-axis, array of all x, or a tuple (x_min,x_max,number of element)
            y_data (dict): dict with string keys values are (data[np.array],color[str],type_of_line[str],fill_style[str], thickness_line/markers[float] (optional)) all values in str.
            Possible style for plot : https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
            Possible markers for scatter : https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
            Possible fillstyle : https://matplotlib.org/3.2.2/gallery/lines_bars_and_markers/marker_fillstyle_reference.html
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
            annotation (list of list): [["text", xy:(tuple), xytext:(tuple), arrow(dict)], [["text2", xy:(tuple), xytext:(tuple), fontsize(int), arrow(dict)]]] 
            vline (dict): {first_vline : (x_data(int), ymin, ymax, colors(str), linewidth(float), linestyle(str))}
            no_legend (bool):
        """

        self.title = title
        self.output_path = output_path
        self.x_data = x_data
        self.y_data = y_data
        self.saving_png = saving_png
        self.name_file = name_file
        self.ticks_font_size = ticks_font_size
        self.title_font = {
            'weight': 'normal',
            'size': title_font_size
        }
        self.sub_font = {
            'weight': 'normal',
            'size': sub_font_size
        }
        self.normalize = normalize
        for key in kwargs.keys():
            self.__setattr__(key, kwargs[key])
        if hasattr(self, "fig_size"):
            self.fig, self.ax = plt.subplots(figsize=self.fig_size)
        else:
            self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self._plotting()

    def _plotting(self):
        self.fig.set_tight_layout(True)
        line = 0
        line_style = ["", "-", "--", "-.", ":", ".", ","]
        for keys, values in self.y_data.items():
            # Verify for thickness_line and plot with the corresponding y_data and parameters
            try:
                if values[3] not in line_style:
                    plt.plot(self.x_data[values[1]], values[0], f"{values[3]}",
                             figure=self.fig, color=values[2], label=keys, fillstyle=values[4], markersize=values[5])
                else:
                    plt.plot(self.x_data[values[1]], values[0], f"{values[3]}",
                             figure=self.fig, color=values[2], label=keys, fillstyle=values[4], linewidth=values[5])
            except Exception:
                plt.plot(self.x_data[values[1]], values[0], f"{values[3]}",
                         figure=self.fig, color=values[2], label=keys, fillstyle=values[4])
            line += 1
        if hasattr(self, "vline"):
            for i, v in self.vline.items():
                plt.vlines(x=v[0],
                           ymin=v[1],
                           ymax=v[2],
                           colors=v[3],
                           linewidth=v[4],
                           linestyles=v[5]
                           )
        if hasattr(self, "annotation"):
            for i in range(len(self.annotation)):
                try:
                    plt.annotate(self.annotation[i][0],xy =self.annotation[i][1], xytext = self.annotation[i][2], fontsize = self.annotation[i][3],
                        arrowprops = self.annotation[i][4])
                except IndexError :
                    try : 
                        plt.annotate(self.annotation[i][0],xy =self.annotation[i][1], xytext = self.annotation[i][2],fontsize= self.annotation[i][3])
                    except IndexError : 
                        print("there is too few arguments in annotation verify the documentation")
        if line > 1:
            if hasattr(self, "no_legend"):
                pass
            else:
                plt.legend(loc='lower right')

        plt.title(self.title, **self.title_font)
        self._change_axis()
        if self.normalize: 
            plt.xlim(left=0)  # adjust the right leaving left unchanged
            plt.ylim(bottom=0)
        if self.saving_png:
            self._save_png()
        plt.show()

    def _change_axis(self):
        plt.xticks(fontsize=self.ticks_font_size)
        plt.yticks(fontsize=self.ticks_font_size)
        if hasattr(self, "x_axis_title"):
            plt.xlabel(f'{self.x_axis_title}', **self.sub_font)

        if hasattr(self, "y_axis_title"):
            plt.ylabel(f'{self.y_axis_title}', **self.sub_font)

        if hasattr(self, "step_xticks"):
            self.ax.xaxis.set_major_locator(MultipleLocator(
                self.step_xticks))  # Intervals for major x-ticks
            # Minor ticks : Automatic filling based on the ytick range
            self.ax.xaxis.set_minor_locator(AutoMinorLocator())
            self.ax.tick_params(axis="x", direction='in', length=4, width=1,
                                grid_color='b', grid_alpha=0.5, which="minor")

        if hasattr(self, "step_yticks"):
            self.ax.yaxis.set_major_locator(
                MultipleLocator(self.step_yticks))  # For y-ticks
            self.ax.yaxis.set_minor_locator(AutoMinorLocator())
            self.ax.tick_params(axis="y", direction='in', length=4, width=1,
                                grid_color='b', grid_alpha=0.5, which="minor")

        self.ax.tick_params(direction='in', length=6, width=1.5,
                            grid_color='black', grid_alpha=0.5)

    def _save_png(self):
        if self.name_file is not None:
            plt.savefig(self.output_path + f"{self.name_file}.png", dpi=600)
        else:
            number = random.randint(0, 100)
            plt.savefig(self.output_path + f"graph{number}.png", dpi=600)
