import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm


class BasePlotly:
    def __init__(self, x_list, y_list, ci95p, ci95n,
                 fuzz_size, fuzz_n, color='#4286f4',
                 median_line=True, median_line_color='#000000', median_line_width=1,
                 layout={'showlegend': False}, figs=[], output="auto"):
        self.x_list = x_list
        self.y_list = y_list
        self.ci95p = ci95p
        self.ci95n = ci95n
        self.fuzz_size = fuzz_size
        self.fuzz_n = fuzz_n
        self.layout = layout
        self.figs = figs
        self.color = color
        self.median_line = median_line
        self.median_line_color = median_line_color
        self.median_line_width = median_line_width
        self.data = []

        # Automatically figures out if it's running in ipython. If not
        # Add default value of offline
        if output == 'auto':
            try:
                get_ipython()
                self.output = 'jupyter'
                from plotly.offline import init_notebook_mode, iplot
                import plotly.graph_objs as go
            except NameError:
                self.output = 'offline'
        else:
            self.output = output

    def hex_to_rgb(self, hex_color):
        color = hex_color.lstrip('#')
        rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
        return rgb_color

    def rgb_to_hex(self, rgb):
        hex_color = "".join([format(val, '02X') for val in rgb])
        return f"#{hex_color}"

    def rgb_to_rgba(self, rgb, opacity):
        """
        Takes rgb tuple and opacity between 0-1 and return rgba tuple.
        """
        color_rgba = rgb + (opacity,)
        return color_rgba

    def rgb_to_rgba_string(self, rgb, opacity):
        """
        Takes rgb tuple and opacity between 0-1 and return rgba tuple. Returns string version.
        """
        color_rgba = rgb + (opacity,)
        return f"rgba{color_rgba}"

    def rbga_to_rgb(self, rgba):
        """
        Takes in tuple of (red, green, blue, opacity).
        Assumes background colour is white.
        """
        BGColor = (255,255,255)

        r = ((1 - rgba[3]) * BGColor[0]) + (rgba[3] * rgba[0])
        g = ((1 - rgba[3]) * BGColor[1]) + (rgba[3] * rgba[1])
        b = ((1 - rgba[3]) * BGColor[2]) + (rgba[3] * rgba[2])
        rgb = (r,g,b)
        return rgb

    def calc_fuzz_area(self, upper, lower, fuzz_size):
        area = [((y1 - y2)*fuzz_size)/2 for (y1, y2) in zip(upper, lower)]
        return area

    def generate_y_line_data(self, upper, lower):
        """
        Creates shape of y values plotly can use. Helps to create shape. (Like square)
        """
        y_plotly_values = lower + list(reversed(upper))
        return y_plotly_values

    def generate_x_line_data(self):
        """
        Creates shape of x values plotly can use. Helps to create shape. (Like square)
        """
        return self.x_list + list(reversed(self.x_list))

    def generate_shape(self, upper, lower, config):
        """
        Takes lines from top and lines from bottom and creates shape. (Like square)
        :param upper: List of upper area
        :param lower: List of lower area
        :param config: User's config dict to modify
        :return: plotly scatter data structure
        """
        x_plotly_values = self.generate_x_line_data()
        y_plotly_values = self.generate_y_line_data(upper, lower)
        area = go.Scatter(
            x=x_plotly_values,
            y=y_plotly_values,
            mode='lines',
            # legendgroup='group 95%',
            # name='drawing shape',
            fill='tozeroy',
            fillcolor=config["color"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': config["color_edge"], 'width': 1,}
        )
        self.data.append(area)
        return area

    def plotly_plot(self):
        fig = go.Figure(data=self.data, layout=self.layout)

        if self.output == 'offline':
            plotly.offline.plot(fig, config={'displayModeBar': False},)
        if self.output == 'online':
            # Online plotly server version. Doesn't seem to be able to turn displayModeBar off.
            py.plot(fig, config={'displayModeBar': False})
        if self.output == 'jupyter':
            from plotly.offline import init_notebook_mode, plot, iplot
            init_notebook_mode(connected=True)
            iplot(fig, config={'displayModeBar': False})

    def create_data(self):
        pass

    def create_median(self):
        median = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(self.y_list, self.y_list),
            mode='lines',
            # legendgroup='group 95%',
            name='drawing shape',
            fill='tozeroy',
            fillcolor=self.median_line_color,
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': self.median_line_color, 'width': self.median_line_width,},
        )
        self.data.append(median)

    def plot(self):
        """
        Runs all internal logic to create and plot chart.
        """
        self.create_data()
        if self.median_line:
            self.create_median()
        if self.figs:
            self.data += self.figs
        self.plotly_plot()

    def export(self):
        """
        Runs all internal logic to create and returns plotly data structure.
        """
        self.create_data()
        if self.median_line:
            self.create_median()
        if self.figs:
            self.data += self.figs
        return self.data


class FuzzyPlotly(BasePlotly):
    def __init__(self, x_list, y_list,
                 ci95p, ci95n, ci60p, ci60n, ci30p, ci30n,
                 fuzz_size, fuzz_n,
                 color='#4286f4', median_line=True, median_line_color='#000000', median_line_width=1,
                 layout={'showlegend': False}, figs=[], output='auto'
                 ):
        super(FuzzyPlotly, self).__init__(x_list, y_list,
                                          ci95p, ci95n, ci60p, ci60n, ci30p, ci30n,
                                          fuzz_size, fuzz_n,
                                          # layout, figs,
                                          )
        self.x_list = x_list
        self.y_list = y_list
        self.ci95p = ci95p
        self.ci95n = ci95n
        self.ci60p = ci60p
        self.ci60n = ci60n
        self.ci30p = ci30p
        self.ci30n = ci30n
        self.fuzz_size = fuzz_size
        self.fuzz_n = fuzz_n
        self.layout = layout
        self.figs = figs
        self.color = color
        self.median_line = median_line
        self.median_line_color = median_line_color
        self.median_line_width = median_line_width
        self.data = []

        if output == 'auto':
            try:
                get_ipython()
                self.output = 'jupyter'
                from plotly.offline import init_notebook_mode, iplot
                import plotly.graph_objs as go
            except NameError:
                self.output = 'offline'
        else:
            self.output = output

    def create_color_opacity(self):
        """
        Calculates color opacity for set confidence intervals using normal distribution to match confidence intervals
        [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
        0.35, 0.65 is 30%
        0.2, 0.8 is 30% (60%-30%)
        0.025, 0.975 is 35% (95-30%-30%)
        """
        w_30 = norm.ppf(0.65, loc=0, scale=1) - norm.ppf(0.35, loc=0, scale=1)
        w_60 = norm.ppf(0.8, loc=0, scale=1) - norm.ppf(0.2, loc=0, scale=1) - w_30
        w_95 = norm.ppf(0.975, loc=0, scale=1) - norm.ppf(0.025, loc=0, scale=1) - w_60 - w_30

        # offset bump whole values down.
        gamma = 2
        color_offset = 0.05

        c_30 = 0.3 / w_30 - color_offset
        c_60 = 0.3 / w_60 - color_offset
        c_95 = 0.35 / w_95 - color_offset

        # factor used to scale to 1 as maximum value for opacity
        a = 1 / c_30

        c_30_final = (c_30 * a) ** gamma
        c_60_final = (c_60 * a) ** gamma
        c_95_final = (c_95 * a) ** gamma

        color_opacity = {
            'w_30': c_30_final,
            'w_60': c_60_final,
            'w_95': c_95_final,
        }
        return color_opacity

    # Using tween to ease start and end
    def calculate_fuzz_colors(self, color_a, color_b, fuzz_n, ease='ease-in'):
        """
        Calculated fuzz colors and return
        Optional easing function to smooth out and reduce colour banding issue.
        :param color_a: Starting colour.
        :param color_b: Ending colour.
        :param fuzz_n: Number of divisions (fuzz) to have.
        :param ease: ease-in, ease-out, ease-linear.
        :return: list of colors in RGB tuple
        """
        # ease = 'ease-linear' # WARNING FORCES LINEAR ON ALL!!!

        color_a_r, color_a_g, color_a_b = color_a
        color_b_r, color_b_g, color_b_b = color_b
        colors = []
        fuzz_n = int(fuzz_n)

        def ease_in_linear(t, b, c, d):
            return c*(t/d)*1+b

        def ease_in_cube(t, b, c, d):
            new = t/d
            t_at_pos = c*(t/d)*new*new+b
            return int(round(t_at_pos))

        def ease_out_cube(t, b, c, d):
            new = (t/d)-1
            t_at_pos = c*((new)*new*new + 1)+b
            return int(round(t_at_pos))

        def ease_in_quad(t, b, c, d):
            new = t/d
            t_at_pos = c*(t/d)*new+b
            return int(round(t_at_pos))

        def ease_out_quad(t, b, c, d):
            new = (t/d)
            t_at_pos = -c*((new)*(new-2))+b
            return int(round(t_at_pos))

        for i in range(fuzz_n):
            if ease == 'ease-in':
                color_new_r = ease_in_cube(t=i, b=color_a[0],
                                      c=abs(( - color_a_r + color_b_r)),
                                      d=fuzz_n)

                color_new_g = ease_in_cube(t=i, b=color_a[1],
                                           c=abs(( - color_a_g + color_b_g)),
                                           d=fuzz_n)

                color_new_b = ease_in_cube(t=i, b=color_a[2],
                                           c=abs(( - color_a_b + color_b_b)),
                                           d=fuzz_n)
            if ease == 'ease-out':
                color_new_r = ease_out_cube(t=i, b=color_a[0],
                                      c=abs(( - color_a_r + color_b_r)),
                                      d=fuzz_n)

                color_new_g = ease_out_cube(t=i, b=color_a[1],
                                           c=abs(( - color_a_g + color_b_g)),
                                           d=fuzz_n)

                color_new_b = ease_out_cube(t=i, b=color_a[2],
                                           c=abs(( - color_a_b + color_b_b)),
                                           d=fuzz_n)
            if ease == 'ease-linear':
                color_new_r = ease_in_linear(t=i, b=color_a[0],
                                            c=abs(( - color_a_r + color_b_r)),
                                            d=fuzz_n)

                color_new_g = ease_in_linear(t=i, b=color_a[1],
                                            c=abs(( - color_a_g + color_b_g)),
                                            d=fuzz_n)

                color_new_b = ease_in_linear(t=i, b=color_a[2],
                                            c=abs(( - color_a_b + color_b_b)),
                                            d=fuzz_n)

            color = (color_new_r, color_new_g, color_new_b)
            colors.append(color)
        return colors

    def create_fuzzy_shape(self, upper, lower, fuzz_size, fuzz_n, color_center, fuzz_colors_upper, fuzz_colors_lower):
        """
        # Finds fuzz for confidence interval with fuzz size and fuzz n.
        # Creates Upper fuzz shape, lower fuzz shape, and central area shape.
        """
        areas_upper = self.calc_fuzz_area(upper, lower, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_upper]

        # Create area with all the fuzz and by generating upper and lower of each line
        # Building from Top to bottom
        # Since it's drawn from up to down, need list of strongest color to weakest.
        for i in range(1, fuzz_n+1):
            # Upper fuzz
            # Building from top to bottom. Color is reversed. Going from last to first
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": f'rgb{fuzz_colors_upper[fuzz_n-i]}',
                                                             "color_edge": f'rgb{fuzz_colors_upper[fuzz_n-i]}'})
            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": f'rgb{fuzz_colors_lower[i-1]}',
                                                                 "color_edge": f'rgb{fuzz_colors_lower[i-1]}'})

        # Central Main shape
        fuzz_main_up_lower = [upper - area for (upper, area) in zip(upper, areas_upper)]
        fuzz_main_down_upper = [upper + area for (upper, area) in zip(lower, areas_upper)]
        self.generate_shape(fuzz_main_up_lower, fuzz_main_down_upper, color_center)

    def create_data(self, color_plot=False):
        """
        Main function which glues all the internal parts after working out interal logic values required.
        Views one central band and creates banding on top and bottom.
        Since one complete fuzz will happen between two band it workout and mid points for colour.
        :param color_plot: True or False. If true, displays r values of color chart in matplotlib for verification.

        """
        color_opacity = self.create_color_opacity()
        color_rgb = self.hex_to_rgb(self.color)

        # 3 center colours + 2 in-between
        color_rgba_w95 = self.rgb_to_rgba(color_rgb, color_opacity['w_95'])
        color_rgba_w60 = self.rgb_to_rgba(color_rgb, color_opacity['w_60'])
        color_rgba_w30 = self.rgb_to_rgba(color_rgb, color_opacity['w_30'])

        color_rgb_w95 = self.rbga_to_rgb(color_rgba_w95)
        color_rgb_w60 = self.rbga_to_rgb(color_rgba_w60)
        color_rgb_w30 = self.rbga_to_rgb(color_rgba_w30)

        # assumes max is white, fading to white. Background is white.
        colors_w95_w100 = self.calculate_fuzz_colors(
            color_rgb_w95,
            (255, 255, 255),
            self.fuzz_n,
            'ease-in',
        )

        # Find mid point between two bands
        color_w30_mid_w60 = ((color_rgb_w30[0] + color_rgb_w60[0]) / 2,
                             (color_rgb_w30[1] + color_rgb_w60[1]) / 2,
                             (color_rgb_w30[2] + color_rgb_w60[2]) / 2,
                             )

        # Find upper
        colors_w30_mid = self.calculate_fuzz_colors(
            color_rgb_w30,
            color_w30_mid_w60,
            self.fuzz_n,
            'ease-in',
        )

        # Find lower
        colors_mid_w60 = self.calculate_fuzz_colors(
            color_w30_mid_w60,
            color_rgb_w60,
            self.fuzz_n,
            'ease-out',
        )

        # Find mid point
        color_w60_mid_w95 = ((color_rgb_w95[0] + color_rgb_w60[0]) / 2,
                             (color_rgb_w95[1] + color_rgb_w60[1]) / 2,
                             (color_rgb_w95[2] + color_rgb_w60[2]) / 2,
                             )

        # Find upper
        colors_w60_mid = self.calculate_fuzz_colors(
            color_rgb_w60,
            color_w60_mid_w95,
            self.fuzz_n,
            'ease-in',
            )

        # Find lower
        colors_mid_w95 = self.calculate_fuzz_colors(
            color_w60_mid_w95,
            color_rgb_w95,
            self.fuzz_n,
            'ease-out',
            )

        # Top part confidence interval colors are reverse of bottom colors. Like mirror image.
        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci60p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w95}', "color_edge": f'rgb{color_rgb_w95}'},
            fuzz_colors_upper=colors_w95_w100, fuzz_colors_lower=colors_mid_w95,
        )
        self.create_fuzzy_shape(
            upper=self.ci60p, lower=self.ci30p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w60}', "color_edge": f'rgb{color_rgb_w60}'},
            fuzz_colors_upper=colors_w60_mid, fuzz_colors_lower=colors_mid_w60,
        )
        self.create_fuzzy_shape(
            upper=self.ci30p, lower=self.ci30n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w30}', "color_edge": f'rgb{color_rgb_w30}'},
            fuzz_colors_upper=colors_w30_mid, fuzz_colors_lower=list(reversed(colors_w30_mid)),
        )
        self.create_fuzzy_shape(
            upper=self.ci30n, lower=self.ci60n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w60}', "color_edge": f'rgb{color_rgb_w60}'},
            fuzz_colors_upper=list(reversed(colors_mid_w60)), fuzz_colors_lower=list(reversed(colors_w60_mid)),
        )
        self.create_fuzzy_shape(
            upper=self.ci60n, lower=self.ci95n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w95}', "color_edge": f'rgb{color_rgb_w95}'},
            fuzz_colors_upper=list(reversed(colors_mid_w95)), fuzz_colors_lower=list(reversed(colors_w95_w100)),
        )

        if color_plot:
            import matplotlib.pyplot as plt
            import numpy as np

            # Colour list is up to down inside of function. To match internal logic colour list needs to reverse.
            # In another words last value is the color list is most outter part on the top. So reverse.
            # Down to up. So color list is same direction.
            # However to draw graph I want to see last value first as that's most outter again. So reverse again.
            y_plot_vals_r = []
            colors_w95_w100_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w95_w100))]
            colors_mid_w95_r_p_vals = [255-rgb[0] for rgb in list(reversed(colors_mid_w95))]

            colors_w60_mid_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w60_mid))]
            colors_mid_w60_r_p_vals = [255-rgb[0] for rgb in list(reversed(colors_mid_w60))]

            colors_w30_mid_top_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w30_mid))]
            colors_w30_mid_bot_r_vals = [255-rgb[0] for rgb in list((colors_w30_mid))]

            y_plot_vals_r = y_plot_vals_r + \
                            colors_w95_w100_r_vals + colors_mid_w95_r_p_vals + \
                            colors_w60_mid_r_vals + colors_mid_w60_r_p_vals + \
                            colors_w30_mid_top_r_vals + colors_w30_mid_bot_r_vals + \
                            list(reversed(colors_mid_w60_r_p_vals)) + list(reversed(colors_w60_mid_r_vals)) + \
                            list(reversed(colors_mid_w95_r_p_vals)) + list(reversed(colors_w95_w100_r_vals))

            plt.bar(np.arange(len(y_plot_vals_r)), y_plot_vals_r, width=1)
            plt.show()


# For full fuzz
class DensPlotly(BasePlotly):
    def __init__(self, x_list, y_list, ci95p, ci95n,
                 fuzz_n, color='#4286f4',
                 median_line=True, median_line_color='#000000', median_line_width=1,
                 layout={'showlegend': False}, figs=[], output='auto'):
        fuzz_size = 1
        super(DensPlotly, self).__init__(x_list, y_list, ci95p, ci95n, fuzz_size, fuzz_n)
        self.x_list = x_list
        self.y_list = y_list
        self.ci95p = ci95p
        self.ci95n = ci95n
        self.fuzz_size = fuzz_size
        self.fuzz_n = fuzz_n
        self.layout = layout
        self.figs = figs
        self.color = color
        self.median_line = median_line
        self.median_line_color = median_line_color
        self.median_line_width = median_line_width
        self.data = []

        if output == 'auto':
            try:
                get_ipython()
                self.output = 'jupyter'
                from plotly.offline import init_notebook_mode, iplot
                import plotly.graph_objs as go
            except NameError:
                self.output = 'offline'
        else:
            self.output = output

    def generate_interval_point(self, p, center, std):
        """
        probability is between 0-1
        example p = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
        """
        point = [p]
        boundary_point = norm.ppf(point, loc=center, scale=std)
        return boundary_point[0]

    def calc_colour(self, upper_ci, lower_ci, per):
        """
        Takes in user's input colour and calculates ci colours
        """
        h_ci = norm.ppf(upper_ci, loc=0, scale=1) - norm.ppf(lower_ci, loc=0, scale=1)
        w_ci = per / h_ci
        return w_ci

    def normalize_data(self, val, val_max, val_min):
        return (val - val_min) / (val_max - val_min)

    def calculate_fuzz_color_normal(self, fuzz_n):
        """
        Assume it's standard normal distribution with loc=0, scale=1 (mean=0, std=1)
        Normalizes opacity from 0 to 1.
        :param fuzz_n:
        :return:
        """
        w95 = 1.959964
        step = w95 / fuzz_n

        color = self.hex_to_rgb(self.color)
        r_color, g_color, b_color = color

        colors = []

        # Normalization part so opacity goes from 0 to 1
        norm_max = norm.pdf(0)
        norm_min = norm.pdf(w95)

        # Going from 0 to 95%. 0 is highest and 95% is lowest.
        for i in range(fuzz_n):
            # This is using normalized so 0 to 1 now
            opacity = self.normalize_data(val=norm.pdf(i * step), val_max=norm_max, val_min=norm_min)

            color_rgba = (r_color, g_color, b_color, opacity)
            color_rgb = self.rbga_to_rgb(color_rgba)

            colors.append(color_rgb)
        return colors

    # Finds fuzz for confidence interval with fuzz size and fuzz n.
    def create_fuzzy_shape(self, upper, lower, fuzz_size, fuzz_n, fuzz_colors):
        areas_upper = self.calc_fuzz_area(upper, lower, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_upper]

        for i in range(1, fuzz_n+1):
            # Upper fuzz
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": f'rgb{fuzz_colors[fuzz_n-i]}',
                                                             "color_edge": f'rgb{fuzz_colors[fuzz_n-i]}'})

            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": f'rgb{fuzz_colors[fuzz_n-i]}',
                                                                 "color_edge": f'rgb{fuzz_colors[fuzz_n-i]}'})

    def create_data(self):
        colors_center_rgb_w95 = self.calculate_fuzz_color_normal(self.fuzz_n)

        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci95n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            fuzz_colors=colors_center_rgb_w95,
        )


class StandardErrorPlot(BasePlotly):
    def __init__(self, *args, **kwargs):
        kwargs['fuzz_size'] = 1
        kwargs['fuzz_n'] = 1
        super(StandardErrorPlot, self).__init__(*args, **kwargs)

    # Finds fuzz for confidence interval with fuzz size and fuzz n.
    def create_fuzzy_shape(self, upper, lower, fuzz_size, fuzz_n):
        areas_upper = self.calc_fuzz_area(upper, lower, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_upper]

        for i in range(1, fuzz_n+1):
            # Upper fuzz
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": self.color, "color_edge": self.color})

            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": self.color, "color_edge": self.color})

    def create_data(self):

        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci95n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
        )


class FanPlotly(FuzzyPlotly):
    def __init__(self, *args, **kwargs):
        kwargs['fuzz_size'] = 0
        kwargs['fuzz_n'] = 1
        super(FanPlotly, self).__init__(*args, **kwargs)
