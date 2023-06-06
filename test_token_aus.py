import pandas as pd
import plotly.express as px

# token = open("../mapbox/token.txt").read()

# us_cities = pd.read_csv(
#     # "https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv"
#     "../data/us-cities-top-1k.csv"
# )

aus_hail = pd.read_csv(
    './hail-australia-2003-2023.csv'
)

# usa_hail = pd.read_csv(
#     '../data/USA_1955-2021_hail.csv'
# )

fig = px.density_mapbox(
    aus_hail,
    lat = 'Latitude',
    lon = 'Longitude',
    z = 'Hail size',
    radius = 30,
    # hover_name='City',
    hover_data=['Hail size', 'Date/Time'],
    # color_discrete_sequence=['fuchsia'],

    # usa_hail,
    # lat = 'slat',
    # lon = 'slon',
    # z = 'mag',
    # radius = 4,
    # hover_data=['mag', 'yr'],

    zoom=4,
    height=1000,
)

fig.update_layout(
    mapbox_style='open-street-map',
    # mapbox_style='light',
    # mapbox_accesstoken=token
)

fig.update_layout(
    margin={
        'r': 0,
        't': 0,
        'l': 0,
        'b': 0
    }
)

aus_solar = pd.read_csv(
    './solar farms in australia.csv'
).fillna(0)

# usa_solar = pd.read_csv(
#     '../data/USA_Global-Solar-Power-Tracker-May-2022.csv'
# ).fillna(0)

fig2 = px.scatter_mapbox(
    aus_solar,
    lat = 'latitude',
    lon = 'longitude',
    size = 'DC Capacity (MWp)',
    hover_data = ['Project/', 'DC Capacity (MWp)'],

    # usa_solar,
    # lat = 'Latitude',
    # lon = 'Longitude',
    # size = 'Capacity (MW)',
    # hover_data = ['Project Name', 'Capacity (MW)'],
)

fig2.update_traces(
    marker = dict(
        color = 'red',
    )
)

fig.add_trace(fig2.data[0])

fig.show()

