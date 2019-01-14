# Uncertainty Plots with python and plotly.
Fan charts and their variations explored by the Winton Centre for Risk and Evidence Communication. Similar to fan chart by Office for National Statistics.



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
from fuzzy.core import StandardErrorPlot

standard_error = StandardErrorPlot(
    x, y_median,
    ci95p=y_p_95, ci95n=y_n_95,
    layout=layout,
)

standard_error.plot()
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

## Other Options

### Plotting options
FuzzyPlotly supports offline, online and jupyter notebook. It automatically defaults to offline mode and detect running of jupyter notebook (ipython).

Possible parameters for output are "auto", "offline", "online", "jupyter"

##### Auto
"auto" is is the value used when output parameter isn't given by an user.
FuzzyPlot will try to figure out user's running environment and automatically pick best setting.

`fuzzy_data = FuzzyPlotly([1,2,3,4,5], [2,6,8,6,5], [1,2,3,2,2])`

##### Offline
By default this mode will be used unless it is being run inside of jupyter notebook.
If output="offline" is set within jupyter html page with plot will be generated and opened.

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

### Axis
#### Date time


(TODO: There was more python related site???)
Use dateutil module to convert to plotly friendly format. 
https://help.plot.ly/date-format-and-time-series/

Please refer to https://stackabuse.com/converting-strings-to-datetime-in-python/

```
from dateutil.parser import parse

date_array = [  
    '2018-06-29 08:15:27.243860',
    'Jun 28 2018  7:40AM',
    'Jun 28 2018 at 7:40AM',
    'September 18, 2017, 22:19:55',
    'Sun, 05/12/1999, 12:30PM',
    'Mon, 21 March, 2015',
    '2018-03-12T10:12:45Z',
    '2018-06-29 17:08:00.586525+00:00',
    '2018-06-29 17:08:00.586525+05:00',
    'Tuesday , 6th September, 2017 at 4:30pm'
]

for date in date_array:  
    print('Parsing: ' + date)
    dt = parse(date)
    print(dt.date())
    print(dt.time())
    print(dt.tzinfo)
    print('\n')
```
Output: 
```
$ python3 dateutil-1.py
Parsing: 2018-06-29 08:15:27.243860  
2018-06-29  
08:15:27.243860  
None

Parsing: Jun 28 2018  7:40AM  
2018-06-28  
07:40:00  
None

Parsing: Jun 28 2018 at 7:40AM  
2018-06-28  
07:40:00  
None

Parsing: September 18, 2017, 22:19:55  
2017-09-18  
22:19:55  
None

Parsing: Sun, 05/12/1999, 12:30PM  
1999-05-12  
12:30:00  
None

Parsing: Mon, 21 March, 2015  
2015-03-21  
00:00:00  
None

Parsing: 2018-03-12T10:12:45Z  
2018-03-12  
10:12:45  
tzutc()

Parsing: 2018-06-29 17:08:00.586525+00:00  
2018-06-29  
17:08:00.586525  
tzutc()

Parsing: 2018-06-29 17:08:00.586525+05:00  
2018-06-29  
17:08:00.586525  
tzoffset(None, 18000)

Parsing: Tuesday , 6th September, 2017 at 4:30pm  
2017-09-06  
16:30:00  
None  
```

## Labeling
Pass in plotly layout to customize figure including labels.


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

# Authors

# License
