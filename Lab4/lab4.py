import urllib.request
import requests

url = "https://api.thingspeak.com/update?api_key="
key = "54CDA6FJF4RCJ92C"
email = "erichardy@cmail.carleton.ca"
group = "L2-M-6"
groupID = "c"
header = "&field1={}&field2={}&field3={}".format(email, group, groupID)
fullUrl = url + key + header
data = urllib.request.urlopen(fullUrl)