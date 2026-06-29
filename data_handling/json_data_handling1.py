import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data_handling/readablejson.json'

with open(filename, 'r', encoding='utf-8') as f:
    data1 = json.load(f)
    filter_data = data1['features']
    magnitudes, longitude, latitude , titles = [], [], [] ,[]
    
    for gdata in filter_data:
        d = gdata['properties']['mag']
        coords = gdata['geometry']['coordinates']
        t = gdata['properties']['title']
        # Skip if missing data
        if d is None or coords is None or t is None or len(coords) < 2:
            continue
            
        long = coords[0]
        lati = coords[1]
        
        if long is None or lati is None:
            continue
            
        magnitudes.append(d)
        longitude.append(long)
        latitude.append(lati)
        titles.append(t)

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': longitude,
    'lat': latitude,
    'text': titles,
    'marker': {
        # If magnitude is negative or zero, give it a default small size of 1
        'size': [5 * mag if mag > 0 else 1 for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
