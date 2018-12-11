import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm


# juypter notebook version
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

# hard coded e for now
e = 0.025
e_offset = 0 # Fixes slight mis-alignment in plotly drawing

x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

y_values = [8.337618963728, 8.279171746205, 8.203023291325001, 8.16982661854, 8.097634166936, 8.008366857893, 8.058186936088001, 7.885838698153, 7.858881576058001, 7.855567493386, 7.820595855792, 7.818122337445001, 7.828704432914, 7.980026665154999, 7.849850895981, 7.79839463565, 7.75388054972, 7.746002782859, 7.668407780941, 7.690985902007999, 7.612645534365, 7.3747395662390005, 7.170755621192, 7.227406558807, 7.171694338855, 6.893654974382, 6.762184038944, 6.598652448781, 6.419642868308999, 6.285297334109, 6.1413396095340005, 6.007282987197, 5.963297915327, 5.9641084307379995, 5.871371751667, 5.713943557774, 5.6704875369000005, 5.586620413797999, 5.550096812713, 5.518101872629, 5.607761950272, 5.6011292164699995, 5.514911517329001, 5.373080972737, 5.288693295291, 5.184773292915, 5.076842783398, 5.099483022613001, 5.087590042512001, 5.116303933252, 5.086588537155, 5.022712701151001, 4.934685111503001, 4.913662261302, 4.885593397848, 4.948802059784, 4.801996126307, 4.840341849932, 4.801265584408, 4.776618718601, 4.7377872479250005,]

std = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


"""
# Also able to custom label? Number of intervals?
# Lets stick to 30%, 60%, 95%
def read_csv(csv_name, column_x, column_y, std):
    use pandas as quick way to read csv.
    returns as list column_x, column_y, std
        
"""


# Optional future params, number of intervals, color scheme (dict?), fuzziness,
# TODO: Add credential files as argument.
# Output can be 4 different states. offline, online, jupyter, auto
class FuzzyPlotly:
    def __init__(self, x_list, y_list, std_list, figs=[], output='auto'):
        #TODO: User should set this themself if they want online functionality
        plotly.tools.set_credentials_file(username='oneGene', api_key='JvxeS4ghBsrIRKsXYfTf')
        self.x_list = x_list
        self.y_list = y_list
        self.std_list = std_list
        self.figs = figs

        # Automatically figures out if it's running in ipython. If not
        # Add default value of offline
        if output == 'auto':
            try:
                get_ipython()
                self.output = 'jupyter'
            except NameError:
                self.output = 'offline'
        else:
            self.output = output

    # function which takes in mean, std (optional configs?) and returns

    # probability is between 0-1
    # example p = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
    def generate_interval_point(self, p, center, std, offset=0):
        point = [p+offset]
        boundary_point = norm.ppf(point, loc=center, scale=std)
        # print(f'point: {point}, p: {p}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
        return boundary_point[0]

    # Gives output Plotly can use
    def generate_y_line_data(self, p, e_upper, e_lower):
        """
        Given probability, return x and y plotly can use.
        """
        # I need list of lower values
        # I need list of upper values
        # Put them together to feed into plotly scatter
        y_lower = []
        y_upper = []

        for i in range(len(self.y_list)):
            y_lower_point = self.generate_interval_point(p, self.y_list[i], self.std_list[i], -e_lower)
            y_upper_point = self.generate_interval_point(p, self.y_list[i], self.std_list[i], e_upper)
            y_lower.append(y_lower_point)
            y_upper.append(y_upper_point)

        # print(y_lower)
        # print(y_upper)

        y_plotly_values = y_lower + list(reversed(y_upper))
        return y_plotly_values

    # Note: Always same for this chart. Could add in config in plotly for labels later.
    def generate_x_line_data(self):
        return self.x_list + list(reversed(self.x_list))

    # def gamma_norm(self, p):
    #     # Given p value, find opacity.
    #     return 1 / norm.pdf(p)

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
        data = self.data()

        if self.output == 'offline':
            plotly.offline.plot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})
        if self.output == 'online':
            # Online plotly server version. Doesn't seem to be able to turn displayModeBar off.
            py.plot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})
        if self.output == 'jupyter':
            init_notebook_mode(connected=True)
            iplot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})


if __name__ == '__main__':

    new_fig_a_1 = {
        'marker': {'color': 'red', 'size': 10, 'symbol': 104},
        'mode': 'markers+lines',
        'name': '1st Trace',
        'text': ['one', 'two', 'three'],
        'type': 'scatter',
        'x': [1, 2, 3],
        'y': [4, 2, 1]
    }

    new_fig_a_2 = {
        'marker': {'color': 'green', 'size': 5, 'symbol': 104},
        'mode': 'markers+lines',
        'name': '1st Trace',
        'text': ['one', 'two', 'three'],
        'type': 'scatter',
        'x': [8, 9, 10],
        'y': [4, 8, 1]
    }

    # Maybe in CSV user can also add labels?

    new_fig2 = go.Scatter(x=[4,5,6], y=[4,5,6], marker={'color': 'red', 'symbol': 104, 'size': 10},  mode="markers+lines",  text=["one","two","three"])
    new_fig3 = go.Scatter(
        x=[4,5,6],
        y=[4,5,9],
        marker={'color': 'red', 'symbol': 104, 'size': 10},
        mode="markers+lines",
        text=["one","two","three"]
    )

    # Plotting directly
    my_plt = FuzzyPlotly(x_values, y_values, std, output='online')
    # my_plt = FuzzyPlotly(x_values, y_values, std, figs=[new_fig2, new_fig3])
    my_plt.plot()

    # Taking out data and plotting independently
    # data = my_plt.data()
    # print(data)
    # data = data + [new_fig_a_1, new_fig2]
    # plotly.offline.plot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})
    # py.plot(data, filename='my_own_plot', config={'displayModeBar': False})
