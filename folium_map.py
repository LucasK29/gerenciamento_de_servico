from geopy import Nominatim
from folium.plugins import MarkerCluster 

import folium
import folium_map_html
import branca

def plot_map(df):

    geolocator = Nominatim(user_agent="geolocation")

    map = folium.Map(location=[df['lat'].mean(), df['long'].mean()], zoom_start=13)
    marker_cluster = MarkerCluster().add_to(map)

    for i, row in df.iterrows():
        html = folium_map_html.popup_html(i,df)
        popup = folium.Popup(html, max_width=600, parse_html=False, show=False, sticky=False)
        folium.Marker([row['lat'],row['long']],
        popup=popup,icon=folium.Icon(color="blue", icon='university', prefix='fa')).add_to(map)  
    return map  