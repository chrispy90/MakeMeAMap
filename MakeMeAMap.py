from Tkinter import *
import folium
import geocoder


''' This program can only geocode cities in the United States

    Makes a HTML document in the same directory as this script 

'''

basemaps = ["OpenStreetMap","MapQuest Open","MapQuest Open Aerial",
            "Mapbox Bright","Mapbox Control Room","CartoDB dark_matter",
            "CartoDB positron", "Stamen Terrain","Stamen Toner",
            "Stamen Watercolor"]

states = ["AL",
          "AK",
          "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

master = Tk()

master.title("Make me a Map!")


Label(master, text="Pick a map").grid(row=0)
Label(master, text="City").grid(row=1)
Label(master, text="State").grid(row=2)

#e1 = Entry(master)
userCity = Entry(master)

#e1.grid(row=0, column=1)
userCity.grid(row=1, column=1)

var1 = StringVar(master)
var1.set(basemaps[8]) # initial value

option1 = apply(OptionMenu, (master, var1) + tuple(basemaps))
option1.grid(row=0, column=1)

var2 = StringVar(master)
var2.set(states[0]) # initial value

option2 = apply(OptionMenu, (master, var2) + tuple(states))
option2.grid(row=2, column=1)

#
# test stuff

def makeMap(city, state, basemap):
    userPlace = city+", "+state
    g = geocoder.google(userPlace)
    x = g.lat
    y = g.lng

    xxx = geocoder.google([x,y], method='reverse')

    cityName  = xxx.city


    mappy = folium.Map(location=[x,y],
                       tiles = basemap,
                       zoom_start = 13)
                       
    folium.Marker([x,y], popup= cityName).add_to(mappy)


    mappy.save('YourMap.html')

def ok():
    print "Basemap: ", var1.get()
    print "City: ", userCity.get()
    print "State: ", var2.get()
    base = var1.get()
    city = userCity.get()
    state = var2.get()
    makeMap(city,state,base)
    

button = Button(master, text="OK", command=ok)
button.grid(row=5, column=0)

mainloop()
