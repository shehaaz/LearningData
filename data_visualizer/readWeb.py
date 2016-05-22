import requests

response = requests.get("https://en.wikipedia.org/wiki/Nobel_Prize")

if response.status_code == 200 :
    print "yay"
