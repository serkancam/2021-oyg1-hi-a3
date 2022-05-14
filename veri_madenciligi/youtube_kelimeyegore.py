from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import pandas as pd
import time
ayarlar = FirefoxOptions()
#ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar, executable_path="/home/serkan/Belgeler/2021-oyg1-hi-a3/geckodriver")
surucu.get("https://www.youtube.com/results?search_query=bilim+sanat+merkezi")

#print(surucu.page_source)

# son_yukseklik = surucu.execute_script("return document.body.scrollHeight")
while True:
    icerik = surucu.page_source
    ayristirma_agaci = BeautifulSoup(icerik,"lxml")
    videolar = ayristirma_agaci.find_all("div", attrs={"class":"style-scope ytd-video-renderer"})
    # print(duyurular)
    # break
    for v in videolar:
        try:
           title=v.find("a").text
           print(title)
        except:
            continue
    surucu.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   
    time.sleep(0.5)
    # yeni_yukseklik = surucu.execute_script("return document.body.scrollHeight")
    # if yeni_yukseklik == son_yukseklik:
    #     break
    # son_yukseklik = yeni_yukseklik
   
   
surucu.close()
