import re
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Test1:

 list200 = ['http://99papers.com/', 'https://99papers.com/pricing',' https://99papers.com/samples','https://99papers.com/samples?lol'];
 list301 = ['http://99papers.com/','https://www.99papers.com/samples'];
 list404 = ['https://99papers.com/pricinglol'];
 driver = webdriver.Chrome('D:\\Miha\\Java and JavaRush\\Python\\Test1\\tests\\resources\\chromedriver.exe')


 def checkCode(code,list,driver):
        for url in list:
            driver.get(url)
            r = requests.get(url)
            code_from_server = r.status_code
            if code==code_from_server:
              print("Ok %d" % code_from_server)
            else:
              print('Error, code %d is not matched as expect result %d' % (code_from_server,code) )
            if code_from_server==200:
                  try:
                      assert 'Cheap Essay Writing Service Online' or 'Best Essays for Cheap, Affordable Prices' in driver.title
                      print('Assertion test pass')
                  except Exception as e:
                      print('Error, assertion test failed', format(e))
                  try:
                    element2 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
                    print('Element h1 is found')
                  except Exception as e:
                      print('NoSuchElementException h1',format(e))
                  try:
                       element3=driver.find_element_by_xpath("//meta[@name='description']")
                       re.search("a", element3.get_attribute('content'))
                       print('Description is corrected')
                  except Exception as e:
                       print('Error, description is not corrected',format(e))




 checkCode(200,list200,driver)
 checkCode(301,list301,driver)
 checkCode(404,list404,driver)
 driver.quit()
