__author__ = 'ccn1069'

##
# Convert url to short url or reverse, using Baidu API
# author: ccn1069
# date: 2015-8-19
# Usage:
# sort_url.py -u <long_url>
# Convert long url to short one
#
# sort_url.py -u <short_url> -o query
# Convert short url to long one
##
import sys
import getopt
import urllib
import urllib2
import json

create_api = "http://dwz.cn/create.php"
query_api = "http://dwz.cn/query.php"


# TODO: Send a post request to the url with the data
def post_data(url, data):
    data_urlencode = urllib.urlencode(data)
    req = urllib2.Request(url=url, data=data_urlencode)
    resp = urllib2.urlopen(req).read()
    return json.loads(resp)


def usage():
    print "Usage: short_url.py [-u | --url=] <your long url> [-o | --op=] <operation: create or query>"


url = ""    # The url waiting to be convert
alias = ""  # Customize short url alias when creating
op = "create"   # Operation, create or query
api_url = create_api    # API url

opts, args = getopt.getopt(sys.argv[1:], "u:a:o:", ["url=", "alias=", "op="])
for key, value in opts:
    if key == "-u" or key == "--url":
        url = value
    elif key == "-a" or key == "--alias":
        alias = value
    elif key == "-o" or key == "--op":
        op = value

if url == "":
    usage()
    sys.exit()

data = {"url": url}     # API query data

if op == "query":
    api_url = query_api
    data = {"tinyurl": url}

if op == "create" and alias != "":
    data["alias"] = alias

result = post_data(api_url, data)

print json.dumps(result)