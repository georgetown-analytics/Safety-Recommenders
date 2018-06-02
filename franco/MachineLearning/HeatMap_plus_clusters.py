from HeatMap import *

COORDINATES = (38.904722, -77.016389)
crimedata = pd.read_csv('test2.csv')

# general heatmap LayerControl

#crimedata2 = pd.read_csv('DC_Crime_Official.csv')
crimedata['latitude'] = list(crimedata['latitude'].astype(float))
crimedata['longitude'] = list(crimedata['longitude'].astype(float))



#map = folium.Map(location=COORDINATES, zoom_start=12)

#################################################33 cluster layer#################################################################3

my_marker_cluster1 = folium.plugins.MarkerCluster(name = "Offenses").add_to(map)

for i, j, k, l, m in zip(crimedata['latitude'][0:1000], crimedata['longitude'][0:1000], crimedata['offense_text'][0:1000], crimedata['start_date'][0:1000], crimedata['method'][0:1000]):
    if k == 'motor vehicle theft':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True , radius = 5, color = 'green', fill_color ='green').add_to(my_marker_cluster1)
    elif k == 'theft':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'blue', fill_color ='blue').add_to(my_marker_cluster1)
    elif k == 'auto theft':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'darkgreen', fill_color ='darkgreen').add_to(my_marker_cluster1)
    elif k == 'burglary':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'purple', fill_color ='purple').add_to(my_marker_cluster1)
    elif k == 'arson':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'yellow', fill_color ='yellow').add_to(my_marker_cluster1)
    elif k == 'assault with weapon':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'pink', fill_color ='pink').add_to(my_marker_cluster1)
    elif k == 'homicide':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'black', fill_color ='black').add_to(my_marker_cluster1)
    elif k == 'sex abuse':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'red', fill_color ='red').add_to(my_marker_cluster1)
    elif k == 'robbery':
        folium.CircleMarker([i,j], popup='Offense: '+k+'<br>'+'Date/Hour: '+l+'<br>'+'Method : '+m, fill_opacity=0.7, fill=True, radius = 5, color = 'orange', fill_color ='orange').add_to(my_marker_cluster1)




######## restaurant points layer #############################


folium.LayerControl().add_to(map)
map.save('maptest1.html')
