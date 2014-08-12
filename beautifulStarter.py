#
#
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC

import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib
import urllib

url = "http://www.yellowpages.com/news/entertainment"
url_somecard = "http://www.someecards.com/ecards/flirting/"
url_triton = "https://act.ucsd.edu/myTritonlink20/display.htm"
image = "http://i1.ypcdn.com/ypcms/system/assets/134450/medium/Million-Dollar-Listing---570-380_medium.jpg"

# remember to change URL for whatever u want
r = requests.get(url)

soup = BeautifulSoup(r.content)
links = soup.find_all("a")

# Use something like this to download all the images from SomeCard
# for link in links:
#   if "http" in link.get("href"):
#     # print link


# for yellowpages, the div tag is post
# V IMPORTANT - DIV Search can have anything you want

# g_data = soup.find_all("div" , {"class" : "img-wrapper"})

g_data = soup.find_all("div" , {"class" : "post"})
# print g_data

for item in g_data:
  print item.text

# def savePic(url):
#     hs = hashlib.sha224(url).hexdigest()
#     file_extension = url.split(".")[-1]
#     uri = ""
#     dest = uri+hs+"."+file_extension
#     print dest
#     try:
#         urllib.urlretrieve(url,dest)
#     except:
#         print "save failed"
#
#
# savePic(image)
