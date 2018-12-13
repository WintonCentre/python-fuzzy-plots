# Python Fuzzy Plots
Fuzzy Plots using python and plotly showing uncertainty. Similar to (x chart?) by Office for National Statistics.
(TODO: insert pic)

Creates fuzzy boundaries around confidence interval at 30%, 60%, 95%.

## Prerequisites
Python 3.4+

## Quick start
Import module and use sample values to create a plot.

In terminal type
`pip install .`

Create a file "example.py" with the code below
```
# Import the module
from fuzzy.fuzzy_main import FuzzyPlotly, x_sample_values, y_sample_values, std

# Create a plot using sample values.
my_plt = FuzzyPlotly(x_sample_values, y_sample_values, std)
my_plt.plot()
```
In terminal execute the file.

`python example.py`

## Jupyter Notebook
Fastest way to see examples are to startup jupyer notebook and running "sample.ipynb" provided.

In terminal:
```
pip install jupyter

jupyter notebook
``` 

## Getting started

### (Optional) - Create virtual environment.
_1. Go to project directory_

_2. Create a virtual environment_

In terminal: 
`python3 -m venv .venv`

_3. Activate virtual environment_

In terminal: 
`. .venv/bin/activate`


### Installation

Install module using pip.
In terminal type: `pip install .`
 
 (TODO FUTURE: `pip install fuzzyplots`)

### Usage

#### Running

Create a file "example.py" with the code below
```
# Import the module
from fuzzy.fuzzy_main import FuzzyPlotly, x_sample_values, y_sample_values, std

# Create a plot using sample values.
my_plt = FuzzyPlotly(x_sample_values, y_sample_values, std)
my_plt.plot()
```
In terminal execute the file.

`python example.py`

#### Basic Plot
FuzzyPlotly(x_list, y_list, std_list, figs=[], output='auto')

x_list, y_list, std_list are list values to plot.

`FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2]).plot()`

#### Additional plot
FuzzyPlotly allows user to add any plots plotly supports.

```
# First create a plotly figure
new_fig_1 = {
         'marker': {'color': 'red', 'size': 10, 'symbol': 104},
         'mode': 'markers+lines',
         'name': '1st Trace',
         'text': ['one', 'two', 'three'],
         'type': 'scatter',
         'x': [1, 2, 3],
         'y': [4, 2, 1]
     }

# Create another plotly figure (Optional)
new_fig_2 = {
         'marker': {'color': 'red', 'size': 10, 'symbol': 104},
         'mode': 'markers+lines',
         'name': '1st Trace',
         'text': ['one', 'two', 'three'],
         'type': 'scatter',
         'x': [5, 6, 7],
         'y': [3, 4, 1]
     }
```

##### Additional plot - Method 1
figs allow user to add additional plot(s). Pass it as list to figs.

```
# Pass plots created above as parameter to figs
my_plt = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2], figs=[new_fig_1, new_fig_2])
my_plt.plot()
```

##### Additional plot - Method 2
Alternatively user can simple take out plotly data structure FuzzyPlotly has generated using .data() method plot it standard plotly way.

```
# Get fuzzy data through .data() method
fuzzy_data = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2]).data()

# Append additional plot(s) to the list
my_data = fuzzy_data + [new_fig_1, new_fig_2]

# Plot using plotly
plotly.offline.plot(data, filename='fuzzy_dev_plt')

```

#### Plotting options
FuzzyPlotly supports offline, online and jupyter notebook. It automatically defaults to offline mode and detect running of jupyter notebook (ipython).

Possible parameters for output are "default", "offline", "online", "jupyter"

##### Offline
By default this mode will be used unless it is being run inside of jupyter notebook.

`fuzzy_data = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2], output='offline')`

##### Jupyter Notebook
User shouldn't need to pass this value. Passing jupyter will force FuzzyPlotly to use plot option for jupyter notebook.

`fuzzy_data = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2], output='jupyter')`

##### Online
To use online mode please add your username/api key from plot.ly at start and run the code.

`plotly.tools.set_credentials_file(username='jack89', api_key='qwfw32EW3twqkitdf')`

`fuzzy_data = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2], output='online')`

(Refer to plotly documentation for addition information.
 https://plot.ly/python/configuration-options/
)

# Authors

# License
