from firebase import firebase
import numpy as np
import gmplot
import cv2
# import webbrowser
gaba=gmplot.GoogleMapPlotter(28.667449,77.228249,zoom=15)
# from flask import Flask,render_template
#
from time import sleep
import pickle
import os
#
# from keras.models import model_from_json
#
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("model.h5")
#


#
def plot_1(lati,long):
    gaba.heatmap(lati,long)
    # gaba.plot(lati,long)

    gaba.draw('templates/heat_map.html')

# app.run(debug=True)

from urllib.request import urlretrieve
firebase_1 = firebase.FirebaseApplication('https://androidfirebase-62b80.firebaseio.com', None)
lat=[]
lon=[]
count=0


while(1):


    gulab=firebase_1.get('/',None)
    # if(count==0):
    #     count=len(gulab)-2

    intensity=1
# print(len(gulab))
    n=len(gulab)-2

    if(count==n):
        continue
    # print(n)
    else:
        values_1=list(gulab.values())[n]
        count=len(gulab)-2
        array = values_1.values()
        list_1 = list(array)
        lat.append(list_1[1])
        lon.append(list_1[2])
        print(lat)
        print(lon)
        # plot_1(lati=lat,long=lon)
        url=list_1[4]
        name_f='okepic.jpg'
        urlretrieve(url,name_f)
        img = cv2.imread('okepic.jpg')
        #sleep(3)
        with open('predict_1.pickle', 'rb') as f:
            y_pred = pickle.load(f)
        print(y_pred)
        try:
            os.remove('okepic.jpg')
        except:
            pass
        if(y_pred[0][0]==1):
            intensity=1
        elif(y_pred[0][1]==1):
            intensity=7
        else:
            intensity=10
        for i in range(0,intensity):
            lat.append(lat[-1]+0.000001)
            lon.append(lon[-1]+0.000001)
        plot_1(lat,lon)
















