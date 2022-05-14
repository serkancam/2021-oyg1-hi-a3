from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import pandas as pd
import time
ayarlar = FirefoxOptions()
ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar, executable_path="/home/serkan/Belgeler/2021-oyg1-hi-a3/geckodriver")
surucu.get("http://www.meb.gov.tr/meb_duyuruindex.php")
aciklama = []
tarih = []
adres = []
#print(surucu.page_source)
sayfa=1
son_sayfa=61
while sayfa<=son_sayfa:
    icerik = surucu.page_source
    ayristirma_agaci = BeautifulSoup(icerik,"lxml")
    duyurular = ayristirma_agaci.find_all("tr", attrs={"role":"row"})
    # print(duyurular)
    # break
    for duyuru in duyurular:
        try:
            duyuru_aciklama=duyuru.find_all("td")[1].text
            duyuru_adres=duyuru.find_all("td")[1].find("a").get("href")
            duyuru_tarih=duyuru.find_all("td")[2].text
            aciklama.append(duyuru_aciklama)
            tarih.append(duyuru_tarih)
            adres.append(duyuru_adres)
        except:
            continue
    sayfa=sayfa+1
    surucu.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a").click()
    # time.sleep(0.5)
surucu.close()
veri = {"aciklama":aciklama,"adres":adres,"tarih":tarih}
df = pd.DataFrame(veri)
df.to_csv("meb_duyuru2_hepsi_headless.csv",index=False)
print("İşlem bitti.")