
import folium
import pandas as pd


def create_map(plot_coordinates, map_filename):

    """saves a map with the latitude, longitude coordinates plotted"""

    latitudes, longitudes = zip(*plot_coordinates)

    m = folium.Map(tiles='Esri.WorldImagery')
    min_lat = min(latitudes)
    max_lat = max(latitudes)
    min_lon = min(longitudes)
    max_lon = max(longitudes)
    m.fit_bounds([[min_lat, min_lon], [max_lat, max_lon]])
    folium.PolyLine(plot_coordinates, color='blue', weight=2, opacity=0.7).add_to(m)

    m.save(map_filename)


# this is the real-time gps data from sensorlogger
gps_output = pd.read_csv(r"sensorlogger output\Location.csv")
gps_coordinates = list(zip(gps_output.latitude, gps_output.longitude))
create_map(gps_coordinates, 'gps_map.html')

# this is the post-processed ppp data from https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php
ppp_output = pd.read_csv(r"rncan full_output\gnss_log_2025_02_26_09_01_38.csv")
ppp_coordinates = list(zip(ppp_output.latitude_decimal_degree, ppp_output.longitude_decimal_degree))
create_map(ppp_coordinates, 'ppp_map.html')