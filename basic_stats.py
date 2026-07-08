import numpy as np
from scipy import stats

class Basic_Stats:
    def __init__(self,data,mean,median,mode,variance,std_dev,max,min):
        self.data=data
        self.mean=mean
        self.median=median
        self.mode=mode
        self.variance=variance
        self.std_dev=std_dev
        self.max=max
        self.min=min

"""This ensures users enter the correct data type and format for the basic statistics 
calculations. It prompts the user to input their data as a comma-separated string, which 
is then converted into a list of floats for further analysis. The class also includes methods
to calculate various statistical measures such as mean, median, mode, variance, standard 
deviation, maximum, and minimum values from the provided data."""
def get_data(self):
    self.data=input("Please enter your data separated by commas: ")
    self.data=[float(x) for x in self.data.split(",")]

def mean(self,data):
    self.mean=np.mean(data)
    return self.mean

def median(self,data):
    self.median=np.median(data)
    return self.median

def mode(self,data):
    self.mode=stats.mode(data, keepdims=True).mode[0]
    return self.mode

def variance(self,data):
    self.variance=np.var(data)
    return self.variance    

def std_dev(self,data):
    self.std_dev=np.std(data)
    return self.std_dev

def max(self,data):
    self.max=np.max(data)
    return self.max

def min(self,data):
    self.min=np.min(data)
    return self.min

def display_stats(self):
    print(f"Mean: {self.mean}")
    print(f"Median: {self.median}")
    print(f"Mode: {self.mode}")
    print(f"Variance: {self.variance}")
    print(f"Standard Deviation: {self.std_dev}")
    print(f"Maximum: {self.max}")
    print(f"Minimum: {self.min}")