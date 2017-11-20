from selenium import webdriver

chromedriver = webdriver.Chrome(executable_path = '/Users/simon/Documents/Simon/Projects/linbot/chromedriver.exe')

url = 'https://www.linkedin.com/'

chromedriver.get(url)

print chromedriver.page_source

chromedriver.quit()