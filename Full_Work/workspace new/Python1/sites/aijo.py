
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("D://chromedriver_win32//chromedriver")  
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("https://www.ajio.com/")  
 
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("shoes")

time.sleep(2) 

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/button/span").click()
time.sleep(2)
driver.get("https://www.ajio.com/crocs-literide-clogs-with-slingback/p/460532521_black")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[6]/div[2]/div/div/div[2]/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[9]/div[1]/div[1]/div").click()
#driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/div[2]/a/div").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[9]/div[1]/div[1]/a/div").click()
print("Run Success")
driver.close()