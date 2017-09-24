import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")
def colorget(Elevation):

    if Elevation>3000.0:
        print(Elevation)
        return "red"
    if Elevation >=1000.0 and Elevation<=3000.0:
        return "orange"
    return "green"
fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, nm, el in zip(lat,lon,name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], fill= True, popup=folium.Popup(nm + " Elevation: " + str(el) + " m",parse_html =True), color=colorget(el)))



fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = "utf-8-sig").read(),style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if x['properties']["POP2005"]<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
