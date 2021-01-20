import pandas as pd 
import numpy as np 
import pickle
import matplotlib.pyplot as plt
import mylib
import day3plot

from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import IsolationForest

if __name__ == '__main__':
    # Disk storage 
    data_file = 'climate sensor tag_2020_06_28_09_39_12_824-Train.csv'
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
    df = mylib.get_data(data_file) 
    print(df)
    
    # see https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
    df.drop('TimeStamp', axis=1, inplace=True)
    print(df)
    ####################################################################

    ####################################################################
    # Lesson 2:  DataFrame to 2D Array
    # TODO: Convert df to array type for sklearn
    print ("Training Data Array:")
    training_data = np.asarray(df)
    for t in training_data:
        print(t)
    ####################################################################

    ####################################################################
    # Lesson 3: Standardizing
    # TODO: Normalize the training_data between 0 and 1.
    scaler = MinMaxScaler().fit(training_data)
    training_data_normalized = scaler.transform(training_data)
    print("Transformed Data");
    for t in training_data_normalized:
       print(t)
    ####################################################################

    ####################################################################
    # Lesson 4: 
    # TODO: Turn the columns of the 2D array into a set of 1D arrays for 
    # plotting each sensor value. Note the 2D array data has been normalized 
    # by this stage.
    humidity = mylib.columnToRow(training_data_normalized,0)
    temperature = mylib.columnToRow(training_data_normalized,1)
    uv = mylib.columnToRow(training_data_normalized,2)
    power = mylib.columnToRow(training_data_normalized,3)
    pressure = mylib.columnToRow(training_data_normalized,4)
    data_arr = [humidity, temperature, uv, power, pressure]
    labels = ["humidity", "temperature", "uv", "power", "pressure"]
    ####################################################################

    ####################################################################
    # Lesson 5: choose the algorithm and create the model.
    # TODO: set the contamination factor and apply to training data once 
    # trained.
    model = IsolationForest(contamination=0.11)
    model.fit(training_data_normalized)
    prediction = model.predict(training_data_normalized)

    #save model & scaler for later application in the test stage.
    pickle.dump(model, open(model_file, 'wb'))
    pickle.dump(scaler, open(scaler_file, 'wb'))
    ####################################################################


    ####################################################################
    # Lesson 6:  Plotting the normalized data to show the interactions between
    #           weather parameters.
    time = np.linspace(0,len(humidity), len(humidity))
    day3plot.forestPlot(time,data_arr, labels, prediction)
    ####################################################################

    #see classification results
    print ("Normal / Anomaly List:")
    print (prediction)

    #for p in prediction:
        #if p == -1:            
            #anomaly_count += 1
            #print("anomaly ", p)
        #else:
            #normal_count += 1  
            #print("normal ", p)  