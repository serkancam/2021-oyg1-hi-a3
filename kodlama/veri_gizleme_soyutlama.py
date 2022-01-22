import datetime


class Araba():
    def __init__(self,marka):
        self.__marka=marka
        self.__model=1983
        self.__vites_sayisi=5
        self.__en_yuksek_hiz=180
    
    def model_bilgisi(self):
        return self.__model

    def model_ata(self,model:int):
        if model>=1983 and model<=datetime.date.today().year:
            self.__model=model
    
    def marka_bilgisi(self):
        return self.__marka
    
    def marka_ata(self,marka:str):
        if marka is str:
            self.__marka=marka
    
a1=Araba("FIAT")
a1.model_ata(2020)
a1.marka_ata(585)
print(a1.marka_bilgisi())
print(a1.model_bilgisi())
