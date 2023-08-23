!pip install Selenium
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys

 

print("sample test case started")  
wd = webdriver.Chrome()  
#driver=wd.firefox()  
#maximize the window size  
wd.maximize_window()  
#navigate to the url  
wd.get("https://www.google.com/")  
