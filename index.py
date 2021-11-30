from selenium import webdriver
import os

if __name__ == '__main__':
 
	chromedriver = "./chromedriver" 
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver) #模拟打开浏览器
	driver.get("https://www.baidu.com/") #打开网址
	driver.maximize_window() #窗口最大化（无关紧要哈）
	
	html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
	print(html)
	driver.quit()

