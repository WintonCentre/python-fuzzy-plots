import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from scipy.stats import norm


# juypter notebook version
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

# hard coded e for now
e = 0.025
e_offset = 0.001 # Fixes slight mis-alignment in plotly drawing

x_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

y_values = [8.337618963728, 8.279171746205, 8.203023291325001, 8.16982661854, 8.097634166936, 8.008366857893, 8.058186936088001, 7.885838698153, 7.858881576058001, 7.855567493386, 7.820595855792, 7.818122337445001, 7.828704432914, 7.980026665154999, 7.849850895981, 7.79839463565, 7.75388054972, 7.746002782859, 7.668407780941, 7.690985902007999, 7.612645534365, 7.3747395662390005, 7.170755621192, 7.227406558807, 7.171694338855, 6.893654974382, 6.762184038944, 6.598652448781, 6.419642868308999, 6.285297334109, 6.1413396095340005, 6.007282987197, 5.963297915327, 5.9641084307379995, 5.871371751667, 5.713943557774, 5.6704875369000005, 5.586620413797999, 5.550096812713, 5.518101872629, 5.607761950272, 5.6011292164699995, 5.514911517329001, 5.373080972737, 5.288693295291, 5.184773292915, 5.076842783398, 5.099483022613001, 5.087590042512001, 5.116303933252, 5.086588537155, 5.022712701151001, 4.934685111503001, 4.913662261302, 4.885593397848, 4.948802059784, 4.801996126307, 4.840341849932, 4.801265584408, 4.776618718601, 4.7377872479250005,]

std = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


# y01Up = [9.137618963728, 9.079171746205, 9.003023291325002, 8.96982661854, 8.897634166936001, 8.808366857893, 8.858186936088002, 8.685838698153, 8.658881576058, 8.655567493386, 8.620595855792, 8.618122337445001, 8.628704432914, 8.780026665154999, 8.649850895981, 8.598394635650001, 8.55388054972, 8.546002782859, 8.468407780941, 8.490985902008, 8.412645534365, 8.174739566239001, 7.970755621192, 8.027406558807, 7.9716943388549995, 7.6936549743819995, 7.562184038944, 7.398652448781, 7.219642868308999, 7.085297334109, 6.941339609534, 6.8072829871969995, 6.763297915327, 6.764108430737999, 6.6713717516669995, 6.513943557774, 6.4704875369, 6.386620413797999, 6.350096812713, 6.318101872629, 6.407761950272, 6.401129216469999, 6.3149115173290005, 6.173080972737, 6.088693295291, 5.9847732929149995, 5.876842783398, 5.899483022613, 5.8875900425120005, 5.916303933252, 5.886588537155, 5.8227127011510005, 5.734685111503, 5.713662261302, 5.685593397848, 5.7488020597839995, 5.601996126307, 5.640341849932, 5.601265584408, 5.576618718601, 5.537787247925]
# y01Down = [7.437618963727999, 7.3791717462049995, 7.303023291325001, 7.26982661854, 7.197634166936, 7.1083668578929995, 7.158186936088001, 6.985838698153, 6.958881576058, 6.955567493386, 6.9205958557919995, 6.918122337445, 6.9287044329139995, 7.080026665154999, 6.949850895980999, 6.89839463565, 6.8538805497199995, 6.846002782858999, 6.768407780941, 6.790985902007999, 6.7126455343649996, 6.474739566239, 6.2707556211919995, 6.327406558807, 6.271694338854999, 5.993654974381999, 5.862184038944, 5.698652448781, 5.519642868308999, 5.385297334109, 5.241339609534, 5.107282987196999, 5.0632979153269995, 5.064108430737999, 4.971371751666999, 4.8139435577739995, 4.7704875369, 4.686620413797999, 4.650096812713, 4.6181018726289995, 4.707761950271999, 4.701129216469999, 4.614911517329, 4.473080972737, 4.388693295291, 4.284773292914999, 4.1768427833979995, 4.199483022613, 4.187590042512, 4.216303933252, 4.186588537155, 4.122712701151, 4.034685111503, 4.013662261302, 3.985593397848, 4.048802059783999, 3.9019961263070004, 3.940341849932, 3.901265584408, 3.876618718601, 3.8377872479250006]
#
# y02Up = [10.537618963728, 10.479171746205001, 10.403023291325002, 10.36982661854, 10.297634166936, 10.208366857893001, 10.258186936088002, 10.085838698153001, 10.058881576058, 10.055567493386, 10.020595855792, 10.018122337445, 10.028704432914001, 10.180026665155, 10.049850895980999, 9.998394635650001, 9.953880549720001, 9.946002782859, 9.868407780941, 9.890985902008, 9.812645534365, 9.574739566239, 9.370755621192, 9.427406558807, 9.371694338855, 9.093654974382, 8.962184038944, 8.798652448781, 8.619642868309, 8.485297334109, 8.341339609534, 8.207282987197, 8.163297915327, 8.164108430738, 8.071371751667, 7.913943557774, 7.870487536900001, 7.7866204137979995, 7.750096812713, 7.718101872629, 7.807761950272, 7.80112921647, 7.714911517329001, 7.573080972737, 7.488693295291, 7.384773292915, 7.276842783398, 7.299483022613001, 7.287590042512001, 7.316303933252001, 7.2865885371550005, 7.222712701151001, 7.134685111503001, 7.113662261302, 7.085593397848, 7.148802059784, 7.0019961263070005, 7.040341849932, 7.001265584408, 6.976618718601, 6.937787247925001]
# y02Down = [6.337618963728, 6.279171746205, 6.203023291325001, 6.16982661854, 6.097634166936, 6.008366857893, 6.058186936088001, 5.885838698153, 5.858881576058001, 5.855567493386, 5.820595855792, 5.818122337445001, 5.828704432914, 5.980026665154999, 5.849850895981, 5.79839463565, 5.75388054972, 5.746002782859, 5.668407780941, 5.690985902007999, 5.612645534365, 5.3747395662390005, 5.170755621192, 5.227406558807, 5.171694338855, 4.893654974382, 4.762184038944, 4.598652448781, 4.419642868308999, 4.285297334109, 4.1413396095340005, 4.007282987197, 3.963297915327, 3.9641084307379995, 3.8713717516669996, 3.713943557774, 3.6704875369000005, 3.5866204137979993, 3.550096812713, 3.518101872629, 3.6077619502719998, 3.6011292164699995, 3.5149115173290006, 3.373080972737, 3.288693295291, 3.1847732929149997, 3.076842783398, 3.0994830226130006, 3.0875900425120006, 3.1163039332520004, 3.0865885371550004, 3.0227127011510007, 2.9346851115030006, 2.913662261302, 2.885593397848, 2.9488020597839997, 2.8019961263070003, 2.840341849932, 2.801265584408, 2.776618718601, 2.7377872479250005]


"""
# Also able to custom label? Number of intervals?
# Lets stick to 30%, 60%, 95%
def read_csv(csv_name, column_x, column_y, std):
    use pandas as quick way to read csv.
    returns as list column_x, column_y, std
        
"""


# Optional future params, number of intervals, color scheme (dict?), fuzziness,
# TODO: Add credential files as argument.
class FuzzyPlotly:
    def __init__(self, x_list, y_list, std_list):
        plotly.tools.set_credentials_file(username='oneGene', api_key='JvxeS4ghBsrIRKsXYfTf')
        self.x_list = x_list
        self.y_list = y_list
        self.std_list = std_list

    # function which takes in mean, std (optional configs?) and returns

    # ci is between 0-1
    # example ci = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
    def generate_interval_point(self, ci, center, std, offset=0):
        point = [ci+offset]
        boundary_point = norm.ppf(point, loc=center, scale=std)
        # print(f'point: {point}, ci: {ci}, center: {center}, std: {std}, offset: {offset} ==> boundary_point: {boundary_point}')
        return boundary_point[0]

    # Gives output Plotly can use
    def generate_y_line_data(self, ci, e_upper, e_lower):
        """
        Given CI, return x and y plotly can use.
        """
        # I need list of lower values
        # I need list of upper values
        # Put them together to feed into plotly scatter
        y_lower = []
        y_upper = []

        for i in range(len(self.y_list)):
            y_lower_point = self.generate_interval_point(ci, self.y_list[i], self.std_list[i], -e_lower)
            y_upper_point = self.generate_interval_point(ci, self.y_list[i], self.std_list[i], e_upper)
            y_lower.append(y_lower_point)
            y_upper.append(y_upper_point)

        # print(y_lower)
        # print(y_upper)

        y_plotly_values = y_lower + list(reversed(y_upper))
        return y_plotly_values

    # Note: Always same for this chart. Could add in config in plotly for labels later.
    def generate_x_line_data(self):
        return self.x_list + list(reversed(self.x_list))

    def generate_data(self):

        # Probably need to generate 1 bound with % input, iterate this to generate others

        # using input values find bounds. Puts data in a list plotly will draw area.
        # data needs to be y + reversed(y) for plotly to draw rea correctly.
        #
        self.x_values = self.x_list
        self.y_values = self.y_list
        # self.area01_x_values = self.x_list + list(reversed(self.x_list))
        # self.area02_x_values = self.x_list + list(reversed(self.x_list))
        #
        # self.area01_y_values = y01Down + list(reversed(y01Up))
        # self.area02_y_values = y02Down + list(reversed(y02Up))

    def gamma_norm(self, ci):
        # Given ci value, find opacity.
        return 1 / norm.pdf(ci)

    def plot(self):

        # simple gradient green
        fillcolor = {
            "fill01": "rgba(141,203,160, 0.8)",
            "fill02": "rgba(141,203,160, 0.5)",
            "fill03": "rgba(141,203,160, 0.2)",
        }

        # simple gradient blue
        fillcolor = {

            "fill01_fuzz": "rgba(32,74,135, 0.9)",
            "fill01": "rgba(32,74,135, 1)",

            "fill02_fuzz_up": "rgba(32,74,135, 0.8)",
            "fill02": "rgba(32,74,135, 0.65)",
            "fill02_fuzz_down": "rgba(32,74,135, 0.5)",


            "fill03_fuzz": "rgba(32,74,135, 0.35)",
            "fill03": "rgba(32,74,135, 0.2)",
            # Same

        }

        # vir
        # fillcolor = {
        #     "fill01": "#440557",
        #     "fill02": "#20908C",
        #     "fill03": "#F8E621",
        # }

        # Generate data plotly can use
        self.generate_data()

        # Create areas.

        # mean = go.Scatter(
        #     x = self.generate_x_line_data(),
        #     y = self.generate_y_line_data(0.5, 0, 0.01),
        #     mode = 'lines',
        #     name = 'mean',
        # )

        # ci = [0.025, 0.2, 0.35, 0.5, 0.65, 0.8, 0.975]
        area01 = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.8875, 0.0875, 0.08125-e+e_offset),
            mode = 'markers',
            name = '95%',
            fill='tozeroy',
            fillcolor=fillcolor["fill03"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area01_lower = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.80625, e, 0+e_offset),
            mode = 'markers',
            name = '95% lower',
            fill='tozeroy',
            fillcolor=fillcolor["fill03_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area02_upper = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.80625, 0, e+e_offset),
            mode = 'markers',
            name = '60% upper',
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_down"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        area02 = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.725, 0.08125-e, 0.1125-e+e_offset),
            mode = 'markers',
            name = '60%',
            fill='tozeroy',
            fillcolor=fillcolor["fill02"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area02_lower = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.6125, e, 0+e_offset),
            mode = 'markers',
            name = '60% lower',
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_up"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area03_upper = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.6125, 0, e+e_offset),
            mode = 'markers',
            name = '30% upper',
            fill='tozeroy',
            fillcolor= fillcolor["fill01_fuzz"],
            # fillcolor= "#AAA", #fillcolor["fill01_fuzz"]
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        area03 = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.5, 0.1125-e, 0.1125-e),
            mode = 'markers',
            name = '30%',
            fill='tozeroy',
            fillcolor=fillcolor["fill01"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )
#0.025
        e_area03_lower = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.3875, e+e_offset, 0),
            mode = 'markers',
            name = '60% lower',
            fill='tozeroy',
            fillcolor=fillcolor["fill01_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area04_upper = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.3875, 0+e_offset, e),
            mode = 'markers',
            name = '30% upper',
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_up"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        area04 = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.275, 0.1125-e+e_offset, 0.08125-e),
            mode = 'markers',
            name = '60%',
            fill='tozeroy',
            fillcolor=fillcolor["fill02"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area04_lower = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.19375, e+e_offset, 0),
            mode = 'markers',
            name = '60% lower',
            fill='tozeroy',
            fillcolor=fillcolor["fill02_fuzz_down"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        e_area05_upper = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.19375, 0+e_offset, e),
            mode = 'markers',
            name = '30% upper',
            fill='tozeroy',
            fillcolor=fillcolor["fill03_fuzz"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        area05 = go.Scatter(
            x = self.generate_x_line_data(),
            y = self.generate_y_line_data(0.1125, 0.08125-e+e_offset, 0.0875),
            mode = 'markers',
            name = '95%',
            fill='tozeroy',
            fillcolor=fillcolor["fill03"],
            hoverinfo='none',
            marker={'size': 1, 'opacity': 0},
        )

        data = [
                            area01, e_area01_lower,
            e_area02_upper, area02, e_area02_lower,
            e_area03_upper, area03, e_area03_lower,
            e_area04_upper, area04, e_area04_lower,
            e_area05_upper, area05
        ]


        # Online plotly server version. Doesn't seem to be able to turn displayModeBar off.
        # py.plot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})


        # Offline html version
        plotly.offline.plot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})


        # Jupyter notebook plot
        # init_notebook_mode(connected=True)
        # iplot(data, filename='fuzzy_dev_plt',  config={'displayModeBar': False})


my_plt = FuzzyPlotly(x_values, y_values, std)
my_plt.plot()
