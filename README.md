# People poptulation density map visualization with a python program

The program `pop_main.py` shows a number of population density charts on the same graph using a function imported from the `pop_module` module.  
The function can process ASCII files that can be downloaded using the following link and supports different data resolution.  
https://sedac.ciesin.columbia.edu/data/set/gpw-v4-population-density-rev11/data-download  

Each file has the following format in a 2D array form like below and covers all coordinates starting from the left top corner (lon=-180, lat=-90) ending to the right bottom one (lon=180, lat=90). That is, every row covers all longitudes (with distance in 360/ncols == cellsize degrees between adjacent values) and every column covers all latitues (with distance in 180/nrows == cellsize degrees between adjacent values).  
The vXY numbers represent people dencity in people/km^2 at the corresponding coordinates.  
```
ncols         8640
nrows         4320
xllcorner     -180
yllcorner     -90
cellsize      0.041666666666667
NODATA_value  -9999
v11 v12 v13 ...
v21 v22 v23 ...
...
```
The function accepts a file name and the area description needed (as 2 paris of longitudes and latitudes in degrees representing the area's boarders) to visualize as parameters.  
Input data files must be placed at the `data` directory where the python files reside to run the program successfully as is.

There is a number of useful links as well:  
documentation: http://sedac.ciesin.columbia.edu/data/collection/gpw-v4/documentation  
website: http://sedac.ciesin.columbia.edu/data/collection/gpw-v4/sets/browse  
