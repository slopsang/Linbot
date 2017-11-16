# Linbot
Increase your popularity on LinkedIn and rank #1 among your network.


## About
* Connections are important within Linkedin
* Relationships
1st connections - people who are already connected with you (don't need to focus)
2nd connections - people who are able to send connect request
3rd connections

But there are A LOT of people. 
So... I want to create a bot to click all the CONNECT button!



## Requirements
Python 2.7, Selenium, Sublimetext

## Steps

### Install Python 2.7
Why not 3.7? <br/>
Because some packages are not yet transformed so 2.7 is better as now.
You can install python 2.7 from [here](https://anaconda.org/)

### Install Selenium package
pip install selenium

### Install chromedriver
You can install chromedriver from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.33/)

### Install Sublimetext
You can use
press CMD + B (MacOS) or 
press Ctrl + B (Windows)
to run foo.py (python file) within Sublimetext.

### Install sublime package control for sublimetext
1. View - Show console 
2. Copy and paste the following from [here](https://packagecontrol.io/installation)
3. press CMD + shift + P to open package control

### Install 2 packages
* Anaconda
* Sublime-text-build-2-text
* Go to package settings -> Anaconda and set "anaconda_linting" to 'false'

### Get html page source
* First, you need to download chromedriver and save in the PATH.
```
from selenium import webdriver

chromedriver = webdriver.Chrome()

url = 'https://www.linkedin.com/'

chromedriver.get(url)

print chromedriver.page_source

chromedriver.quit()
```

### Find element by xpath and do sendkey action (id,pass) / do click action (log-in)
* Go to the Linkedin.com browser 
* use INSPECT 
* COPY XPath
To see the result, we will add
```
import time
time.sleep(5)
```
