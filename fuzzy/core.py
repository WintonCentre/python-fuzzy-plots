import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm

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


# Optional future params, number of intervals, color scheme (dict?), fuzziness,
class FuzzyPlotly:
    def __init__(self, x_list, y_list,
                 ci95p, ci95n, ci60p, ci60n, ci30p, ci30n,
                 fuzz_size, fuzz_n,
                 layout={}, figs=[], output='auto'):
        plotly.tools.set_credentials_file(username='oneGene', api_key='JvxeS4ghBsrIRKsXYfTf')
        self.x_list = x_list
        self.y_list = y_list
        self.ci95p = ci95p
        self.ci95n = ci95n
        self.ci60p = ci60p
        self.ci60n = ci60n
        self.ci30p = ci30p
        self.ci30n = ci30n,
        self.fuzz_size = fuzz_size,
        self.fuzz_n = fuzz_n,
        self.layout = layout
        self.figs = figs
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

    def generate_shape(self, upper, lower):
        x_plotly_values = self.generate_x_line_data()
        y_plotly_values = self.generate_y_line_data(upper, lower)
        area = go.Scatter(
            x=x_plotly_values,
            y=y_plotly_values,
            mode='lines',
            # legendgroup='group 95%',
            name='drawing shape',
            fill='tozeroy',
            # fillcolor=fillcolor["fill03"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
            line={'width': 0.5}
        )
        self.data.append(area)
        return area

    # Finds fuzz given size and n.
    def create_fuzzy_area(self, upper, lower, fuzz_size, fuzz_n):
        areas_p_95 = test_plot.calc_fuzz_area(self.ci95p, self.ci60p, fuzz_size=fuzz_size)
        area_per_fuzz = [area/fuzz_n for area in areas_p_95]
        # print(areas_p_95)
        # print(area_per_fuzz)


        # Create area with all the fuzz and by generating upper and lower of each line
        # Building from Top to bottom
        # Upper fuzz
        for i in range(1, fuzz_n+1):
            cur_upper = [upper - (area*(i-1)) for (upper, area) in zip(self.ci95p, area_per_fuzz)]
            cur_lower = [upper - (area*(i)) for (upper, area) in zip(self.ci95p, area_per_fuzz)]
            self.generate_shape(cur_upper, cur_lower)

        # Lower fuzz - Building from bottom to top
        for i in range(1, fuzz_n+1):
            cur_upper = [upper + (area*(i)) for (upper, area) in zip(self.ci60p, area_per_fuzz)]
            cur_lower = [upper + (area*(i-1)) for (upper, area) in zip(self.ci60p, area_per_fuzz)]
            self.generate_shape(cur_upper, cur_lower)


    # Central Main shape
        fuzz_p_95_up_lower = [upper - area for (upper, area) in zip(self.ci95p, areas_p_95)]
        fuzz_p_95_down_upper = [upper + area for (upper, area) in zip(self.ci60p, areas_p_95)]
        self.generate_shape(fuzz_p_95_up_lower, fuzz_p_95_down_upper)

    def data(self):

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


if __name__ == '__main__':

    df = pd.read_csv("../csv/unemployment 2012-2017.csv")
    std = list(df['sd'])
    y = list(df['People'])

    y_n_95 = []
    y_p_95 = []

    y_n_60 = []
    y_p_60 = []

    y_n_30 = []
    y_p_30 = []

    y_median = []

    def generate_interval_point(p, center, std, offset=0):
        point = [p+offset]
        boundary_point = norm.ppf(point, loc=center, scale=std)
        # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
        return boundary_point[0]

    for i in range(len(y)):
        y_n_95.append(generate_interval_point(0.025, y[i], std[i]))
        y_p_95.append(generate_interval_point(0.975, y[i], std[i]))

        y_n_60.append(generate_interval_point(0.2, y[i], std[i]))
        y_p_60.append(generate_interval_point(0.8, y[i], std[i]))

        y_n_30.append(generate_interval_point(0.35, y[i], std[i]))
        y_p_30.append(generate_interval_point(0.65, y[i], std[i]))

        y_median.append(generate_interval_point(0.5, y[i], std[i]))

    # print(y_n_95)

    # Need to add now
    # n = Number of lines, u = Fuzziness size in %. 1 is 100%, 0.1 is 10%.
    test_plot = FuzzyPlotly(
        x_sample_values, y_median,
        ci95p=y_p_95, ci95n=y_n_95,
        ci60p=y_p_60, ci60n=y_n_60,
        ci30p=y_p_30, ci30n=y_n_30,
        fuzz_size=0.1, fuzz_n=2,
                )
    # # Discrete lines
    # test_plot.generate_shape(y_p_95, y_p_60)
    # test_plot.generate_shape(y_p_60, y_p_30)
    #
    # test_plot.generate_shape(y_p_30, y_n_30)
    #
    # test_plot.generate_shape(y_n_30, y_n_60)
    # test_plot.generate_shape(y_n_60, y_n_95)


    # With fuzz boundaries but no fuzzying
    # areas_p_95 = test_plot.calc_fuzz_area(y_p_95, y_p_60, fuzz_size=0.1, fuzz_n=2)
    #
    # fuzz_p_95_up_lower = [upper - area for (upper, area) in zip(y_p_95, areas_p_95)]
    # fuzz_p_95_down_upper = [upper + area for (upper, area) in zip(y_p_60, areas_p_95)]
    #
    # print(y_p_95)
    # print(fuzz_p_95_up_lower)
    # # print(fuzz_p_95_down_upper)
    # # print(y_p_60)
    #
    # # print(len(y_p_95))
    # # print(len(fuzz_95_up_lower))
    # # print(len(fuzz_95_down_upper))
    # # print(len(y_p_60))
    #
    # test_plot.generate_shape(y_p_95, fuzz_p_95_up_lower)
    # test_plot.generate_shape(fuzz_p_95_up_lower, fuzz_p_95_down_upper)
    # test_plot.generate_shape(fuzz_p_95_down_upper, y_p_60)
    #
    # # test_plot.generate_shape(y_p_30, y_n_30)


    test_plot.create_fuzzy_area(upper="x", lower="x", fuzz_size=0.1, fuzz_n=10)

    test_plot.plot()
