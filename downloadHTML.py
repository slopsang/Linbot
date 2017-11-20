from selenium import webdriver
import time


chromedriver = webdriver.Chrome()
myemail = 'simonsokim@naver.com'
mypassword = 'simonsokimnavercom'

# login function 
def login_linkedin(myemail, mypassword):
	
	url = 'https://www.linkedin.com'

	chromedriver.get(url)

	# print chromedriver.page_source

	# email
	email = chromedriver.find_element_by_xpath('//*[@id="login-email"]')
	email.send_keys(myemail)
	#email.send_keys('simonsokim@naver.com')

	# password
	password = chromedriver.find_element_by_xpath('//*[@id="login-password"]')
	password.send_keys(mypassword)
	#password.send_keys('simonsokimnavercom')

	# sign-in button click
	sign_in = chromedriver.find_element_by_xpath('//*[@id="login-submit"]')
	sign_in.click()

	time.sleep(5)


# login function
login_linkedin( myemail, mypassword )

//*[@id="ember3261"]/button
//*[@id="ember3164"]/div/div[3]
//*[@id="ember801"]/div[6]
//*[@id="ember10333"]/button
//*[@id="ember10326"]/div/div[3]
//*[@id="ember848"]/div[6]/div[4]
//*[@id="ember848"]/div[6]



#search_input = chromedriver.find_element_by_xpath('//*[@id="ember957"]/search_inputut')
search_input = chromedriver.find_element_by_xpath('//*[@id="nav-typeahead-wormhole"]/div/artdeco-typeahead/artdeco-typeahead-input/input')

search_input.send_keys('Java')

search_button = chromedriver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button')
search_button.click()

#people_only = chromedriver.find_element_by_xpath('//*[@id="ember801"]/div[6]/div[4]/div[1]/ul/li[2]/button')
#people_only.click()

time.sleep(50)

chromedriver.quit()
