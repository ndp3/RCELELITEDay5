#The required libs must be imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler

def get_data(filename):
  """
  get_data - collect real time data from sensor 
  device .csv file.
  
  input: filename - the name of the csv file we 
            want to grab data from.
  output: training_data - a numpy array of arrays 
            containing the data we are interested 
            in manipulating.
  """
  df = pd.read_csv(filename, usecols=np.arange(0,7)) 
  print(df)
  # see https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
  df.drop(['Index','TimeStamp'], axis=1, inplace=True)    
  return df

def columnToRow(inputArray, index):
  """
  columnToRow - grab a column from the csv we 
                have and turn it into its own 
                row array of data.
                
  input:  inputArray - the numpy array of csv 
            data we can easily grab from.
          index - the column index we're 
            interested in (i.e. 0 for humidity, 
            etc.)
  output: columnArray - the array of categorical 
            data from one column
  """
  
  thisArray = np.array([])
  for a in inputArray:
    thisArray = np.append(thisArray, a[index])
    print(inputArray[index])
  return thisArray  
  
  
def rollingAverageRow (row_arr, window, min_per):
  return pd.Series(row_arr).rolling(window, min_periods=min_per).mean()  
  
  
  
  
  
def line_plots(time, data_arr, labels):
  """
  line_plots - plot the different weather data
               collected from the Climate Tag
               over time, labeling based off of 
               the labels sequence.
  input:  time - the timepoints for all the 
                  weather data collected.
          data_arr - a sequence of the different
                     Climate Tag categories to be
                     plotted.
          labels - a sequence of strings to serve
                   as labels for the respectively
                   indexed data in data_arr.
  output: a matplotlib line plot to visualize 
          the different Climate Tag categories.
  """
  plt.figure()
  
  # Setting up the color scheme for our plot
  colors = plt.cm.cool(np.linspace(0,1, len(data_arr)))
  plt.gca().set_prop_cycle(cycler('color', colors))
  
  # Iterate through data and plot each row
  for data in data_arr:
    plt.plot(time, data, label=str(labels.pop(0)))
  
  plt.xlabel('Time Point')
  plt.xticks([])
  plt.ylabel('Degrees (Celsius) or Percentage')
  plt.legend()
  plt.show()
  
  
def bar_plots(time, data_arr, labels):
  """
  bar_plots - plot the different weather data
               collected from the Climate Tag
               over time, labeling based off of 
               the labels sequence.
  input:  time - the timepoints for all the 
                  weather data collected.
          data_arr - a sequence of the different
                     Climate Tag categories to be
                     plotted.
          labels - a sequence of strings to serve
                   as labels for the respectively
                   indexed data in data_arr.
  output: a matplotlib bar plot to visualize the
          different Climate Tag categories.
  """
  plt.figure()
  
  # Setting up the color scheme for our plot
  colors = plt.cm.cool(np.linspace(0,1, len(data_arr)))
  plt.gca().set_prop_cycle(cycler('color', colors))
  
  # Iterate through data and plot each row
  for data in data_arr:
    plt.bar(time, data, label=str(labels.pop(0)))
  
  plt.title('Deviation from Average')
  plt.xlabel('Time Point')
  plt.xticks([])
  plt.ylabel('Degrees of Deviation (Celsius)')
  plt.legend()
  plt.show()

  
def forest_plot(time, data_arr, labels, prediction):
  """
  forest_plot - plot the different weather data
               collected from the Climate Tag
               over time, labeling based off of 
               the labels sequence and highlighting
               different anomalies.
  input:  time - the timepoints for all the 
                  weather data collected.
          data_arr - a sequence of the different
                     Climate Tag categories to be
                     plotted.
          labels - a sequence of strings to serve
                   as labels for the respectively
                   indexed data in data_arr.
          prediction - labeled anomalies based off
                   Isolation Forest training.
  output: a matplotlib line plot to visualize the
          different Climate Tag categories and 
          classified anomalies.
  """
  plt.figure()
    
  # Setting up the color scheme for our plot
  colors = plt.cm.cool(np.linspace(0,1,5))
  plt.gca().set_prop_cycle(cycler('color', colors))
  
  for data in data_arr:
    plt.plot(data, label=labels.pop(0))

  # Find where the anomalies are and highlight them
  anomaly_loc = np.where(prediction == -1)
  anomaly_loc = np.squeeze(anomaly_loc)
  while anomaly_loc.size != 0:
    start = anomaly_loc[0]
    anomaly_loc = anomaly_loc[1:]
    end = start
    idx = 0
    for next in anomaly_loc:
      if next - 1 == end:
        end = next
        idx += 1
      else:
        anomaly_loc = anomaly_loc[idx:]
        break
    plt.axvspan(start, end, color='yellow', alpha=0.25)

  plt.legend()
  plt.show()