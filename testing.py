#/usr/bin/env python3
#################################
#owner: droritzz
#date: 10.6.21
#purpose: check if the docker container works properly, the webpage is correct
##################################

# import HTMLSession from requests_html. this library gets JS support
from requests_html import HTMLSession

#import datetime from datetime
from datetime import date
today = date.today()
print("today is:" , today)

# create an HTML session object and test if the webpage is served properly
session = HTMLSession()
response = session.get("IP address of the pod, not finished")
print = (f"RESPONSE CODE: {response.status_code}")
# get text rendered by JavaScript
response.html.render()





#getting the real time from the test
testime = datetime.datetime.now()
print(testime)
