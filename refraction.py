# file to get data for all the refractive values.
from math import sin, asin, pi, radians
import csv

def get_uncertainty(i, r, u1=0, u2=0):
    v1 = sin(radians(i+u1))/sin(radians(r-u2))
    v2 = sin(radians(i-u1))/sin(radians(r+u2))
    return i, r, min(v2, v1)+(v1-v2)/2, (v1-v2)/2

def dgs(rads):
    return rads * 360/ (2*pi)

def get_many(vals, ri, u1, u2):
    # ri = sin(i)/sin(r)
    output = []
    for i in vals:
        r = round(dgs(asin(sin(radians(i))/ri)))
        try:
            output.append(get_uncertainty(i, r, u1, u2))
        except:
            output.append([i, r, None, None])
    # print("Values:")
    return output


data = get_many([*range(91)], 4/3, 0.5, 0.5)  # The Uncertainties are the last two values.
with open("values1.txt", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Angle of Incidence", "Angle of Refraction", "Refractive Index", "Uncertainty"])
    writer.writerows(data)

