import geopandas as gpd
import time
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Load the GeoJSON file into a GeoDataFrame
print("Starting read")
start_time = time.time()

gdf = gpd.read_file('FiltFireData.geojson')

end_time=time.time()
elapsed_time = end_time-start_time 
print(f"Ending Read: Time taken to read the file: {elapsed_time:.2f} seconds")
print(gdf.head())
print("Done")


gdf['NWCG_GENERAL_CAUSE'] = gdf['NWCG_GENERAL_CAUSE'].astype('category')

filtered_gdf = gdf[gdf['FIRE_SIZE']>=50].copy()

# Ensure the data is sorted by FIRE_YEAR in ascending order
filtered_gdf = filtered_gdf.sort_values(by='FIRE_YEAR')

fig = px.scatter_geo(filtered_gdf,
                     lat = 'LATITUDE',
                     lon = 'LONGITUDE',
                     color = 'NWCG_GENERAL_CAUSE',
                     size = 'FIRE_SIZE',
                     animation_frame = 'FIRE_YEAR',
                    #  animation_group = 'FIRE_NAME',
                     hover_name = 'FIRE_NAME',
                     hover_data = ['NWCG_GENERAL_CAUSE', 'FIRE_SIZE'],
                     labels = {'NWCG_GENERAL_CAUSE': 'Cause of Fire'},
                     template = 'plotly',
                     projection = "albers usa",
                     )

fig.show()



# # Update the layout to include the animation controls
# fig.update_layout(
#     title="Fires by Year",
#     geo=dict(
#         scope="usa",  # Focus on the USA
#         showland=True,
#         landcolor="white",
#         showlakes=True,
#         lakecolor="lightblue"
#     ),
#     updatemenus=[{
#         "buttons": [
#             {
#                 "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
#                 "label": "Play",
#                 "method": "animate"
#             },
#             {
#                 "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
#                 "label": "Pause",
#                 "method": "animate"
#             }
#         ],
#         "direction": "left",
#         "pad": {"r": 10, "t": 87},
#         "showactive": False,
#         "type": "buttons",
#         "x": 0.1,
#         "xanchor": "right",
#         "y": 0,
#         "yanchor": "top"
#     }]
# )


# fig.update_traces(
#     hovertemplate=(
#         'Fire Name: %{hovertext}<br>' # name of fire
#         'Cause: %{customdata[0]}<br>' # Cause of fire
#         'Size: %{marker.size} acres<br>' # size of fire
#         'Latitude: %{lat}<br>' #latitude
#         'Longitude: %{lon}<br>' #longitude
#     )
# )


# fig.update_layout(
#     updatemenus=[dict(
#         type='buttons',
#         x=0.1,
#         y=-0.1,
#         showactive=False,
#         buttons=[dict(label='Play',
#                       method='animate',
#                       args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)])])]
# )

new_end_time=time.time()
new_elapsed_time = new_end_time-start_time 
print(f"Time taken to SHOW the file: {new_elapsed_time:.2f} seconds")
