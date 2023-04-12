import pytest
from selenium import webdriver
from selenium.webdriver.common. service import Service
from pageobject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.CustomLogger import LogGen


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    logger = LogGen.loggen()

    @pytest.mark.regresion

    def test_homePageTitle(self,setup):

        self.logger.info("*************Test_001_login************")
        self.logger.info("***************verifying Home page Title**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title1 = self.driver.title
        if act_title1 == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********************Home page title test is passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********************Home page title is failed*************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self,setup):
        self.logger.info("*************Verifying login test************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title2 = self.driver.title
        if act_title2 == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**********************login test is passed****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**********************Home page title test is failed****************")
            assert False





