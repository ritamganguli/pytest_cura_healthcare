import time
from selenium.webdriver.support.ui import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        title = self.driver.title
        print("Page title:", title)
        return title


    def book_appointment(self):
        self.driver.find_element_by_css_selector("a[id='btn-make-appointment']").click()
        time.sleep(10)

    def enter_username_password(self):
        self.driver.find_element_by_id("txt-username").send_keys("John Doe")
        time.sleep(5)
        self.driver.find_element_by_id("txt-password").send_keys("ThisIsNotAPassword")
        time.sleep(5)

    def click_login(self):
        self.driver.find_element_by_id("btn-login").click()
        time.sleep(10)
    def get_current_url(self):
        url=self.driver.current_url
        return url
    def select_dropdown_option(self):
        dropdown = Select(self.driver.find_element_by_id("combo_facility"))
        dropdown.select_by_index(2)
        time.sleep(5)
    def select_checkbox(self):
        self.driver.find_element_by_id("chk_hospotal_readmission").click()
        time.sleep(10)
    def select_date(self):
        self.driver.find_element_by_id("txt_visit_date").send_keys("04/02/2024")
        time.sleep(5)
        self.driver.find_element_by_id("txt_visit_date").click()
        time.sleep(10)
    def add_comment(self):
        self.driver.find_element_by_id("txt_comment").send_keys("Kuch Bhi...")
        time.sleep(10)
    def book_appointment_button(self):
        scroll_position = (60 / 100) * self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(5)
        self.driver.find_element_by_id("btn-book-appointment").click()
        time.sleep(10)
    def booking_conformation(self):
        book_confirm=self.driver.find_element_by_xpath("//p[@class='lead']").text
        return book_confirm
        
    
    
