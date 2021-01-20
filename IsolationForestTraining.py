import pandas as pd 
import numpy as np 
import pickle
import matplotlib.pyplot as plt
from cycler import cycler
import mylib

from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

if __name__ == '__main__':
    # Disk storage 
    data_file = 'climateSensorDay_Night.csv'
    model_file = "model.sav"
    scaler_file = "scaler.sav"

    ####################################################################
    # Output Formatting  
    # stack overflow:  https://stackoverflow.com/questions/2891790/how-to-pretty-print-a-numpy-array-without-scientific-notation-and-with-given-pre
    np.set_printoptions(precision=2)
    np.set_printoptions(suppress=True)
    np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
    ####################################################################

    #classification results from training data
    anomaly_count = 0
    normal_count = 0

    ####################################################################
    # Lesson 1: CSV acquisition and Data pre-processing step 
    # Enhance the pd.read_csv(data_file) command to eliminate the date and 
    # index columns from the data frame here.

    # This should be a get_data() function in mylib
    # see https://stackoverflow.com/questions/12960574/pandas-read-csv-index-col-none-not-working-with-delimiters-at-the-end-of-each-li
    
    ## TODO: Set df to your desired csv file data
    df = mylib.get_data("climate sensor tag_2020_06_28_09_39_12_824-Train.csv")
    print(df)

    ####################################################################

    ####################################################################
    # Lesson 2:  DataFrame to 2D Array
    # TODO: Convert df to array type for sklearn
    training_data = np.asarray(df)
    print ("Training Data Array:")
    print(training_data)

    ####################################################################

    ####################################################################
    # Lesson 3: Standardizing
    # TODO: Normalize the training_data between 0 and 1.
    ####################################################################
    scaler = MinMaxScaler().fit(training_data)
    training_data_normalized = scaler.transform(training_data)
    
    ####################################################################
    # Lesson 4: 
    # TODO: Turn the columns of the 2D array into a set of 1D arrays for 
    # plotting each sensor value. Note the 2D array data has been normalized 
    # by this stage.
    ####################################################################
    humidity = mylib.columnToRow(training_data_normalized,0)
    temperature = mylib.columnToRow(training_data_normalized,1)
    uv = mylib.columnToRow(training_data_normalized,2)
    power = mylib.columnToRow(training_data_normalized,3)
    pressure = mylib.columnToRow(training_data_normalized,4)
    #smooth out pressure with rolling average
    pressure = mylib.rollingAverageRow(pressure, len(pressure), 2)
    
    
    ####################################################################
    # Lesson 5: choose the algorithm and create the model.
    # TODO: set the contamination factor and apply to training data once 
    # trained.

    #model = IsolationForest(max_samples=50, contamination=0.08)
    #model.fit(training_data_normalized)
    #prediction = model.predict(training_data_normalized)
    
    
    model = LocalOutlierFactor(contamination=0.3)
    prediction = model.fit_predict(training_data_normalized)

    
    #see classification results
    print ("Normal / Anomaly List:")
    print (prediction)

    # save model & scaler for later application in the test stage.
    pickle.dump(model, open(model_file, 'wb'))
    pickle.dump(scaler, open(scaler_file, 'wb'))
    ####################################################################

    ####################################################################
    # Lesson 6:  Plotting the normalized data to show the interactions between
    #           weather parameters.

    print (len(humidity))
    time = np.linspace(0, len(humidity), len(humidity))
    #labels = ["humidity", "temperature", "uv", "power", "pressure"]
    labels = ["hum","temp","uv","light","pres"]
    data_arr = [humidity, temperature, uv, power, pressure]
    #mylib.line_plots(time, data_arr,labels)
    mylib.forest_plot(time, data_arr,labels, prediction)

    ####################################################################

