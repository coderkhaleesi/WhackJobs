# import web driver
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

sleep(1)
login_button = driver.find_element_by_class_name('nav__button-secondary')

login_button.click()
sleep(0.5)
username = driver.find_element_by_id('username')
sleep(0.5)
username.send_keys('universalapproximation@gmail.com')
password = driver.find_element_by_id('password')
sleep(1)
password.send_keys('zmG6?bME&9c#Th.')
sleep(0.5)
signin = driver.find_element_by_class_name('btn__primary--large')
sleep(1)
signin.click()
sleep(2)
driver.get('https://www.linkedin.com/jobs/')
job_search_box = driver.find_element_by_class_name('jobs-search-box__text-input')
job_search_box.send_keys("Data")
location = driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location')]")
location.send_keys('Worldwide')
job_submit = driver.find_element_by_class_name('jobs-search-box__submit-button')
job_submit.click()


current_page = driver.find_element_by_class_name('active')

current_page.click()


pages = driver.find_element_by_class_name("artdeco-pagination__pages")

pages_li = pages.find_elements_by_tag_name('li')

for page in pages_li:
    butn = page.find_element_by_xpath("//button")
    print(page.text)