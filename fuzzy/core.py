import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm

import matplotlib.pyplot as plt
import numpy as np


class FuzzyPlotly:
    def __init__(self, x_list, y_list,
                 ci95p, ci95n, ci60p, ci60n, ci30p, ci30n,
                 fuzz_size, fuzz_n,
                 color='#4286f4', layout={}, figs=[], output='auto'):
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

        c_30 = 0.3 / w_30 - 0.05
        c_60 = 0.3 / w_60 - 0.05
        c_95 = 0.35 / w_95 - 0.05

        # factor used to scale to 1 as maximum value for opacity
        a = 1 / c_30

        gamma = 2.5

        c_30_final = (c_30 * a) ** gamma
        c_60_final = (c_60 * a) ** gamma
        c_95_final = (c_95 * a) ** gamma

        color_opacity = {
            'w_30': c_30_final,
            'w_60': c_60_final,
            'w_95': c_95_final,
        }

        print(f'w_30: {w_30} w_60: {w_60} w_95: {w_95} ')
        print(f'c_30: {c_30} c_60: {c_60} c_95: {c_95} ')
        print('final color_opacity')
        print(color_opacity)

        # color_opacity = {
        #     'w_30': 1,
        #     'w_60': 0.42,
        #     'w_95': 0.2,
        # }
        return color_opacity

    def rgb_to_rgba(self, rgb, opacity):
        '''
        Takes rgb tuple and opacity between 0-1 and return rgba tuple.
        :param rgb:
        :param opacity:
        :return:
        '''
        color_rgba = rgb + (opacity,)
        return color_rgba

    def rgb_to_rgba_string(self, rgb, opacity):
        '''
        Takes rgb tuple and opacity between 0-1 and return rgba tuple.
        :param rgb:
        :param opacity:
        :return:
        '''
        color_rgba = rgb + (opacity,)
        return f"rgba{color_rgba}"

    def rbga_to_rgb(self, rgba):
        '''
        Takes in tuple of (255,255,255,1)
        :param rgba:
        :return:
        '''

        # Background color. Assumes it's white.
        BGColor = (255,255,255)

        r = ((1 - rgba[3]) * BGColor[0]) + (rgba[3] * rgba[0])
        g = ((1 - rgba[3]) * BGColor[1]) + (rgba[3] * rgba[1])
        b = ((1 - rgba[3]) * BGColor[2]) + (rgba[3] * rgba[2])
        rgb = (r,g,b)
        # print(rgb)
        return rgb

    # # Finds color between two colors using gradient
    # # takes rgb only.?
    # # go from low color to high
    # def calculate_fuzz_colors(self, color_a, color_b, fuzz_n):
    #     color_a_r, color_a_g, color_a_b = color_a
    #     color_b_r, color_b_g, color_b_b = color_b
    #     colors = []
    #     fuzz_n = int(fuzz_n)
    #     # print(f'color_a: {color_a}')
    #     # print(f'color_b: {color_b}')
    #     r_step = abs(( - color_a_r + color_b_r))/fuzz_n
    #     g_step = abs(( - color_a_g + color_b_g))/fuzz_n
    #     b_step = abs(( - color_a_b + color_b_b))/fuzz_n
    #
    #     # print(f'color_a_r: {color_a_r}')
    #     # print(f'color_b_r: {color_b_r}')
    #     # print(f'self.fuzz_n: {self.fuzz_n}')
    #     # print(f'r_step: {r_step}')
    #     # print(f'r_step: {r_step}')
    #
    #     for i in range(fuzz_n):
    #         color = ((color_a_r + i*r_step), (color_a_g + i*g_step), (color_a_b + i*b_step), )
    #
    #         # print(f'i: {i}')
    #         # print(f'r_step: {r_step}')
    #         # print(f'color_a_r: {color_a_r}')
    #         # color = color_a_r + (i*r_step)
    #         colors.append(color)
    #
    #         # print(color)
    #         # print('===')
    #     # print(colors[0])
    #     # print(colors[-1])
    #     # print('')
    #     return colors

    # Using tween to ease start and end
    def calculate_fuzz_colors(self, color_a, color_b, fuzz_n, ease='ease-in'):

        # ease = 'ease-linear' # WARNING FORCES LINEAR ON ALL!!!

        color_a_r, color_a_g, color_a_b = color_a
        color_b_r, color_b_g, color_b_b = color_b
        colors = []
        fuzz_n = int(fuzz_n)
        print(f'color_a: {color_a}')
        print(f'color_b: {color_b}')
        print(f'ease is {ease}')

        # r_step = abs(( - color_a_r + color_b_r))/fuzz_n
        # g_step = abs(( - color_a_g + color_b_g))/fuzz_n
        # b_step = abs(( - color_a_b + color_b_b))/fuzz_n
        #
        # print(f'color_a_r: {color_a_r}')
        # print(f'color_b_r: {color_b_r}')
        # print(f'self.fuzz_n: {self.fuzz_n}')
        # print(f'r_step: {r_step}')
        # print(f'r_step: {r_step}')

        # t = current strip (i in loop)
        # d = total size of strip
        # b = beginning value (0=start from 0?)
        # c = .? (lets try 1)

        # Linear. Same as what I was doing before.
        def ease_in_linear(t, b, c, d):
            # print(f'{c}*({t}/{d})*{1}+{b} = {c*(t/d)*1+b}')
            return c*(t/d)*1+b

        def ease_in_cube(t, b, c, d):
            # print(f'{c}*({t}/{d})*{t}+{b} = {c*(t/d)*t+b}')

            new = t/d
            t_at_pos = c*(t/d)*new*new+b
            # print(int(round(t_at_pos)))
            return int(round(t_at_pos))
            # return int(111)

        def ease_out_cube(t, b, c, d):
            # print(f'{c}*({t}/{d})*{t}+{b} = {c*(t/d)*t+b}')

            new = (t/d)-1
            t_at_pos = c*((new)*new*new + 1)+b
            # print(int(round(t_at_pos)))
            return int(round(t_at_pos))

        def ease_in_quad(t, b, c, d):
            # print(f'{c}*({t}/{d})*{t}+{b} = {c*(t/d)*t+b}')

            new = t/d
            t_at_pos = c*(t/d)*new+b
            # print(int(round(t_at_pos)))
            return int(round(t_at_pos))
            # return int(111)

        def ease_out_quad(t, b, c, d):
            # print(f'{c}*({t}/{d})*{t}+{b} = {c*(t/d)*t+b}')

            new = (t/d)
            t_at_pos = -c*((new)*(new-2))+b
            # print(int(round(t_at_pos)))
            return int(round(t_at_pos))

        for i in range(fuzz_n):
            if ease == 'ease-in':
                color_new_r = ease_in_cube(t=i, b=color_a[0],
                                      c=abs(( - color_a_r + color_b_r)),
                                      d=fuzz_n)
                # print('=ease_1=' + str(i))
                # print(color_new_r)

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
                # print('=ease_1=' + str(i))
                # print(color_new_r)

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
                # print('=ease_1=' + str(i))

                color_new_g = ease_in_linear(t=i, b=color_a[1],
                                            c=abs(( - color_a_g + color_b_g)),
                                            d=fuzz_n)

                color_new_b = ease_in_linear(t=i, b=color_a[2],
                                            c=abs(( - color_a_b + color_b_b)),
                                            d=fuzz_n)

            color = (color_new_r, color_new_g, color_new_b)

            # print(color_a_r + i*

            # print(f'i: {i}')
            # print(f'r_step: {r_step}')
            # print(f'color_a_r: {color_a_r}')
            # color = color_a_r + (i*r_step)
            colors.append(color)

            # print(color)
            # print('===')
        # print(colors[0])
        # print(colors[-1])
        print('')
        return colors

    def calc_fuzz_area(self, upper, lower, fuzz_size):
        # area_diff = upper - lower
        area = [((y1 - y2)*fuzz_size)/2 for (y1, y2) in zip(upper, lower)]
        return area

    # Gives output Plotly can use
    def generate_y_line_data(self, upper, lower):
        """
        Creates shape of y values y plotly can use.
        """
        y_plotly_values = lower + list(reversed(upper))
        return y_plotly_values

    # Note: Always same for this chart. Could add in config in plotly for labels later.
    def generate_x_line_data(self):
        return self.x_list + list(reversed(self.x_list))

    def generate_shape(self, upper, lower, config):
        x_plotly_values = self.generate_x_line_data()
        y_plotly_values = self.generate_y_line_data(upper, lower)
        # print("Config at generate_shape")
        # print(config)
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

    # Finds fuzz for confidence interval with fuzz size and fuzz n.
    def create_fuzzy_shape(self, upper, lower, fuzz_size, fuzz_n, color_center, fuzz_colors_upper, fuzz_colors_lower):
        areas_upper = self.calc_fuzz_area(upper, lower, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_upper]
        # print(areas_p_95)
        # print(area_per_fuzz)


        # Create area with all the fuzz and by generating upper and lower of each line
        # Building from Top to bottom

        # color_opacity = self.create_color_opacity()
        # color_rgb = self.hex_to_rgb(self.color)
        # color_rgba = self.rgb_to_rgba(color_rgb, color_opacity['w_95'])
        # color_rgb_re = self.rbga_to_rgb(color_rgba)
        # print(color_rgb_re)
        # config_re = {"color": f'rgb{color_rgba}'}
        #
        # colors = self.calculate_fuzz_colors(
        #     self.rbga_to_rgb(self.rgb_to_rgba(color_rgb, color_opacity['w_60'])),
        #     self.rbga_to_rgb(color_rgba))
        # print(colors)

        # Since it's drawn from up to down, need list of strongest color to weakest.
        # print(fuzz_n)
        for i in range(1, fuzz_n+1):
            # print(f'i :{i}')
            # print(f'fuzz_n :{fuzz_n}')
            # print(f'len(fuzz_colors_upper) :{len(fuzz_colors_upper)}')
            # Upper fuzz
            # Building from top to bottom.
            # Color is reversed. Going from last to first
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": f'rgb{fuzz_colors_upper[fuzz_n-i]}', "color_edge": f'rgb{fuzz_colors_upper[fuzz_n-i]}'})
            # print('cur_up_upper')
            # print('cur_up_lower')
            # print(cur_up_upper)
            # print(cur_up_lower)

            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": f'rgb{fuzz_colors_lower[i-1]}', "color_edge": f'rgb{fuzz_colors_lower[i-1]}'})

            # print('cur_down_upper')
            # print('cur_down_lower')
            # print(cur_down_upper)
            # print(cur_down_lower)


        # Central Main shape
        fuzz_main_up_lower = [upper - area for (upper, area) in zip(upper, areas_upper)]
        fuzz_main_down_upper = [upper + area for (upper, area) in zip(lower, areas_upper)]
        self.generate_shape(fuzz_main_up_lower, fuzz_main_down_upper, color_center)

    def create_data(self):
        color_opacity = self.create_color_opacity()
        color_rgb = self.hex_to_rgb(self.color)

        # 3 center colours + 2 in-between
        color_rgba_w95 = self.rgb_to_rgba(color_rgb, color_opacity['w_95'])
        color_rgba_w60 = self.rgb_to_rgba(color_rgb, color_opacity['w_60'])
        color_rgba_w30 = self.rgb_to_rgba(color_rgb, color_opacity['w_30'])

        color_rgb_w95 = self.rbga_to_rgb(color_rgba_w95)
        color_rgb_w60 = self.rbga_to_rgb(color_rgba_w60)
        color_rgb_w30 = self.rbga_to_rgb(color_rgba_w30)

        # colors_w30_w60 = self.calculate_fuzz_colors(
        #     color_rgb_w30,
        #     color_rgb_w60,
        #     self.fuzz_n,
        # )
        # colors_w60_w95 = self.calculate_fuzz_colors(
        #     color_rgb_w60,
        #     color_rgb_w95,
        #     self.fuzz_n,
        # )
        # # assumes max is white?
        colors_w95_w100 = self.calculate_fuzz_colors(
            color_rgb_w95,
            (255, 255, 255),
            self.fuzz_n,
            'ease-in',
        )
        #
        # Find mid point

        # Giving incorrect mid point!!!
        # color_w30_mid_w60 = self.calculate_fuzz_colors(
        #     color_rgb_w30,
        #     color_rgb_w60,
        #     self.fuzz_n,
        # )[int(self.fuzz_n/2)]

        color_w30_mid_w60 = ((color_rgb_w30[0]+color_rgb_w60[0])/2,
                             (color_rgb_w30[1]+color_rgb_w60[1])/2,
                             (color_rgb_w30[2]+color_rgb_w60[2])/2,
                             )

        # # TODO: Testing code here
        print('color_rgb_w30')
        print(color_rgb_w30)

        print('color_w30_mid_w60')
        print(color_w30_mid_w60)

        print('color_rgb_w60')
        print(color_rgb_w60)


        # Find upper
        # color_w30_mid_w60 = (255,255,255) # Testing to see if I see visual difference
        colors_w30_mid = self.calculate_fuzz_colors(
            color_rgb_w30,
            color_w30_mid_w60,
            self.fuzz_n,
            'ease-in',
        )
        # print('color_rgb_w30')
        # print(color_rgb_w30)
        # print('color_w30_mid_w60')
        # print(color_w30_mid_w60)

        # Find lower
        colors_mid_w60 = self.calculate_fuzz_colors(
            color_w30_mid_w60,
            color_rgb_w60,
            self.fuzz_n,
            'ease-out',
        )
        # # print(color_w30_mid_w60)
        # # print(colors_w30_mid)
        # print('color_mid_w60')
        # print(colors_mid_w60)
        # # print(colors_w30_w60)

        # Find mid point
        # color_w60_mid_w95 = self.calculate_fuzz_colors(
        #     color_rgb_w60,
        #     color_rgb_w95,
        #     self.fuzz_n,
        # )[int(self.fuzz_n/2)]

        color_w60_mid_w95 = ((color_rgb_w95[0]+color_rgb_w60[0])/2,
                             (color_rgb_w95[1]+color_rgb_w60[1])/2,
                             (color_rgb_w95[2]+color_rgb_w60[2])/2,
                             )

        print('==color_rgb_w95==')
        print(color_rgb_w95)

        print('color_w60_mid_w95')
        print(color_w60_mid_w95)

        print('color_rgb_w60')
        print(color_rgb_w60)

        # Find upper
        colors_w60_mid = self.calculate_fuzz_colors(
            color_rgb_w60,
            color_w60_mid_w95,
            self.fuzz_n,
            'ease-in',
            )
        # print("colors_w60_mid")
        # print(colors_w60_mid)

        # Find lower
        colors_mid_w95 = self.calculate_fuzz_colors(
            color_w60_mid_w95,
            color_rgb_w95,
            self.fuzz_n,
            'ease-out',
            )

        # TODO: TEMP OVERRIDE OF CENTRAL COLOURS JUST TO SEE!!!
        # color_rgb_w95 = (255.0, 196.51278306108654, 196.51278306108654)
        # color_rgb_w30 = (255.0, 125, 0)
        # color_rgb_w60 = (255.0, 125, 0)
        # color_rgb_w95 = (255.0, 125, 0)

        # Another darker color
        # color_rgb_w30 = (178, 34, 34)
        # color_rgb_w60 = (178, 34/2, 34/2)
        # color_rgb_w95 = (178, 34/4, 34/4)

        # color_rgb_w95 = color_rgb_w60
        # color_rgb_w60 = color_rgb_w30
        # color_rgb_w30 = (125, 125, 124)

        # Top part confidence interval colors are reverse of bottom colors. Like mirror image.
        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci60p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w95}', "color_edge": f'rgb{color_rgb_w95}'},
            fuzz_colors_upper=colors_w95_w100, fuzz_colors_lower=list((colors_mid_w95)),
        )
        self.create_fuzzy_shape(
            upper=self.ci60p, lower=self.ci30p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w60}', "color_edge": f'rgb{color_rgb_w60}'},
            fuzz_colors_upper=colors_w60_mid, fuzz_colors_lower=list((colors_mid_w60)),
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

        # Up to down. So color list is up to down inside of function. To copy what it's doing I need to reverse.
        # In another words last value is the color list is most outter part on the top. So reverse.
        #
        # Down to up. So color list is same direction. However to draw graph I want to see last value first as that's most outter again. So reverse again.
        y_plot_vals_r = []
        colors_w95_w100_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w95_w100))]
        colors_mid_w95_r_p_vals = [255-rgb[0] for rgb in list(reversed(colors_mid_w95))]

        colors_w60_mid_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w60_mid))]
        colors_mid_w60_r_p_vals = [255-rgb[0] for rgb in list(reversed(colors_mid_w60))]

        colors_w30_mid_top_r_vals = [255-rgb[0] for rgb in list(reversed(colors_w30_mid))]
        colors_w30_mid_bot_r_vals = [255-rgb[0] for rgb in list((colors_w30_mid))]

        print('y_plot_vals_r')
        print(y_plot_vals_r)
        y_plot_vals_r = y_plot_vals_r + \
                        colors_w95_w100_r_vals + colors_mid_w95_r_p_vals + \
                        colors_w60_mid_r_vals + colors_mid_w60_r_p_vals + \
                        colors_w30_mid_top_r_vals + colors_w30_mid_bot_r_vals + \
                        list(reversed(colors_mid_w60_r_p_vals)) + list(reversed(colors_w60_mid_r_vals)) + list(reversed(colors_mid_w95_r_p_vals)) + list(reversed(colors_w95_w100_r_vals))




        # Color chart
        print('y_plot_vals_r')
        print(len(y_plot_vals_r))
        print(y_plot_vals_r)

        plt.bar(np.arange(len(y_plot_vals_r)), y_plot_vals_r, width=1)
        plt.show()



        # # W60 p Line
        # print('reversed - colors_mid_w60 (ease out)')
        # print(list(reversed(colors_mid_w60)))
        # print('colors_w60_mid (ease out)')
        # print(colors_w60_mid)

        # # W60 Line
        # print('colors_mid_w60 (ease out)')
        # print(colors_mid_w60)
        # print('colors_w60_mid (ease out?)')
        # print(colors_w60_mid)

        # W95 Line, Bottom line
        print('colors_mid_w95 (ease out)')
        print(colors_mid_w95)
        print('colors_w95_w100 (ease out (both? maybe good enough))')
        print(colors_w95_w100)

        median = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(self.y_list, self.y_list),
            mode='lines',
            # legendgroup='group 95%',
            name='drawing shape',
            fill='tozeroy',
            fillcolor="#000000",
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': "#000000", 'width': 1,}
        )
        self.data.append(median)

    def plot(self):
        fig = go.Figure(data=self.data, layout=self.layout)

        if self.output == 'offline':
            plotly.offline.plot(fig, config={'displayModeBar': False},)
        if self.output == 'online':
            # Online plotly server version. Doesn't seem to be able to turn displayModeBar off.
            py.plot(fig, config={'displayModeBar': False})
        if self.output == 'jupyter':
            init_notebook_mode(connected=True)
            iplot(fig, config={'displayModeBar': False})


# For full fuzz
class FuzzPlotly:
    def __init__(self, x_list, y_list, ci95p, ci95n,
                 fuzz_size, fuzz_n,
                 color='#4286f4', layout={}, figs=[], output='auto'):
        self.x_list = x_list
        self.y_list = y_list
        self.ci95p = ci95p
        self.ci95n = ci95n
        self.fuzz_size = fuzz_size
        self.fuzz_n = fuzz_n
        self.layout = layout
        self.figs = figs
        self.color = color
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

    # # probability is between 0-1
    # # example p = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
    def generate_interval_point(self, p, center, std, offset=0):
        point = [p]
        boundary_point = norm.ppf(point, loc=center, scale=std)
        return boundary_point[0]

    def hex_to_rgb(self, hex_color):
        color = hex_color.lstrip('#')
        rgb_color = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
        return rgb_color

    def rgb_to_hex(self, rgb):
        hex_color = "".join([format(val, '02X') for val in rgb])
        return f"#{hex_color}"

    # Takes in user's input colour and calculates ci colours
    def calc_colour(self, upper_ci, lower_ci, per):
        h_ci = norm.ppf(upper_ci, loc=0, scale=1) - norm.ppf(lower_ci, loc=0, scale=1)
        # print(h_ci)
        w_ci = per / h_ci
        # print(w_ci)
        return w_ci

    def rgb_to_rgba(self, rgb, opacity):
        '''
        Takes rgb tuple and opacity between 0-1 and return rgba tuple.
        :param rgb:
        :param opacity:
        :return:
        '''
        color_rgba = rgb + (opacity,)
        return color_rgba

    def rgb_to_rgba_string(self, rgb, opacity):
        '''
        Takes rgb tuple and opacity between 0-1 and return rgba tuple.
        :param rgb:
        :param opacity:
        :return:
        '''
        color_rgba = rgb + (opacity,)
        return f"rgba{color_rgba}"

    def rbga_to_rgb(self, rgba):
        '''
        Takes in tuple of (255,255,255,1)
        :param rgba:
        :return:
        '''

        # Background color. Assumes it's white.
        BGColor = (255,255,255)

        r = ((1 - rgba[3]) * BGColor[0]) + (rgba[3] * rgba[0])
        g = ((1 - rgba[3]) * BGColor[1]) + (rgba[3] * rgba[1])
        b = ((1 - rgba[3]) * BGColor[2]) + (rgba[3] * rgba[2])
        rgb = (r,g,b)
        # print(rgb)
        return rgb

    def normalize_data(self, val, val_max, val_min):
        return (val - val_min) / (val_max - val_min)

    # Assume it's standard normal distribution with loc=0, scale=1 (mean=0, std=1)
    def calculate_fuzz_color_normal(self, fuzz_n):
        w95 = 1.959964
        step = w95 / fuzz_n

        scaling_to_1 = 2.5066282746310002 # 1 is max
        # scaling_to_0 = 0.01/0.058440944333451476 # 0.01 is min

        color = self.hex_to_rgb(self.color)
        # print('color')
        # print(color)
        r_color, g_color, b_color = color

        colors = []

        # Normalization part so opacity goes from 0 to 1
        norm_max = norm.pdf(0)
        norm_min = norm.pdf(w95)

        # Going from 0 to 95%. 0 is highest and 95% is lowest.
        for i in range(fuzz_n):
            # Option 0: Purely height values from norm curve
            # opacity = norm.pdf(i * step)

            # Option 1: This is just scaling so max is 1.
            # Multiples by "scaling_to_1" which pushes chart up so 1 is max
            # opacity = norm.pdf(i * step) * scaling_to_1

            # Option 2: This is using normalized so 0 to 1 now
            opacity = self.normalize_data(val=norm.pdf(i * step), val_max=norm_max, val_min=norm_min)

            # Option 3: Linear?
            # opacity = self.normalize_data(val=norm.pdf(i * step), val_max=norm_max, val_min=norm_min)


            color_rgba = (r_color, g_color, b_color, opacity)
            color_rgb = self.rbga_to_rgb(color_rgba)

            # print(f'i: {i}')
            # print(f'r_step: {step}')
            # print(f'opacity: {opacity}')
            # print(f'color_rgba: {color_rgba}')
            # print(f'color_rgb: {color_rgb}')
            # print()

            colors.append(color_rgb)
        return colors

    # Assume it's standard normal distribution with loc=0, scale=1 (mean=0, std=1)

    # Using helixCube
    # def calculate_fuzz_color_normal(self, fuzz_n):
    #
    #     def norm_value_to_pos(x, a, b, c, d):
    #         return (x-a) * ((d-c)/(b-a)) + c
    #
    #     w95 = 1.959964
    #     step = w95 / fuzz_n
    #
    #     # Using color values from cube helix.
    #     # my_cubehelix = Cubehelix.make(gamma=0.7, start=0.78, rotation=-0.35, sat=1, n=fuzz_n, reverse=True,
    #     #                               min_light=0.3, max_light=0.8
    #     #                               )
    #     # my_cubehelix = Cubehelix.make(gamma=0.7, start_hue=200, end_hue=70, sat=1, n=fuzz_n, reverse=True,
    #     #                               min_light=0.3, max_light=0.8
    #     #                               )
    #     my_cubehelix = Cubehelix.make(gamma=0.5, start=0.7, rotation=-0.3, sat=1.5, n=fuzz_n, reverse=True,
    #                                   min_light=0.3, max_light=1
    #                                   )
    #     # print(my_cubehelix.colors)
    #     # print(len(my_cubehelix.colors))
    #     cubehelix_colors = my_cubehelix.colors
    #
    #     color = self.hex_to_rgb(self.color)
    #     # print('color')
    #     # print(color)
    #     r_color, g_color, b_color = color
    #
    #     colors = []
    #
    #     # Normalization part so opacity goes from 0 to 1
    #     norm_max = norm.pdf(0)
    #     norm_min = norm.pdf(w95)
    #
    #     # Going from 0 to 95%. 0 is highest and 95% is lowest.
    #     for i in range(fuzz_n):
    #         opacity = self.normalize_data(val=norm.pdf(i * step), val_max=norm_max, val_min=norm_min)
    #         pos = int(round(norm_value_to_pos(x=opacity, a=0, b=1, c=0, d=fuzz_n-1)))
    #         print(type(pos))
    #         print(pos)
    #         print(type(cubehelix_colors[pos]))
    #         print(tuple(cubehelix_colors[pos]))
    #         colors.append(tuple(cubehelix_colors[pos]))
    #
    #     # print(f'len colors (from norm): {len(colors)}')
    #     # print(f'colors (from norm): {colors}')
    #     return colors


    # Finds color between two colors using gradient
    # go from low color to high
    def calculate_fuzz_colors(self, color_a, color_b, fuzz_n):
        color_a_r, color_a_g, color_a_b = color_a
        color_b_r, color_b_g, color_b_b = color_b
        colors = []
        fuzz_n = int(fuzz_n)
        # print(f'color_a: {color_a}')
        # print(f'color_b: {color_b}')
        r_step = abs(( - color_a_r + color_b_r))/fuzz_n
        g_step = abs(( - color_a_g + color_b_g))/fuzz_n
        b_step = abs(( - color_a_b + color_b_b))/fuzz_n

        # print(f'color_a_r: {color_a_r}')
        # print(f'color_b_r: {color_b_r}')
        # print(f'self.fuzz_n: {self.fuzz_n}')
        # print(f'r_step: {r_step}')
        # print(f'r_step: {r_step}')

        for i in range(fuzz_n):
            color = ((color_a_r + i*r_step), (color_a_g + i*g_step), (color_a_b + i*b_step), )

            # print(f'i: {i}')
            # print(f'r_step: {r_step}')
            # print(f'color: {color}')
            # color = color_a_r + (i*r_step)
            colors.append(color)

            # print(color)
            # print('===')
        return colors

    def calc_fuzz_area(self, upper, lower, fuzz_size):
        # area_diff = upper - lower
        area = [((y1 - y2)*fuzz_size)/2 for (y1, y2) in zip(upper, lower)]
        return area

    # Gives output Plotly can use
    def generate_y_line_data(self, upper, lower):
        """
        Creates shape of y values y plotly can use.
        """
        y_plotly_values = lower + list(reversed(upper))
        return y_plotly_values

    # Note: Always same for this chart. Could add in config in plotly for labels later.
    def generate_x_line_data(self):
        return self.x_list + list(reversed(self.x_list))

    def generate_shape(self, upper, lower, config):
        x_plotly_values = self.generate_x_line_data()
        y_plotly_values = self.generate_y_line_data(upper, lower)
        # print("Config at generate_shape")
        # print(config)
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

    # Finds fuzz for confidence interval with fuzz size and fuzz n.
    def create_fuzzy_shape(self, upper, lower, fuzz_size, fuzz_n, fuzz_colors):
        areas_upper = self.calc_fuzz_area(upper, lower, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_upper]

        # Since it's drawn from up to down, need list of strongest color to weakest.
        # print(fuzz_n)
        for i in range(1, fuzz_n+1):
            # print(f'i :{i}')
            # print(f'fuzz_n :{fuzz_n}')
            # print(f'len(fuzz_colors_upper) :{len(fuzz_colors_upper)}')
            # Upper fuzz
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": f'rgb{fuzz_colors[fuzz_n-i]}', "color_edge": f'rgb{fuzz_colors[fuzz_n-i]}'})

            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": f'rgb{fuzz_colors[fuzz_n-i]}', "color_edge": f'rgb{fuzz_colors[fuzz_n-i]}'})

        # Central Main shape
        # DELETE, no longer relevant in full fuzz
        # fuzz_main_up_lower = [upper - area for (upper, area) in zip(upper, areas_upper)]
        # fuzz_main_down_upper = [upper + area for (upper, area) in zip(lower, areas_upper)]
        # self.generate_shape(fuzz_main_up_lower, fuzz_main_down_upper, color_center)

    def create_data(self):
        color_rgb = self.hex_to_rgb(self.color)

        # Linear version
        # color_rgba_w95 = self.rgb_to_rgba(color_rgb, 0)
        # color_rgba_center = self.rgb_to_rgba(color_rgb, 1)

        # # Find upper. Reverse for other side.
        # colors_center_rgb_w95 = self.calculate_fuzz_colors(
        #     color_rgb_center,
        #     color_rgb_w95,
        #     self.fuzz_n,
        # )

        # print('color_rgb_w95')
        # print(color_rgba_w95)
        #
        # print('color_rgba_center')
        # print(color_rgba_center)
        # color_rgb_w95 = self.rbga_to_rgb(color_rgba_w95)

        colors_center_rgb_w95 = self.calculate_fuzz_color_normal(self.fuzz_n)


    # print(colors_center_rgb_w95)

        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci95n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            # color_center={"color": f'rgb{color_rgb_center}', "color_edge": f'rgb{color_rgb_center}'},
            fuzz_colors=colors_center_rgb_w95,
        )

        median = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(self.y_list, self.y_list),
            mode='lines',
            # legendgroup='group 95%',
            name='drawing shape',
            fill='tozeroy',
            fillcolor="#000000",
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': "#000000", 'width': 1,},
        )
        self.data.append(median)

    def plot(self):
        fig = go.Figure(data=self.data, layout=self.layout)

        if self.output == 'offline':
            plotly.offline.plot(fig, config={'displayModeBar': False},)
        if self.output == 'online':
            # Online plotly server version. Doesn't seem to be able to turn displayModeBar off.
            py.plot(fig, config={'displayModeBar': False})
        if self.output == 'jupyter':
            init_notebook_mode(connected=True)
            iplot(fig, config={'displayModeBar': False})
