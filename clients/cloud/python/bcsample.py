import json
import urllib.request
import os
with urllib.request.urlopen('http://rbi.ddns.net/getBreadCrumbData')as response:
   breadcrumb = response.read()
data = json.loads(breadcrumb)
#data = json.loads(json_string
#for k in range(1, 1000):
 # print(data[k])
with open('bread_crumb_data.json', 'w') as file:
 #for i in range(1, 1000):        
  #json.dump(data[i], file)
  json.dump(data[:1001],file)



