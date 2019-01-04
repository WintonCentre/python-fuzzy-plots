import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm
from palettable.cubehelix import Cubehelix

import pandas as pd

# hard coded e for now
e = 0.05
# e = 0
e_offset = 0 # Fixes slight mis-alignment in plotly drawing

x_sample_values = ["2013-07",
                   "2013-08",
                   "2013-09",
                   "2013-10",
                   "2013-11",
                   "2013-12",
                   "2014-01",
                   "2014-02",
                   "2014-03",
                   "2014-04",
                   "2014-05",
                   "2014-06",
                   "2014-07",
                   "2014-08",
                   "2014-09",
                   "2014-10",
                   "2014-11",
                   "2014-12",
                   "2015-01",
                   "2015-02",
                   "2015-03",
                   "2015-04",
                   "2015-05",
                   "2015-06",
                   "2015-07",
                   "2015-08",
                   "2015-09",
                   "2015-10",
                   "2015-11",
                   "2015-12",
                   "2016-01",
                   "2016-02",
                   "2016-03",
                   "2016-04",
                   "2016-05",
                   "2016-06",
                   "2016-07",
                   "2016-08",
                   "2016-09",
                   "2016-10",
                   "2016-11",
                   "2016-12",
                   "2017-01",
                   "2017-02",
                   "2017-03",
                   "2017-04",
                   "2017-05",
                   "2017-06",
                   "2017-07",
                   "2017-08",
                   "2017-09",
                   "2017-10",
                   "2017-11",
                   "2017-12",
                   "2018-01",
                   "2018-02",
                   "2018-03",
                   "2018-04",
                   "2018-05",
                   "2018-06",
                   "2018-07",]



y_sample_values = [8.337618963728, 8.279171746205, 8.203023291325001, 8.16982661854, 8.097634166936, 8.008366857893, 8.058186936088001, 7.885838698153, 7.858881576058001, 7.855567493386, 7.820595855792, 7.818122337445001, 7.828704432914, 7.980026665154999, 7.849850895981, 7.79839463565, 7.75388054972, 7.746002782859, 7.668407780941, 7.690985902007999, 7.612645534365, 7.3747395662390005, 7.170755621192, 7.227406558807, 7.171694338855, 6.893654974382, 6.762184038944, 6.598652448781, 6.419642868308999, 6.285297334109, 6.1413396095340005, 6.007282987197, 5.963297915327, 5.9641084307379995, 5.871371751667, 5.713943557774, 5.6704875369000005, 5.586620413797999, 5.550096812713, 5.518101872629, 5.607761950272, 5.6011292164699995, 5.514911517329001, 5.373080972737, 5.288693295291, 5.184773292915, 5.076842783398, 5.099483022613001, 5.087590042512001, 5.116303933252, 5.086588537155, 5.022712701151001, 4.934685111503001, 4.913662261302, 4.885593397848, 4.948802059784, 4.801996126307, 4.840341849932, 4.801265584408, 4.776618718601, 4.7377872479250005,]

std = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

layout = {
    'showlegend': False,
    'xaxis': {
        'title': 'Date',
        'titlefont': {
            'family': 'Arial, sans-serif',
            'size': 18,
            'color': 'grey',
        },
        # 'ticktext':x_label,
        # 'tickvals':x,
        # 'ticktext':x_label_test,
        # 'tickvals':x_test,
        'showgrid':False,

        'tickmode':'array',
        'ticks': 'outside',
        'tickangle': 45,
        'showticklabels': True,
        # 'ticklen': 3,
        'tickwidth': 2,
        'tickcolor': '#000',


        # 'nticks': 5, #tickmode has to be auto

        # 'tick0': 'hello',
        # 'dtick': 0.5,

        # 'tickformat': '%{n}f'
        # '':,
    },
    'yaxis': {
        'title': 'Unemployment (in thousands)',
        'titlefont': {
            'family': 'Arial, sans-serif',
            'size': 18,
            'color': 'grey',
        },
        'showgrid':False,
        'range': [1000000/1000, 2600000/1000],

    }
}




class FuzzyPlotly:
    def __init__(self, x_list, y_list,
                 ci95p, ci95n, ci60p, ci60n, ci30p, ci30n,
                 fuzz_size, fuzz_n,
                 color='#4286f4', layout={}, figs=[], output='auto'):
        plotly.tools.set_credentials_file(username='oneGene', api_key='JvxeS4ghBsrIRKsXYfTf')
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

    # # probability is between 0-1
    # # example p = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
    # def generate_interval_point(self, p, center, std, offset=0):
    #     point = [p+offset]
    #     boundary_point = norm.ppf(point, loc=center, scale=std)
    #     # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
    #     return boundary_point[0]

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

    def create_color_opacity(self):
        '''
        Calculates color opacity for set confidence intervals using normal distribution to match confidence intervals
        :return:
        '''
        # [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
        w_30 = self.calc_colour(0.65, 0.35, 0.3)
        w_60 = self.calc_colour(0.8, 0.2, 0.3)
        w_95 = self.calc_colour(0.975, 0.025, 0.35)

        # factor used to scale to 1 (for opacity)
        a = 1 / w_30

        # 1, 1, 2
        w_30_final = w_30 * a / 1
        w_60_final = w_60 * a / 1  # modified color
        w_95_final = w_95 * a / 1  # modified color

        color_opacity = {
            'w_30': w_30_final,
            'w_60': w_60_final,
            'w_95': w_95_final,
        }
        # color_opacity = {
        #     'w_30': 1,
        #     'w_60': 0.7,
        #     'w_95': 0.2,
        # }
        print(color_opacity)
        # print(w_30)
        # print(w_60)
        # print(w_95)
        #
        # print("")
        #
        # print(w_30 * a)
        # print(w_60 * a)
        # print(w_95 * a)
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

    # Finds color between two colors using gradient
    # takes rgb only.?
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
            # print(f'color_a_r: {color_a_r}')
            # color = color_a_r + (i*r_step)
            colors.append(color)

            # print(color)
            # print('===')
        # print(colors[0])
        # print(colors[-1])
        # print('')
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
            cur_up_upper = [upper - (area*(i-1)) for (upper, area) in zip(upper, area_per_fuzz)]
            cur_up_lower = [upper - (area*(i)) for (upper, area) in zip(upper, area_per_fuzz)]
            self.generate_shape(cur_up_upper, cur_up_lower, {"color": f'rgb{fuzz_colors_upper[fuzz_n-i]}', "color_edge": f'rgb{fuzz_colors_upper[fuzz_n-i]}'})

            # Lower fuzz - Building from bottom to top
            cur_down_upper = [upper + (area*(i)) for (upper, area) in zip(lower, area_per_fuzz)]
            cur_down_lower = [upper + (area*(i-1)) for (upper, area) in zip(lower, area_per_fuzz)]
            self.generate_shape(cur_down_upper, cur_down_lower, {"color": f'rgb{fuzz_colors_lower[fuzz_n-i]}', "color_edge": f'rgb{fuzz_colors_lower[fuzz_n-i]}'})

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

        colors_w30_w60 = self.calculate_fuzz_colors(
            color_rgb_w30,
            color_rgb_w60,
            self.fuzz_n,
        )
        colors_w60_w95 = self.calculate_fuzz_colors(
            color_rgb_w60,
            color_rgb_w95,
            self.fuzz_n,
        )
        # assumes max is white?
        colors_w95_w100 = self.calculate_fuzz_colors(
            color_rgb_w95,
            (255, 255, 255),
            self.fuzz_n,
        )

        # Find mid point
        color_w30_mid_w60 = self.calculate_fuzz_colors(
            color_rgb_w30,
            color_rgb_w60,
            self.fuzz_n,
        )[int(self.fuzz_n/2)]

        # Find upper
        colors_w30_mid = self.calculate_fuzz_colors(
            color_rgb_w30,
            color_w30_mid_w60,
            self.fuzz_n,
        )

        # Find lower
        colors_mid_w60 = self.calculate_fuzz_colors(
            color_w30_mid_w60,
            color_rgb_w60,
            self.fuzz_n,
        )
        # print(color_w30_mid_w60)
        # print(colors_w30_mid)
        # print(colors_mid_w60)
        # print(colors_w30_w60)

        # Find mid point
        color_w60_mid_w95 = self.calculate_fuzz_colors(
            color_rgb_w60,
            color_rgb_w95,
            self.fuzz_n,
        )[int(self.fuzz_n/2)]

        # Find upper
        colors_w60_mid = self.calculate_fuzz_colors(
            color_rgb_w60,
            color_w60_mid_w95,
            self.fuzz_n,
            )
        print("colors_w60_mid")
        print(colors_w60_mid)

        # Find lower
        colors_mid_w95 = self.calculate_fuzz_colors(
            color_w60_mid_w95,
            color_rgb_w95,
            self.fuzz_n,
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

        self.create_fuzzy_shape(
            upper=self.ci95p, lower=self.ci60p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w95}', "color_edge": f'rgb{color_rgb_w95}'},
            fuzz_colors_upper=colors_w95_w100, fuzz_colors_lower=list(reversed(colors_mid_w95)),
        )
        self.create_fuzzy_shape(
            upper=self.ci60p, lower=self.ci30p, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w60}', "color_edge": f'rgb{color_rgb_w60}'},
            fuzz_colors_upper=colors_w60_mid, fuzz_colors_lower=list(reversed(colors_mid_w60)),
        )
        self.create_fuzzy_shape(
            upper=self.ci30p, lower=self.ci30n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w30}', "color_edge": f'rgb{color_rgb_w30}'},
            fuzz_colors_upper=colors_w30_mid, fuzz_colors_lower=colors_w30_mid,
        )
        self.create_fuzzy_shape(
            upper=self.ci30n, lower=self.ci60n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w60}', "color_edge": f'rgb{color_rgb_w60}'},
            fuzz_colors_upper=list(reversed(colors_mid_w60)), fuzz_colors_lower=colors_w60_mid,
        )
        self.create_fuzzy_shape(
            upper=self.ci60n, lower=self.ci95n, fuzz_size=self.fuzz_size, fuzz_n=self.fuzz_n,
            color_center={"color": f'rgb{color_rgb_w95}', "color_edge": f'rgb{color_rgb_w95}'},
            fuzz_colors_upper=list(reversed(colors_mid_w95)), fuzz_colors_lower=colors_w95_w100,
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
            line={'color': "#000000", 'width': 1,}
        )
        self.data.append(median)

    def datax(self):

        fillcolor = {
            "fill01_fuzz": "#355B92",
            "fill01": "#204A87",

            "fill02_fuzz_up": "#4C6E9F",
            "fill02": "#6D89B1",
            "fill02_fuzz_down": "#8FA4C3",

            "fill03_fuzz": "#B1C0D5",
            "fill03": "#D2DBE7",
            # Same

            "median": "#EF2929",
        }

        # fillcolor = {
        #     "fill01_fuzz": "#355B92",
        #     "fill01": "#E0ECE6",
        #
        #     "fill02_fuzz_up": "#C6D9CF",
        #     "fill02": "#A8C6B6",
        #     "fill02_fuzz_down": "#9FBFAF",
        #
        #     "fill03_fuzz": "#AFC9BC",
        #     "fill03": "#A3C2B3",
        #     # Same
        #
        #     "median": "#EF2929",
        # }

        # Create areas.

        median = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.5, -0.01, 0.01),
            mode='lines',
            name='median',
            fillcolor=fillcolor["median"],
            line={'color': fillcolor["median"], 'width': 1}
        )

        # p=[0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]

        area01 = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.8875, 0.0875, 0.08125-e+e_offset),
            mode='lines',
            legendgroup='group 95%',
            name='95%',
            fill='tozeroy',
            fillcolor=fillcolor["fill03"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill03"], 'width': 0.5}
        )

        e_area01_lower = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.80625, e, 0+e_offset),
            mode='lines',
            legendgroup='group 95%',
            # name='95% lower',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill03_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill03_fuzz"], 'width': 0.5}
        )

        e_area02_upper = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.80625, 0, e+e_offset),
            mode='lines',
            legendgroup='group 60%',
            # name='60% upper',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_down"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02_fuzz_down"], 'width': 0.5}
        )

        area02 = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.725, 0.08125-e, 0.1125-e+e_offset),
            mode='lines',
            legendgroup='group 60%',
            name='60%',
            fill='tozeroy',
            fillcolor=fillcolor["fill02"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02"], 'width': 1}
        )

        e_area02_lower = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.6125, e, 0+e_offset),
            mode='lines',
            legendgroup='group 60%',
            # name='60% lower',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_up"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02_fuzz_up"], 'width': 1}
        )

        e_area03_upper = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.6125, 0, e+e_offset),
            mode='lines',
            legendgroup='group 30%',
            # name='30% upper',
            showlegend=False,
            fill='tozeroy',
            fillcolor= fillcolor["fill01_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill01_fuzz"], 'width': 1}
        )

        area03 = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.5, 0.1125-e, 0.1125-e),
            mode='lines',
            legendgroup='group 30%',
            name='30%',
            fill='tozeroy',
            fillcolor=fillcolor["fill01"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill01"], 'width': 0.5}
        )

        e_area03_lower = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.3875, e+e_offset, 0),
            mode='lines',
            legendgroup='group 30%',
            # name='30% lower',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill01_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill01_fuzz"], 'width': 1}
        )

        e_area04_upper = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.3875, 0+e_offset, e),
            mode='lines',
            legendgroup='group 60%',
            # name='60% upper',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_up"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02_fuzz_up"], 'width': 1}
        )

        area04 = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.275, 0.1125-e+e_offset, 0.08125-e),
            mode='lines',
            legendgroup='group 60%',
            name='60%',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill02"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02"], 'width': 1}
        )

        e_area04_lower = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.19375, e+e_offset, 0),
            mode='lines',
            legendgroup='group 60%',
            name='60% lower',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_down"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill02_fuzz_down"], 'width': 1}
        )

        e_area05_upper = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.19375, 0+e_offset, e),
            mode='lines',
            legendgroup='group 95%',
            name='95% upper',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill03_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill03_fuzz"], 'width': 1}
        )

        area05 = go.Scatter(
            x=self.generate_x_line_data(),
            y=self.generate_y_line_data(0.1125, 0.08125-e+e_offset, 0.0875),
            mode='lines',
            legendgroup='group 95%',
            name='95%',
            showlegend=False,
            fill='tozeroy',
            fillcolor=fillcolor["fill03"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'color': fillcolor["fill03"], 'width': 1}
        )

        data = [
                            area01, e_area01_lower,
            e_area02_upper, area02, e_area02_lower,
            e_area03_upper, area03, e_area03_lower,
            e_area04_upper, area04, e_area04_lower,
            e_area05_upper, area05, median,
        ] + self.figs

        return data

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
        plotly.tools.set_credentials_file(username='oneGene', api_key='JvxeS4ghBsrIRKsXYfTf')
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


# For Full fuzz "FuzzPlotly" Trying
if __name__ == '__main__':

    x_list = ['Aug-Oct 2013', 'Sep-Nov 2013', 'Oct-Dec 2013', 'Nov-Jan 2014', 'Dec-Feb 2014', 'Jan-Mar 2014', 'Feb-Apr 2014', 'Mar-May 2014', 'Apr-Jun 2014', 'May-Jul 2014', 'Jun-Aug 2014', 'Jul-Sep 2014', 'Aug-Oct 2014', 'Sep-Nov 2014', 'Oct-Dec 2014', 'Nov-Jan 2015', 'Dec-Feb 2015', 'Jan-Mar 2015', 'Feb-Apr 2015', 'Mar-May 2015', 'Apr-Jun 2015', 'May-Jul 2015', 'Jun-Aug 2015', 'Jul-Sep 2015', 'Aug-Oct 2015', 'Sep-Nov 2015', 'Oct-Dec 2015', 'Nov-Jan 2016', 'Dec-Feb 2016', 'Jan-Mar 2016', 'Feb-Apr 2016', 'Mar-May 2016', 'Apr-Jun 2016', 'May-Jul 2016', 'Jun-Aug 2016', 'Jul-Sep 2016', 'Aug-Oct 2016', 'Sep-Nov 2016', 'Oct-Dec 2016', 'Nov-Jan 2017', 'Dec-Feb 2017', 'Jan-Mar 2017', 'Feb-Apr 2017', 'Mar-May 2017', 'Apr-Jun 2017', 'May-Jul 2017', 'Jun-Aug 2017', 'Jul-Sep 2017', 'Aug-Oct 2017', 'Sep-Nov 2017', 'Oct-Dec 2017', 'Nov-Jan 2018', 'Dec-Feb 2018', 'Jan-Mar 2018', 'Feb-Apr 2018', 'Mar-May 2018', 'Apr-Jun 2018', 'May-Jul 2018', 'Jun-Aug 2018', 'Jul-Sep 2018', 'Aug-Oct 2018']



    y_p_95 = [2564.998456480288, 2451.9984932307575, 2396.9984932307575, 2367.998511605992, 2304.9985299812265, 2274.998566731696, 2189.998566731696, 2116.9985851069305, 2107.9985851069305, 2123.9985851069305, 2117.9986034821654, 2120.9986034821654, 2105.998566731696, 2022.9986034821654, 1901.9986402326347, 1879.9986586078694, 1883.9986402326347, 1889.9986402326347, 1839.9986586078694, 1854.9986218574, 1896.9986034821654, 1933.9986034821654, 1921.9986034821654, 1912.9986218574, 1862.9986402326347, 1776.9986769831041, 1716.9986953583386, 1705.9986769831041, 1742.9986769831041, 1751.9986586078694, 1690.9987137335734, 1651.9987137335734, 1687.9986769831041, 1742.9986402326347, 1808.9986034821654, 1767.9986034821654, 1762.9985851069307, 1692.9986218574, 1620.9986402326347, 1598.9986586078694, 1596.9986586078694, 1598.9986769831041, 1548.9987137335734, 1496.998732108808, 1527.9986953583386, 1561.9986769831041, 1586.9986769831041, 1572.9986769831041, 1567.9986769831041, 1522.9987137335734, 1496.9987137335734, 1473.998732108808, 1462.9987137335734, 1486.9987137335734, 1442.998732108808, 1416.9987137335734, 1402.998732108808, 1461.9986953583386, 1499.9986769831041, 1522.9986586078694, 1521.9986586078694]

    y_n_95 = [2397.001543519712, 2288.0015067692425, 2233.0015067692425, 2206.001488394008, 2145.0014700187735, 2119.001433268304, 2034.001433268304, 1963.0014148930693, 1954.0014148930693, 1970.0014148930693, 1966.0013965178346, 1969.0013965178346, 1950.001433268304, 1871.0013965178346, 1754.0013597673653, 1734.0013413921306, 1736.0013597673653, 1742.0013597673653, 1694.0013413921306, 1705.0013781426, 1745.0013965178346, 1782.0013965178346, 1770.0013965178346, 1763.0013781426, 1715.0013597673653, 1633.0013230168959, 1575.0013046416614, 1562.0013230168959, 1599.0013230168959, 1606.0013413921306, 1551.0012862664266, 1512.0012862664266, 1544.0013230168959, 1595.0013597673653, 1657.0013965178346, 1616.0013965178346, 1609.0014148930693, 1543.0013781426, 1473.0013597673653, 1453.0013413921306, 1451.0013413921306, 1455.0013230168959, 1409.0012862664266, 1359.001267891192, 1386.0013046416614, 1418.0013230168959, 1443.0013230168959, 1429.0013230168959, 1424.0013230168959, 1383.0012862664266, 1357.0012862664266, 1336.001267891192, 1323.0012862664266, 1347.0012862664266, 1305.001267891192, 1277.0012862664266, 1265.001267891192, 1320.0013046416614, 1356.0013230168959, 1377.0013413921306, 1376.0013413921306]

    y_median = [2481.0, 2370.0, 2315.0, 2287.0, 2225.0, 2197.0, 2112.0, 2040.0, 2031.0, 2047.0, 2042.0, 2045.0, 2028.0, 1947.0, 1828.0, 1807.0, 1810.0, 1816.0, 1767.0, 1780.0, 1821.0, 1858.0, 1846.0, 1838.0, 1789.0, 1705.0, 1646.0, 1634.0, 1671.0, 1679.0, 1621.0, 1582.0, 1616.0, 1669.0, 1733.0, 1692.0, 1686.0, 1618.0, 1547.0, 1526.0, 1524.0, 1527.0, 1479.0, 1428.0, 1457.0, 1490.0, 1515.0, 1501.0, 1496.0, 1453.0, 1427.0, 1405.0, 1393.0, 1417.0, 1374.0, 1347.0, 1334.0, 1391.0, 1428.0, 1450.0, 1449.0]

    my_fuzz_plot = FuzzPlotly(x_list=x_list, y_list=y_median, ci95p=y_p_95, ci95n=y_n_95, fuzz_size=1, fuzz_n=100, output='offline', layout=layout)

    my_fuzz_plot.create_data()
    my_fuzz_plot.plot()



# if __name__ == '__main__':
#
#     df = pd.read_csv("../csv/unemployment 2012-2017.csv")
#     std = list(df['sd'])
#     y = list(df['People'])
#
#     y_n_95 = []
#     y_p_95 = []
#
#     y_n_60 = []
#     y_p_60 = []
#
#     y_n_30 = []
#     y_p_30 = []
#
#     y_median = []
#
#     def generate_interval_point(p, center, std, offset=0):
#         point = [p+offset]
#         boundary_point = norm.ppf(point, loc=center, scale=std)
#         # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
#         return boundary_point[0]
#
#     for i in range(len(y)):
#         y_n_95.append(generate_interval_point(0.025, y[i], std[i]))
#         y_p_95.append(generate_interval_point(0.975, y[i], std[i]))
#
#         y_n_60.append(generate_interval_point(0.2, y[i], std[i]))
#         y_p_60.append(generate_interval_point(0.8, y[i], std[i]))
#
#         y_n_30.append(generate_interval_point(0.35, y[i], std[i]))
#         y_p_30.append(generate_interval_point(0.65, y[i], std[i]))
#
#         y_median.append(generate_interval_point(0.5, y[i], std[i]))
#
#     # print(y_n_95)
#
#     # Need to add now
#     # n = Number of lines, u = Fuzziness size in %. 1 is 100%, 0.1 is 10%.
#
#
#     # # Discrete lines
#     # test_plot.generate_shape(y_p_95, y_p_60)
#     # test_plot.generate_shape(y_p_60, y_p_30)
#     #
#     # test_plot.generate_shape(y_p_30, y_n_30)
#     #
#     # test_plot.generate_shape(y_n_30, y_n_60)
#     # test_plot.generate_shape(y_n_60, y_n_95)
#
#
#     # With fuzz boundaries but no fuzzying
#     # areas_p_95 = test_plot.calc_fuzz_area(y_p_95, y_p_60, fuzz_size=0.1, fuzz_n=2)
#     #
#     # fuzz_p_95_up_lower = [upper - area for (upper, area) in zip(y_p_95, areas_p_95)]
#     # fuzz_p_95_down_upper = [upper + area for (upper, area) in zip(y_p_60, areas_p_95)]
#     #
#     # print(y_p_95)
#     # print(fuzz_p_95_up_lower)
#     # # print(fuzz_p_95_down_upper)
#     # # print(y_p_60)
#     #
#     # # print(len(y_p_95))
#     # # print(len(fuzz_95_up_lower))
#     # # print(len(fuzz_95_down_upper))
#     # # print(len(y_p_60))
#     #
#     # test_plot.generate_shape(y_p_95, fuzz_p_95_up_lower)
#     # test_plot.generate_shape(fuzz_p_95_up_lower, fuzz_p_95_down_upper)
#     # test_plot.generate_shape(fuzz_p_95_down_upper, y_p_60)
#     #
#     # # test_plot.generate_shape(y_p_30, y_n_30)
#
#
#     # Fuzzy plot example 01
#     test_plot = FuzzyPlotly(
#         x_sample_values, y_median,
#         ci95p=y_p_95, ci95n=y_n_95,
#         ci60p=y_p_60, ci60n=y_n_60,
#         ci30p=y_p_30, ci30n=y_n_30,
#         fuzz_size=1, fuzz_n=20, color="#0000FF"
#                 )
#     test_plot.create_data()
#     test_plot.plot()
#
#     # Fuzzy plot example 02
#     # test_plot2 = FuzzyPlotly(
#     #     x_sample_values, y_median,
#     #     ci95p=y_p_95, ci95n=y_n_95,
#     #     ci60p=y_p_60, ci60n=y_n_60,
#     #     ci30p=y_p_30, ci30n=y_n_30,
#     #     fuzz_size=0.8, fuzz_n=10, color="#0000FF"
#     #             )
#     # test_plot2.create_data()
#     # test_plot2.plot()
#
#     # # Discrete plot example 03
#     # test_plot_discrete = FuzzyPlotly(
#     #     x_sample_values, y_median,
#     #     ci95p=y_p_95, ci95n=y_n_95,
#     #     ci60p=y_p_60, ci60n=y_n_60,
#     #     ci30p=y_p_30, ci30n=y_n_30,
#     #     fuzz_size=0.01, fuzz_n=1, color="#0000FF"
#     # )
#     # test_plot_discrete.create_data()
#     # test_plot_discrete.plot()
