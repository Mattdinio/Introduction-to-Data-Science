# This code was originally done within Jupyter notebooks and has been copied across into a .py file
# This is to allow me to upload the code to Github to showcase
# This is because Juypter notbookes has a proprietary format

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
from datetime import date
labels = ["unworked", "break", "worked"]
colours = ["Red","Blue","Green" ]

def hourTracking():
    normalHours = 8.00 #total number of hours worked by employee
    worked = 5 # how long they marked as working
    breakTime = 1 #how much they marked as break
    actualHours = worked + breakTime #combined hours of work and breaks
    if actualHours < normalHours: #check if actual hours is less than what they should have worked
        actualHours = normalHours #if true use normal hours
    unWorked = actualHours - (worked+breakTime)
    if unWorked < 0:
        unWorked = 0
    values = [unWorked,breakTime, worked]
    workPie = plt.pie (values, labels=labels, colors=colours,
    autopct='%1.1f%%', shadow=True, startangle=90)
    #draw circle
    centre_circle = plt.Circle((0,0),0.8,fc="white")
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    today = date.today()
    plt.title(today.strftime("%d %B %Y"))
    plt.show()