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

    return {"Q1": round(Q1,2), "Q2": round(Q2,2), "Q3": round(Q3, 2)}

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
    #print("Using updated correlation function") 
    if len(x) != len(y):
        raise ValueError("Lists must be the same length.")
    
    cov = covariance(x, y)
    devX = standardDeviation(x)
    devY = standardDeviation(y)
    return cov / (devX * devY)

#regression parameters
def regression_slope(x, y):
    mean_x = arithmeticMean(x)
    return covariance(x, y) / sum((xi - mean_x) ** 2 for xi in x)

def regression_intercept(x, y):
    return arithmeticMean(y) - regression_slope(x, y) * arithmeticMean(x)

def regression_line(x, y):
    slope = regression_slope(x, y)
    intercept = regression_intercept(x, y)
    return f"y = {slope:.4f} * x + {intercept:.4f}"


# Regression predictions
def predicted_values(x, y):
    slope = regression_slope(x, y)
    intercept = regression_intercept(x, y)
    return [slope * xi + intercept for xi in x]

# Total variation
def total_variation(y):
    mean_y = arithmeticMean(y)
    total_variation = sum((yi - mean_y) ** 2 for yi in y)
    return total_variation

# Explained variation
def explained_variation(x, y):
    mean_y = arithmeticMean(y)
    y_hat = predicted_values(x, y)
    explained_variation = sum((yhi - mean_y) ** 2 for yhi in y_hat)
    return explained_variation

# Unexplained variation
def unexplained_variation(x, y):
    y_hat = predicted_values(x, y)
    unexplained_variation = sum((y[i] - y_hat[i]) ** 2 for i in range(len(y)))
    return unexplained_variation

# Mean Squared Error
def mean_squared_error(x, y):
    y_hat = predicted_values(x, y)
    mse = sum((y[i] - y_hat[i]) ** 2 for i in range(len(y))) / len(y)
    return mse

# R-squared
def r_squared(x, y):
    ss_total = total_variation(y)
    ss_residual = unexplained_variation(x, y)
    r2 = 1 - (ss_residual / ss_total)
    return r2

