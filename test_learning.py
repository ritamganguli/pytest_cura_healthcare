import time
from BaseClass import BaseClass
from mainpage import LoginPage



class TestCase(BaseClass):
    
    def test_title(self):
        log=self.getLogger()
        login_page = LoginPage(self.driver)
        if login_page.get_title()=="CURA Healthcare Service":
            log.info("The title of the page is: "+login_page.get_title())
        if login_page.get_title()!="CURA Healthcare Service":
            log.warn("The title of the page is: "+login_page.get_title())
        print(login_page.get_title())
        login_page.book_appointment()
        log.info("Proceeding with booking the appointment")
        login_page.enter_username_password()
        log.info("Entering The Username And Password")
        login_page.click_login()
        log.info("Proceeding with login")
        if "appointment" in login_page.get_current_url():
            log.info("Succefully verified that the person is on appointment page")
        login_page.select_dropdown_option()
        login_page.select_checkbox()
        log.info("Selected Seol Cura Health Care Center")
        login_page.select_date()
        log.info("Selected Date")
        login_page.book_appointment_button()
        log.info("Clicked On Appointment Button")
        if login_page.booking_conformation()=="Please be informed that your appointment has been booked as following:":
            print("Test Case Passed")
            log.info("Successfully booked the appointment")