from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r".\geckodriver-v0.26.0-win64\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(4)

        username_input = driver.find_element_by_xpath("//input[@name='username']")
        password_input = driver.find_element_by_xpath("//input[@name='password']")        
        
        username_input.clear()
        username_input.send_keys(self.username)

        password_input.clear()
        password_input.send_keys(self.password)

        time.sleep(1)

        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")

        time.sleep(5)

        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        pics = driver.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]/a')
                
        pic_hrefs = [elem.get_attribute("href") for elem in pics]
        
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs: 
            driver.get(pic_href)

            try:
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]').click()

                print("Curtiu: " + pic_href)
                time.sleep(19)
            except Exception as e:
                time.sleep(5)
                print(e)

usuario = "SeuUsuario"
senha = "SuaSenha"

bot = InstagramBot(usuario, senha)

print("Executing...")

bot.login()
bot.curtir_fotos("memesBR")