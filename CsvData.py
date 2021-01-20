# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mylib

csv_config = 'climateSensorDay_Night.csv'
weather_data = pd.read_csv(csv_config)
print(weather_data)

weather_array = weather_data.values
print("numpy array of first data point:", \
      weather_array[0])

time0humidity = weather_array[0,1]
print(time0humidity)

####################################################################################
# Great!
# 
# TODO: Now we know how to grab a specific time 
# point's array of data, or even a specific 
# category of its data. But what if we want to 
# look at a specific category across time points? 
# Try and build a 1 Dimensional Array (just a 
# simple numpy array) containing humidity across 
# all timepoints!
####################################################################################


####################################################################################
# There's got to be a simpler way, right?
#
# There is! Let's talk a bit about colons -- 
# colons give you the power to specify multiple 
# rows or columns, depending on the axis you 
# apply them on. For example, calling 
# *weather_array[: , 2]* should give you data 
# for temperature (second column) across **all** 
# rows. The code basically calls 
# *weather_array[row, 2]* while filling in the 
# *row* spot for you.
#
# Calling *weather_array[0, :]* will give you all
# the categorical data in the first row -- it is 
# essentially the same information as calling 
# *weather_array[0]*. 
# 
# TODO: Try it yourself!
####################################################################################


####################################################################################
# Data Visualization
#
# What's the point of having data if you can't 
# interpret it? Let's look at ways we can plot 
# our data, to make it more readable both for 
# ourselves and others.
####################################################################################

# TODO: Using mylib.line_plots, plot the humidity
# and temperature in the CSV over time.

humidity = weather_array[:,1]
temperature = weather_array[:,2]
data_arr = [humidity, temperature]
labels = ["humidity", "temperature"]
time = weather_array[:,0]
mylib.line_plots(time, data_arr, labels)

####################################################################################
# Data Visualization Part 2
#
# Lets look at deviation of temperature from the mean, so we can get a better sense of
# the variance!
####################################################################################
# To find the average temperature, we may simply call numpy's mean() method on 
# the array. Then, we may subtract it from the original array, which will then
# go through and apply that subtraction to each element of the array. Thus, we
# are left with an array of deviations from the average.
temp = weather_array[:,2]
average_temp = temp.mean()
normalized_temp = temp - average_temp

# Plotting the deviation of temperature, removing tick marks on the x axis to
# improve readability.
mylib.bar_plots(time, [normalized_temp], ["avg temp"])