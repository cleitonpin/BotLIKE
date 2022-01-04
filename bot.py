from selenium  import webdriver
import os
import time
import configparser


class InstagramBot:
    
    def __init__(self, username, password):

        """
        Inicialates an instance of the instagramBot class. call the login method to athenticat


        Args:
            username:str: The instagram username for a user
            password:str: The instagram apssword for a user

        Areibutters:
            driver:selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions

        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()

        


    def login(self):
        self.driver.get(f'{self.base_url}/accounts/login/')

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Entrar')]")[0].click()


        time.sleep(2)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

    def seguir_user(self, user):

        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")[0]               
        follow_button.click()

    # def seguir_follow_action(self, user, unfollow=False):

    #     if unfollow == True:
    #         action_button_text = 'Seguindo'

    def unfollow_user(self, user):

        self.nav_user(user)
        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Seguindo')]")[0]               
        unfollow_button.click()

        time.sleep(1)
        unfollow = self.driver.find_elements_by_xpath("//button[contains(text(), 'Deixar de seguir')]")[0]  
        unfollow.click() 




if __name__ == '__main__':

    # config_path = './config.ini'
    # cparser = configparser.ConfigParser()
    # cparser.read(config_path)
    # username = cparser['AUTH']['USERNAME']
    # password = cparser['AUTH']['PASSWORD']

    
    ig_bot = InstagramBot('username', 'password') 
    #ig_bot.nav_user('garyvee')
    ig_bot.seguir_user('maaurotony')
  


 
