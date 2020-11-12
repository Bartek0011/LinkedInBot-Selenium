from selenium import webdriver
import time
from sec import passd


class LinkedIn:
    def __init__(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.linkedin.com//")
        time.sleep(0.1)
        self.driver.find_element_by_xpath('//*[@id="session_key"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="session_password"]').send_keys(passd)
        time.sleep(0.1)
        self.driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click()
        time.sleep(0.4)

    def invite_new(self, search_title):
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ember16"]/input').send_keys(search_title)
        time.sleep(0.1)
        self.driver.find_element_by_xpath('//*[@id="ember16"]/input').send_keys(u'\ue007')
        time.sleep(4)
        self.driver.find_element_by_css_selector("[aria-label='Zobacz wyniki tylko dla Osoby']").click()    
        self.ul_buttons()

    def ul_buttons(self):
	for page_number in range(1, 25):  # go through 25 pages
		if page_number != 1:  # next page
			self.driver.find_element_by_css_selector("[aria-label='Strona {}']".format(page_number)).click()
		time.sleep(3)

		for position in [400, 650, 900, 1150, 900, 650, 400, 0]:
		    self.driver.execute_script("window.scrollTo(0, {})".format(position))  # scroll as human, up and down
		    time.sleep(0.3)
		time.sleep(1)

		position = 1
		users_ul = self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[2]/div/div[2]/div/div/div/ul')
		for button in users_ul.find_elements_by_tag_name('button'):

		    try:
		        button.click()
		    except:
		        print("no button")

		    time.sleep(0.5)
		    try:
		        self.driver.find_element_by_css_selector("[aria-label='Wyślij teraz']").click()
		    except:
		        print("there's no Send now")
		    time.sleep(0.5)
		    # try:
		    #     self.driver.find_element_by_css_selector("[aria-label='Dodaj notatkę']").click()
		    # except RuntimeError:
		    #     print("there's no Add note")
		    # time.sleep(0.5)
		    try:
		        self.driver.find_element_by_css_selector("[aria-label='Odrzuć']").click()
		    except:
		        print("there's no Reject")
		    time.sleep(1)
		    position += 1
		    self.driver.execute_script("window.scrollTo(0, {})".format(position * 130))
		    time.sleep(2)

        time.sleep(0.4)


bot = LinkedIn('')  # type your username or email here
bot.invite_new('')  # type yout topic here
