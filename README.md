# FlightRecs
This program is used to find the top 20 lowest cost flights from a given origin.  Given the circumstances with COVID-19... we're desperate to go anywhere in our budget!  This app will help identify those locations by scraping skiplagged.com

## Prerequisites
  + Anaconda 3.7
  + Python 3.7
## Installation
Fork this [remote repository](https://github.com/nyk89/flightrecs) under your own control, then "clone" or download your remote copy onto your local computer.
Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):
```sh
cd FlightRecs
```
Use Anaconda to create and activate a new virtual environment, perhaps called "FlightRecs-env":
```sh
conda create -n FlightRecs-env python=3.7 # (first time only)
conda activate FlightRecs-env
```
From within the virtual environment, install any packages you might need:
```sh
pip install bs4
pip install selenium
pip install lxml
```
Download the appropriate chromedriver
```sh
http://chromedriver.chromium.org/
```
## Use
Run the program by typing the following into your terminal:
```sh
python flightrecs.py
```
Follow the instructions in the commandline.  Note that airport codes must be in capital letters and valid.  If searching for a one way ticket, do not type anything into the end date prompt, simply press enter.
