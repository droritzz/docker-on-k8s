#/usr/bin/env python3
#################################
#owner: droritzz
#date: 10.6.21
#purpose: check if the docker container works properly, the webpage is correct
##################################

# import HTMLSession from requests_html
from requests_html import HTMLSession

#import datetime from datetime
from datetime import datetime


#getting the real time from the test
testime = datetime.datetime.now()
print(testime)
