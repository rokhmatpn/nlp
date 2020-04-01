from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import requests
import urllib, urllib2, json

import glob
import os
import io
import datetime, time

# INR_API = "https://api.kgnewsroom.com/api/"
# TOKEN = "Ita4en7cj64a471AacsYbP2GRjAe8hzTmEfJiS87aQTPI_7ZHvLMsxEN0NyZa1z0AWxW5f-bXmqTyRV09ZBuyzIO7zd1lplvlhwpp8DT_eqCb9BreDzZP1HJF258WZV81zWwClOwEh3W3dwU-FmtNvvTKP1CcWKeU4wnzLDLMNpzRMqiucXm_w9zjdsPUth4n4ym1CnrzFulQShsVGq8Fbsz4hwZcZuZLkkt7kz58covIIko--b8rrr0K5UGd5Wp_H9P7oVmPo4YVJ2ryIdoqfn6l0qWnBeUZox4O1ccXkO6AWeFN3bggEdk61c90G-xqCzFqFBXZUilrn7cTfh5ngumdG6v9LM8ZW7l6ZEz0EpnSnuQOiPe-_HqLhoL4qpDQzo1s1Q_D0JdEQWiKxJ2cPwRvFiTEoGG1VZeTjfZuTzgofm-_bGntXEfnG4eCYopIaeYMQ"

driver = webdriver.ChromeOptions() 
driver.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=driver)

driver.get("https://web.whatsapp.com/send?phone=6281316262616") 
wait = WebDriverWait(driver, 60)

dirt = 'D:/MASTER/whatsappapi/file/'

def load_main():

	while 1:

		time.sleep(10)
		print str(datetime.datetime.now())[:19]+" loop"

		data_index = os.listdir(dirt+'contact/') 
		total_files = len(data_index)
		if total_files>0:
			add_user()
		else:
			send_wa()


def send_wa():

	os.chdir(dirt+'msg/')
	for file in glob.glob("*.json"):
		if os.path.exists(dirt + 'msg/' +file):
			with open(dirt + 'msg/' +file) as f:
				data_index = json.load(f)
				for row in data_index:

					try:
						print "process send msg"

						msg = row['msg']

						number = str(row['target'])
						number = number.replace('+62', '0', 1)
						number = number.replace('0', '62', 1)

						f.close()
						os.remove(dirt + 'msg/' +file) 

						number_1 = number[0:2];
						number_1 = number_1.replace('62', '+62')
						number_2 = number[2:5];
						number_3 = number[5:9];
						number_4 = number[9:14];

						target = number_1+' '+number_2+'-'+number_3+'-'+number_4
						target = '"'+target+'"'

						x_arg = '//span[contains(@title,' + target + ')]'
						group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
						group_title.click() 

						msg_box = driver.find_element_by_class_name('_2S1VP')

						msg_box.send_keys(msg)
						button = driver.find_element_by_class_name('_35EW6')
						button.click()
						print "Send message success"
						
					except Exception, e:

						try:
							print "process add contact"

							number = str(row['target'])
							number = number.replace('+62', '0', 1)
							number = number.replace('0', '62', 1)
							msg = row['msg']

							driver.get("https://web.whatsapp.com/send?phone="+number+"&text="+msg)
							time.sleep(10)

							# button = driver.find_element_by_id('action-button')
							# button.click()
							# time.sleep(10)

							button = driver.find_element_by_class_name('_35EW6')
							button.click()
							print "Add contact success"

						except Exception, e:
							print "Invalid number"
							if os.path.exists(dirt + 'contact/' +file):
								os.remove(dirt + 'contact/' +file) 

							print "Send message failed"
							if os.path.exists(dirt + 'msg/' +file):
								os.remove(dirt + 'msg/' +file) 

							driver.get("https://web.whatsapp.com/")
			time.sleep(5)

def add_user():

	os.chdir(dirt+'contact/')
	for file in glob.glob("*.json"):
		if os.path.exists(dirt + 'contact/' +file):
			with open(dirt + 'contact/' +file) as f:
				data_index = json.load(f)
				for row in data_index:

					try:
						print "process add contact"
						number = str(row['number'])
						# msg = str(row['name'])
						# print len(number)

						number = number.replace('+62', '0', 1)
						number = number.replace('0', '62', 1)

						f.close()
						os.remove(dirt + 'contact/' +file) 

						msg = "Your number "+number+"  is connected to the INR System"
						driver.get("https://web.whatsapp.com/send?phone="+number+"&text="+msg)
						time.sleep(5)

						# button = driver.find_element_by_id('action-button')
						# button.click()
						# time.sleep(10)

						button = driver.find_element_by_class_name('_35EW6')
						button.click()
						print "Add contact success"

						
					except Exception, e:
						print "Invalid number"
						if os.path.exists(dirt + 'contact/' +file):
							os.remove(dirt + 'contact/' +file) 

						driver.get("https://web.whatsapp.com/")




if __name__ == "__main__":
	load_main()

