Let's walk through what we expect you to do in this file:

1. After you've grabbed your ```mylib.py``` file and uploaded it to today's project, use your ```get_data()``` function to read in weather data from the CSV file under Lesson 1! Set the output of that function to ```df```.
2. Convert ```df``` to a numpy array under Lesson 2 so that we can manipulate the data and pass it into our algorithm! Call this ```training_data```.
3. In Lesson 3, use the ```MinMaxScaler.fit()``` function from sklearn to define a scaling function specific to ```training_data```, and assign it to the variable ```scaler```. Then, assign to ```training_data_normalized``` the scaler transform on our training data (called by ```scaler.transform()```) to apply the scaling to our CSV data.
4. In Lesson 4, use your ```columnToRow()``` function from ```mylib.py``` to create variables for each column (humidity, temperature, etc.). You should then add these to a Python sequence by writing something like ```data = [var1, var2,...]``` and then create a sequence of labels in the same order, something like ```labels = ["varname1", "varname2",...]```. Make sure the orders are the same (i.e. humidity data is first in ```data``` and first in ```labels```)!
5. Uncomment the line ```model = IsolationForest(contamination=0.11)``` and alter the contamination factor in Lesson 5. In the lines directly below this, fit the model to our normalized training data by calling ```model.fit()``` with the ```training_data_normalized``` as input. Then, define a variable called ```prediction``` to be the result of ```model.predict()``` with ```training_data_normalized``` as input.
6. In Lesson 6, we want you to plot the output of your network on the data you trained on. Since you trained on this data, it should be pretty accurate! We're going to be using the mylib.py file that has been provided to you, calling the function ```forest_plot()```. The time can be derived by uncommenting the line with the variable ```time```, so long as one of your column arrays is entitled ```humidity```. The order in which you should pass in your input parameters is:
      - time
      - array of column data
      - array of label strings
      - prediction


{Try It!}(python3 IsolationForestTraining.py)