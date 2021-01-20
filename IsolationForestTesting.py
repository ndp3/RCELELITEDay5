import pandas as pd 
import numpy as np
import pickle
import time
import mylib

####################################################################
# Output Formatting  
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
####################################################################

def classify(model, scaler, ANOMALY):
  '''
  classify - Classifies data as anomaly or normal behavior 

  inputs: model    trained model to classify event data
          scaler   MinMaxScaler used to scale training data for the model
          ANOMALY  Constant value signaling anomaly from model prediction 
  '''
  ####################################################################
  # Lesson 1: CSV acquisition and Data pre-processing step 
  # Enhance the pd.read_csv(data_file) command to eliminate the date and 
  # index columns from the data frame here.
  #
  # TODO: grab data using get_data() and scale it
  
  ####################################################################
  events = mylib.get_data( "climate sensor tag_2020_06_28_14_41_08_188-Test.csv" ) # returns data frame object
  training_data = np.asarray(events)
  
  transformed_data = scaler.transform(training_data)  # Normalizes the data
  print ("Scaled Data:")
  for t in transformed_data:
    print(t)
  ####################################################################
  # Lesson 2: Determine the classifications made by the model and 
  # iterate through the predicted anomalies and print out where they
  # occur, then plot it!
  #
  # TODO: use forest_plot from mylib to plot the anomalies!
  
  ####################################################################
  #classification = model.predict(transformed_data) # Isolation Forest
  classification = model.fit_predict(transformed_data) # LOcal Outlier Factor
  print ("Anomaly Classification:")
  print (classification)

  #print event data with labels 
  '''
  i=1
  for p in classification:
    if p == ANOMALY:
      #TODO send data to data visualization service 
      print("Row", i, ": " , events[i], "ANOMALY") #placeholder
    else:
      print("Row", i, ": " , events[i], "Normal") #placeholder
    i += 1
    #time.sleep(1)  
  '''    
 
  #set up the plot arrays
  humidity = mylib.columnToRow(transformed_data,0)
  temperature = mylib.columnToRow(transformed_data,1)
  uv = mylib.columnToRow(transformed_data,2)
  power = mylib.columnToRow(transformed_data,3)
  pressure = mylib.columnToRow(transformed_data,4)
  #smooth out pressure with rolling average
  pressure = mylib.rollingAverageRow(pressure, len(pressure), 2)

  time = np.linspace(0, len(humidity), len(humidity))
  labels = ["hum","temp","uv","light","pres"]
  data_arr = [humidity, temperature, uv, power, pressure]
  mylib.forest_plot(time, data_arr,labels, classification)    
    
    

if __name__ == '__main__':
    ANOMALY = -1
    model_file = "model.sav"
    scaler_file = "scaler.sav"

    ####################################################################
  # Lesson 3: Load up the model and scaler you trained by running the
  # training file so you can apply the now trained model to the new data.
  #
  # TODO: Use pkl functions to load the model/scaler!
  
  ####################################################################

    #load model & scaler
    model = pickle.load(open(model_file, 'rb'))
    scaler = pickle.load(open(scaler_file, 'rb'))
    classify(model, scaler, ANOMALY)