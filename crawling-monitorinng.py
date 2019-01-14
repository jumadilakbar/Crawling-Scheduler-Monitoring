import schedule
import time
import pymongo
import gc
from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import pprint
client = MongoClient('127.0.0.1', 27017)
client.admin.authenticate('root', 'password', source='admin')
db = client['admin']
Monitoring= db["Monitoring"]
logf = open("crawling.log", "w")
# db.collection_names(include_system_collections=False)
mycol= db["Crawling"]
myberita= db["BERITA"]

def get_url(html,tag,style):
    soup = BeautifulSoup(html, 'lxml')
    crawl = soup.find_all(tag,class_=style)
    link = []
    for a in crawl:
        link.append(str(a))
    temp_urls = []
    #supoort my code with contact muhamadjumadilakbar@gmail.com
    return urls
def job():
    list_data = []
    data = {}
    for post in mycol.find():
        url = post['url']
        html = urlopen(url)
        list_url = get_url(html,post['path_crawling'][0],post['path_crawling'][1])
        pc = post['path_content'][0]
        pc1 =post['path_content'][1]
        tb = post['path_terbit'][0]
        tb1 = post['path_terbit'][1]
        nama_sumber =post['website']

        #....
        #supoort my code with contact muhamadjumadilakbar@gmail.com
    if not list_data:
        pass
    else:
        simpan = myberita.insert_many(list_data)
    print("I'm working...")
    logf.write(" Crawling Success ")
    post = {"Status": "Crawling Success",
            "date": datetime.datetime.now()}
    Monitoring.insert_one(post)
    gc.collect()

try :
    schedule.every(1).hours.do(job)
    while True:
        schedule.run_pending()
        #supoort my code with contact muhamadjumadilakbar@gmail.com
        time.sleep(1)

# except OSError as er:
except Exception as e:
    logf.write(" Crawling Failed ")
    post = {"Status": "Crawling Failed",
            "date": datetime.datetime.now()}
    Monitoring.insert_one(post)
    #supoort my code with contact muhamadjumadilakbar@gmail.com
