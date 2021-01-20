## CSV Data

> Comma-separated values (CSV) data is a super useful way to organize large sets of data. As the name suggests, the tabular data in these files are separated by commas! You've also probably seen this type of data before... think Microsoft Excel!

>So now we know how to make variables and numpy arrays and how to access the data within them. But, what if we want to analyze data that's too big to write in by hand? Or, perhaps, that someone else collected? For this, we will need to understand File I/O, meaning how to make your program read and write other files in the script itself.

## 2 Dimensional Arrays

### Wow, look at all that data!

#### So....now what?

To play with this data, we have a few options &mdash; the method we'll be using in this course is to populate numpy arrays with csv data. Here's how we'll do it!

The pandas read_csv method gives you the data in the form of an array of arrays. You can think of this as a matrix, which the inner most arrays are each a row of the matrix, and once you select a row you may choose a column. For example, suppose you have the following matrix below, which is composed of the first two data points of the csv we read in above:

$$
\left[\begin{array}{cc} 
0	& 58	& 19	& 215 &	1119437.0 &	101.76\\
1 &	58	& 19	& 215	& 1119437.0	& 101.76\\
\end{array}\right]
$$

This is just the first two rows of that csv file! But how do we represent this in Python?

$$
\left[\begin{array}{cc} 
\left[\begin{array}{cc}
0	& 58	& 19	& 215 &	1119437.0 &	101.76
\end{array}\right]\\
\left[\begin{array}{cc}
1 &	58	& 19	& 215	& 1119437.0	& 101.76
\end{array}\right]\\
...
\end{array}\right]
$$

As you can see, we have one big array, built up of smaller arrays. We call this format a 2 Dimensional Array. Each inner array on its own is a row in the csv data we had above. Once you grab one of those arrays (rows), you can easily grab any of the array specific data points (columns), whether it's that point in time's humidity, temperature, etc.

Let's call our 2D Array *weather_array*. If we wanted to grab that first row of *weather_array*, we would index it by 0 by writing *weather_array[0]*. This would give us direct access to the following:

$$
\left[\begin{array}{cc}
0	& 58	& 19	& 215 &	1119437.0 &	101.76
\end{array}\right]\\
$$

Let's suppose we were only interested in the humidity of the first time stamp. To grab *only* that information, we would call *weather_array[0,1]* to give us direct access to the following information:

$$
58
$$

{Try It!}(python3 CsvData.py)