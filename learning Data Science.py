# This code was originally done within Jupyter notebooks and has been copied across into a .py file
# This is to allow me to upload the code to Github to showcase
# This is because Juypter notbookes has a proprietary format

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

country_data = pd.read_csv("countries.csv")
US = country_data[country_data.country == "United States"]
China = country_data[country_data.country == "China"]

def learningGraphs():
    x = [1,2,3,8,22]
    y = [1,4,9,12,5]
    z = [5,6,7,8,10]
    plt.plot(x,y)
    plt.plot(x,z)
    plt.title("Weird Number thing")
    plt.xlabel("things")
    plt.ylabel("more things")
    plt.legend(["this is Y", "this is Z"])
    plt.show()

def usingSampleData():
    sample_data = pd.read_csv("sample_data.csv")
    x = sample_data.column_a
    y = sample_data.column_b
    z = sample_data.column_c
    plt.plot (x,y)
    plt.plot (x,z)
    plt.title("sample data")
    plt.legend(["X", "Y"])

def ChinaVsUS():
    plt.plot (US.year, US.population // 10**6)
    plt.plot (China.year, China.population // 10**6)
    plt.legend(["US", "China"])
    plt.title("US vs China Population Growth")
    plt.xlabel("year")
    plt.ylabel("population")
    plt.show

def ChinaVsUS():
    plt.style.use("ggplot")
    width = 0.8
    plt.bar (US.year, US.population / US.population.iloc[0] * 100, color = "b", label = "US")
    plt.bar (China.year + width, China.population / China.population.iloc[0] * 100, color = "r", label = "China")
    plt.title("US vs China Population Growth")
    plt.xlabel("year")
    plt.ylabel("population (first year = 100%)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("US vs China.png")
    plt.show

