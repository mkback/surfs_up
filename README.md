# Surfs Up 

## Overview 

W. Avy wants to open a surf shop in Hawaii, but wants to make sure the temperatures are good to make the ice cream business sustainable. We are given a sqlite database that has weather information around the island. We are able to pull from this database by using SQLAlchemy, a python library that allows us to map tables from the database. 

## Results

Using Matplotlib and python, the below chart was created to show the amount of rain in Hawaii. We can see that there are a few large rainstorms throughout the year, but there is no clear “rainy season." 
![Alt Image Text](https://github.com/mkback/surfs_up/blob/main/Resources/precp.png)

To compare temperature in Hawaii, we took a look at June and December results. Below are the summary statistics for each of these month’s temperatures. While it is slightly warmer in June, the two months do not have large differences. The average temperature in June was 75 degrees with a total range of 64-85 degrees while the average temperature in December was 71 degrees with a total range of 56-83 degrees.

June: 
![Alt Image Text](https://github.com/mkback/surfs_up/blob/main/Resources/June_temp_stats.png)  

December: 
![Alt Image Text](https://github.com/mkback/surfs_up/blob/main/Resources/Dec_temp_stats.png) 