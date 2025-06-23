import math
import pandas as pd

## arithmetic mean
def arithmeticMean(data): return sum(data)/len(data)

## variance
def variance(data):
    n=len(data)
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / n

##standard deviation
def standardDeviation(data):
    return math.sqrt(variance(data))


##quartiles 
def quartiles(data):
     n=len(data)
     dataS = sorted(data)
     Q1=math.median(dataS)
     if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
     else:
        lower_half = data[:n // 2]
        upper_half = data[n // 2 + 1:]
     Q1 =math.median(lower_half)
     Q3 =math.median(upper_half)


   
