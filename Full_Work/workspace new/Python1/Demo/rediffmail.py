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
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")  
#identify the user name text box and enter the value  
driver.find_element_by_xpath("//*[@id='login1']").send_keys("amalak6870052@gmail.com")  
time.sleep(1)  
 
driver.find_element_by_name("passwd").send_keys("amala")  
time.sleep(1) 
driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input[2]").click()  
time.sleep(1) 

driver.close()  
print("rediffmail login has been successfully completed")  
  