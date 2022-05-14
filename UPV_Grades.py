from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class UPV_Grades():
    
    def __init__(self) -> None:
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        self._driver = webdriver.Chrome(service=Service(PATH))
        self._driver.get('https://intranet.upv.es/pls/soalu/est_intranet.NI_Portal_n?p_idioma=i')
        assert 'UPV' in (self._driver.title), self._driver.quit()

    def login(self,dni,pin):
        self._dni = self._driver.find_element(By.NAME,'dni')
        self._dni.send_keys(dni) 
        self._pin = self._driver.find_element(By.NAME,'clau')
        self._pin.send_keys(pin)
        self._enter = self._driver.find_element(By.CLASS_NAME,'upv_btsubmit')
        self._enter.click()

    def intranet(self):
        self._intranet = self._driver.find_element(By.ID,'intranet')
        self._intranet = self._intranet.find_element(By.CLASS_NAME,'titularEspecial')
        self._intranet.click()
        
    def notas(self):
        self._notas = self._driver.find_element(By.ID,'elemento_405')
        self._notas = self._notas.find_element(By.TAG_NAME,'a')
        self._notas.click()
        self._notasPadrinoTabla = self._driver.find_element(By.XPATH,"//div[@id='contenido']/div[@class='container'][4]")
        self._tablaNotas = self._notasPadrinoTabla.find_elements(By.TAG_NAME,'td') # Devuelve todas las filas
        self._notasDict = self.dicNotas(self._tablaNotas)
        UPV_Grades.displayNotas(self._notasDict)
        
    def dicNotas(self,tablaNotas) -> dict:
        counter = 0
        mainDict = {}
        auxDict = {}
        FirstTime = True
        for fila in tablaNotas:
            
            class_ = fila.get_attribute('class')
            if class_ == "upv_listacolumnassubtitulo":
                if not FirstTime:
                    mainDict[dic_key] = auxDict.copy()
                    auxDict = {}
                dic_key = fila.text
                counter=0
                FirstTime = False
                
            elif counter==1:
                value_link = fila.find_element(By.TAG_NAME,'a').get_attribute('href')
            elif counter==2:
                value_date = fila.text
            elif counter==3:
                value_exam = fila.text
            elif counter==4:
                value_grade = fila.text
                
                auxDict[value_exam] = [value_date,value_grade,value_link]
                counter=0
            
            counter+=1
            
        return mainDict
    
    def displayNotas(dictionary):
        for clave in dictionary:
            print(f'{clave}')
            auxDic = dictionary[clave]
            for subClave in auxDic:
                values = auxDic[subClave]
                print(f'\t {subClave}: {values[1]}')
        
    def close(self):
        self._driver.quit()
        
if __name__ == '__main__':
    bot = UPV_Grades()
    bot.login('','') # Poner credenciales
    bot.intranet()
    bot.notas()
    time.sleep(5)
    bot.close()
    
