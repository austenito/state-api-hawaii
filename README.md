# Hawaii API

This is the start of an API for my home state of Hawaii. Since I've always 
wanted to visualize this data, I'm going to slowly start mapping an API loosely 
based off of [DBEDT's](http://hawaii.gov/dbedt/info/economic/databook/) data.

* Flask
* D3.js
* MongoDB

## Getting started

### Running the API server

``` 
$> workon <your magical env here>
$> pip install requirements.txt 
$> python api.py
```
#### Testing the api

``` curl localhost:5000/population/2012/hawaii ```

**win**

### Running the www server

``` 
$> workon <your magical env here>
$> pip install requirements.txt 
$> bower install
$> python www.py
```

## Updates

### 2013-02-16

Brought in Bower, D3, Bootstrap.  Testing out a few visualizations.

### 2013-02-13

My game plan is to stub out the data, then take a peek at what the data
contract(s) should be. Also, here be dragons. I'm learning Flask. I swear I'll
try not to break anything. :)
