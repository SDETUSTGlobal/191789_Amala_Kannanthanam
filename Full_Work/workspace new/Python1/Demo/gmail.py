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
driver.get("https://www.gmail.com")  
#identify the user name text box and enter the value  
driver.find_element_by_id("identifierId").send_keys("amalak6870052@gmail.com")  
time.sleep(2)  
  

#click on the next button  
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()  
time.sleep(1) 
driver.find_element_by_xpath("//*[@id='next']/div/button/span").click()  
time.sleep(1) 
driver.find_element_by_xpath("/html/body/header/div/div/div/a[2]").click()  
time.sleep(1) 
driver.find_element_by_id("identifierId").send_keys("amalak6870052@gmail.com")  
time.sleep(2)  
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()  
time.sleep(1) 
  
 #driver.find_element_by_xpath("").click()  
#identify the password text box and enter the value   
#driver.find_element_by_name("password").send_keys("######")  
#time.sleep(3)  
#click on the next button  
#driver.find_element_by_xpath("//span[contains(text(),'Next')][1]").click()  
#time.sleep(3)  
#close the browser  
driver.close()  
print("Gmail login has been successfully completed")  
