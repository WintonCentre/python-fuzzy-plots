# Uncertainty Plots with python and plotly.
Fan charts and their variations explored by the Winton Centre for Risk and Evidence Communication. Similar to fan chart by Office for National Statistics. Take a look at [jupyter notebook examples](examples/unemployment_example.ipynb) to see the usage.

Solid fan chart example
![Fan plot](example_images/03-fan.png)

Standard error chart example
![Standard error plot](example_images/02-ci.png)

Density chart example
![Density plot](example_images/01-dens.png)

Fuzzy fan chart example
![Fuzzy fan plot](example_images/04-fuzzy-fan.png)

Fuzzy fan - Zoomed
![Fuzzy fan plot](example_images/04.1-zoomed.png)


## Prerequisites
Python 3.4+

## Usage and Examples - Jupyter Notebook
Best way to see usage is through the [jupyter notebook examples](examples/unemployment_example.ipynb).

To access a local editable copy in Jupyter notebooks, you may need to install Jupyter first.
In a terminal:
```
pip install jupyter

jupyter notebook
``` 

## Getting started

### (Optional, but recommended) - Create virtual environment.
_1. Go to project directory_

_2. Create a virtual environment_

In terminal: 
`python3 -m venv .venv`

_3. Activate virtual environment_

In terminal: 
`. .venv/bin/activate`


### Installation

Install this module using pip.
In terminal type: `pip install .`
 
 (TODO FUTURE: `pip install fuzzyplots`)

### Usage

#### Basic Plot

Within Jupyter or a python file, start with the code below.
Fanplotly generates a Plotly fan chart using parameters which are described below.
```
# Import the module
from fuzzy.core import FanPlotly

solid_ci = FanPlotly(
    x, y_median,
    ci95p=y_p_95, ci95n=y_n_95,
    ci60p=y_p_60, ci60n=y_n_60,
    ci30p=y_p_30, ci30n=y_n_30,
)

# Plot
solid_ci.plot()

```
We first create an instance of the FanPlotly class, and then call its plot method to generate the chart.

Execute the code to see the chart.

## Classes

There are a number of python classes for the various possible chart types. 

### Solid Fan chart
`FanPlotly(x, y, ci95p, ci95n, ci60p, ci60n, ci30p, ci30n, fuzz_size, color_levels, color='#4286f4', median_line=True, median_line_color='#000000', median_line_width=1, layout={'showlegend': False}, figs=[], output='auto')`

Required parameters:
- x: x-axis values in a list.
- y: y-axis median values in a list.
- ci95p: Upper values of 95% confidence interval in a list.
- ci95n: Lower values of 95% confidence interval in a list.
- ci60p: Upper values of 60% confidence interval in a list.
- ci60n: Lower values of 60% confidence interval in a list.
- ci30p: Upper values of 30% confidence interval in a list.
- ci30n: Lower values of 30% confidence interval in a list.

### Density chart

`DensPlotly(x, y, ci95p, ci95n, color_levels, color='#4286f4', median_line=True, median_line_color='#000000', median_line_width=1, layout={'showlegend': False}, figs=[], output='auto')`

Required parameters:
- x: x-axis values in a list.
- y: y-axis median values in a list.
- ci95p: Upper values of 95% confidence interval in a list.
- ci95n: Lower values of 95% confidence interval in a list.
- color_levels: The number of colour levels used to indicate the likely value as a density. Takes an integer value between 1-150. Recommend least 20 to make make colour changes smooth.


### Standard error chart

`StandardErrorPlot(x, y, ci95p, ci95n, color_levels, color='#4286f4', median_line=True, median_line_color='#000000', median_line_width=1, layout={'showlegend': False}, figs=[], output='auto')`

Required parameters:
- x: x-axis values in a list.
- y: y-axis median values in a list.
- ci95p: Upper values of 95% confidence interval in a list.
- ci95n: Lower values of 95% confidence interval in a list.


### Fuzzy fan chart
For some applications, it may be preferable to blur the boundaries between the fans. 
--Add justification of this--

`FuzzyPlotly(x, y, ci95p, ci95n, ci60p, ci60n, ci30p, ci30n, fuzz_size, color_levels, color='#4286f4', median_line=True, median_line_color='#000000', median_line_width=1, layout={'showlegend': False}, figs=[], output='auto')`

Required parameters:
- x: x-axis values in a list.
- y: y-axis median values in a list.
- ci95p: Upper values of 95% confidence interval in a list.
- ci95n: Lower values of 95% confidence interval in a list.
- ci60p: Upper values of 60% confidence interval in a list.
- ci60n: Lower values of 60% confidence interval in a list.
- ci30p: Upper values of 30% confidence interval in a list.
- ci30n: Lower values of 30% confidence interval in a list.
- fuzz_size: The width of the blurring. Takes integer value between 0-1.
- color_levels: The number of colour levels used to implement the blur. Takes integer value between 1-150. Recommend least 15 to make make colour changes smooth.

### Shared optional parameters.

- color: The colour of the highest density band given as a hex value in string. The default value is #4286f4. Lower density colours are calculated from this value,
- layout: [Plotly layout](https://plot.ly/python/reference/#layout) - an object to configure the layout of the chart.
- median_line: True/False to enable or disable median line. Default value is True.
- median_line_color: Colour of the median line. Takes a hex value in string. The default value is #000000 (black).
- median_line_width: Thickness of the median line. Takes an integer. The default value is 1.
- figs: Takes in plotly data structures to add additional charts. Pass in as a list if there are multiple figures to plot.


## Other Options

### Plotting options
FuzzyPlotly supports offline, online, and jupyter notebooks. It automatically defaults to offline mode and detect running of jupyter notebook (ipython).

Possible parameters for output are "auto", "offline", "online", "jupyter"

##### Auto
"auto" is is the value used when output parameter isn't given by an user. 
FuzzyPlot will switch between offline and jupyter notebook mode depending on the user's running environment.

`dens_plot = DensPlotly(x=x, y=y_median, ci95p=y_p_95, ci95n=y_n_95, color_levels=30)`

##### Offline
By default this mode will be used unless it is being run inside of jupyter notebook.
If output="offline" is set within jupyter, it will open a browser pointing to an html page containing the plot.

`dens_plot = DensPlotly(x=x, y=y_median, ci95p=y_p_95, ci95n=y_n_95, color_levels=30, output='offline')`

##### Jupyter Notebook
Passing jupyter will force FuzzyPlotly to use plot option for jupyter notebook. Not normally necessary.

`dens_plot = DensPlotly(x=x, y=y_median, ci95p=y_p_95, ci95n=y_n_95, color_levels=30, output='jupyter')`

##### Online
To use online mode please sign up on the Plotly web site and obtain add your username/api key from the settings page. 

`plotly.tools.set_credentials_file(username='jack89', api_key='qwfw32EW3twqkitdf')`

`dens_plot = DensPlotly(x=x, y=y_median, ci95p=y_p_95, ci95n=y_n_95, color_levels=30, output='online')`

(Refer to the plotly documentation for addition information.
 https://plot.ly/python/configuration-options/
)

## Labeling
Pass in a plotly layout object to configure titles, labels, and fonts.


```
# Create layout
layout = go.Layout(
    title='Unemployment between 2012 and 2017',
    xaxis=dict(
        title='Dates',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Unemployment rate',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

FuzzyPlotly(x_sample_values, y_sample_values, std, layout=layout).plot()

```
