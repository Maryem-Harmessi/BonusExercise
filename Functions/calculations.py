import math
import statistics

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
    dataS = sorted(data)
    n = len(dataS)

    Q2 = statistics.median(dataS)

    if n % 2 == 0:
        lower_half = dataS[:n // 2]
        upper_half = dataS[n // 2:]
    else:
        lower_half = dataS[:n // 2]
        upper_half = dataS[n // 2 + 1:]

    Q1 = statistics.median(lower_half)
    Q3 = statistics.median(upper_half)

    return {"Q1": Q1, "Q2": Q2, "Q3": Q3}

#covariance
def covariance(x,y):
    if len(x) != len(y):
        raise ValueError("Both lists must have the same length.")
    
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n
    return cov
    
#correlation
def correlation(x, y):
    print("Using updated correlation function") 
    if len(x) != len(y):
        raise ValueError("Lists must be the same length.")
    
    cov = covariance(x, y)
    devX = standardDeviation(x)
    devY = standardDeviation(y)
    return cov / (devX * devY)



   
