import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from explicity_wait import ExplicitWaitType


class Trello:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)
        self.tarjetas_lista = []

    def login_trello(self):
        self.driver.get(f"https://trello.com/login")
        user_element = self.wait.waitForElement(locator='user')
        self.wait.sendKeys("lucin.perez@lionintel.com", user_element)
        login_element = self.wait.waitForElement(locator='login')
        self.wait.elementClick(login_element)
        time.sleep(2)
        password_element = self.wait.waitForElement(locator='password')
        self.wait.sendKeys("tXj/Rih78CgbrTX", password_element)
        login_element = self.wait.waitForElement(locator="login-submit")
        self.wait.elementClick(login_element)
        return True


    def extraer(self,):
        time.sleep(5)
        self.driver.get("https://trello.com/b/EneMeDPQ/qa-team")
        for n in range(1,7):
            element_tarjeta_1 = self.wait.waitForElement(locator=f'//*[@id="board"]/div[2]/div/div[2]/a[{n}]', locatorType='xpath')
            self.wait.elementClick(element_tarjeta_1)
            time.sleep(1)
            titulo_text = self.driver.title
            salir_element = self.wait.waitForElement(locator='//*[@id="chrome-container"]/div[3]/div/div/a', locatorType='xpath')
            descripcion_element = self.wait.waitForElement(locator='//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[2]/div/div/div/div[2]/div/div/div[2]', locatorType='xpath')
            descripcion_element = self.wait.get_text(descripcion_element).strip()
            etiqueta_element = self.wait.waitForElement(locator='//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[1]/div[3]/div/span[1]', locatorType='xpath')
            etiqueta_element = self.wait.get_text(etiqueta_element).strip()
            self.wait.elementClick(salir_element)
            titulo = self.formato_titulo(titulo_text)
            descripcion_element = self.formato_descripcion(descripcion_element)

            self.tarjetas_lista.append((titulo, descripcion_element, etiqueta_element))

        return self.tarjetas_lista


    def formato_titulo(self, titulo):
        titulo = titulo.split(" ")
        nuevo_titulo = ""
        for palabra in titulo:
            if palabra == "en" or palabra == "3DID" or palabra == "|" or palabra == "Trello" or palabra == "TEAM" or palabra == "QA":
                pass
            else:
                nuevo_titulo += palabra + " "
        return nuevo_titulo.strip()


    def formato_descripcion(self, descripcion):
        descripcion = descripcion.replace(f'\n', "")
        return descripcion
    def cerrar(self):
        self.driver.close()

    def login_true(self):
        time.sleep(1.5)
        return True

    def login_qase(self):
        self.driver.get("https://app.qase.io/login")
        email_element = self.wait.waitForElement(locator='inputEmail')
        self.wait.sendKeys("lucin.perez@lionintel.com", email_element)
        time.sleep(1)
        password_element = self.wait.waitForElement(locator='inputPassword')
        self.wait.sendKeys("-JzSL_HCHi4#Nn7", password_element)
        login_element = self.wait.waitForElement(locator='btnLogin')
        self.wait.elementClick(login_element)
        return True