from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import pandas as pd
import time
ayarlar = FirefoxOptions()
ayarlar.add_argument("--headless")
surucu = webdriver.Firefox(options=ayarlar, executable_path="geckodriver.exe")
surucu.get("http://www.meb.gov.tr/meb_duyuruindex.php")
aciklama = []
tarih = []
adres = []