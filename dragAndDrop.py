
#Task -23 -https://jqueryui.com/droppable/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class DragAndDrop:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def drag(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.implicitly_wait(5)             
            #switch to iframe
            iframe = self.driver.find_element(By.XPATH, '//iframe[@src = "/resources/demos/droppable/default.html"]')
            self.driver.switch_to.frame(iframe)
            #Drag and Drop
            action = ActionChains(self.driver)
            source = self.driver.find_element(By.ID, 'draggable')
            target = self.driver.find_element(By.ID, 'droppable')
            action.drag_and_drop(source=source, target=target).perform()
            sleep(3)
        
        except NoSuchElementException as error:
            print(error)


url = "https://jqueryui.com/droppable/"
d = DragAndDrop(url)
d.drag()