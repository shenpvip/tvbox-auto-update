import re
import datetime
import requests
import json
import urllib3
import os
import shutil

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
with open('./url.json', 'r', encoding='utf-8') as f:
    urlJson = json.load(f)
sourceList = ''
proxyUrl = "https://github.rocs.site/https://raw.githubusercontent.com"

if os.path.exists('./tv'):
    shutil.rmtree('./tv')
for item in urlJson:
    urlReq = requests.get(item["url"], verify=False)
    urlName = item["name"]
    urlPath = item["path"]
    reqText = urlReq.text
    reqText = reqText.replace("'./", "'" + urlPath) \
        .replace('"./', '"' + urlPath) \
        .replace("/raw/", "/") \
        .replace("'https://github.com", "'" + proxyUrl) \
        .replace('"https://github.com', '"' + proxyUrl) \
        .replace("'https://raw.githubusercontent.com", "'" + proxyUrl) \
        .replace('"https://raw.githubusercontent.com', '"' + proxyUrl)
    sourceList += urlName + '：' + proxyUrl + '/shenpvip/vd/main'+"/tv/" + str(reI) + "/" + urlName + ".json \n\n"
    filePath = "./tv/" + str(reI)
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    fp = open(filePath + "/" + urlName + ".json", "w+", encoding='utf-8')
    fp.write(reqText)
        
now = datetime.datetime.now()
fp = open('json.txt', "w+", encoding='utf-8')
fp.write("本次更新时间为：" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
fp.write(sourceList)
fp.close()
