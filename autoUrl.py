import re
import datetime
import requests
import json
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
with open('./url.json', 'r', encoding='utf-8') as f:
    urlJson = json.load(f)
sourceList = ''
reList = ["https://ghproxy.com/https://raw.githubusercontent.com", "https://cdn.staticaly.com/gh",
          "https://raw.fastgit.org", "https://raw.kgithub.com", "https://raw.iqiq.io",
          "https://github.moeyy.xyz/https://raw.githubusercontent.com"]

for item in urlJson:
    urlReq = requests.get(item["url"], verify=False)
    for reI in range(len(reList)):
        urlName = item["name"]
        urlPath = item["path"]
        reqText = urlReq.text
        reqText = reqText.replace("'./", "'" + urlPath) \
            .replace('"./', '"' + urlPath) \
            .replace("/raw/", "/") \
            .replace("'https://github.com", "'" + reList[reI]) \
            .replace('"https://github.com', '"' + reList[reI]) \
            .replace("'https://raw.githubusercontent.com", "'" + reList[reI]) \
            .replace('"https://raw.githubusercontent.com', '"' + reList[reI])
        sourceList += urlName + '：' + reList[reI] + '/shenpvip/tvbox-auto-update/main'+"/tv/" + str(reI) + "/" + urlName + ".json \n\n"
        filePath = "./tv/" + str(reI)
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        fp = open(filePath + "/" + urlName + ".json", "w+", encoding='utf-8')
        fp.write(reqText)
now = datetime.datetime.now()
fp = open('README.md', "w+", encoding='utf-8')
fp.write("# TvBox 配置\n\n")
fp.write(sourceList)
fp.write("本次更新时间为：" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
fp.close()
