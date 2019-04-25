#import yt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

# Read data from mesa data: 
a = pd.read_excel("data/ONe6040_update.xlsx")

r_sun = 6.955e10  # cm
radius = np.array(a["radius"])

temp = np.array(a["temperature"])
plt.plot(radius*r_sun, temp, label = 'MESA')
plt.xlabel("Radius [cm]")
plt.ylabel("Temperature [K]")
#plt.ylim(1e5,1e13)
plt.xlim(0,1.5e8)
plt.grid()
plt.legend()
plt.savefig("temp.png")
