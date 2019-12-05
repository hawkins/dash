#!/usr/bin/env python3

from abc import ABC, abstractmethod
from os import getenv
from sys import stderr
from typing import Optional

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


class Widget(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def evaluate(self) -> str:
        return ""


class ScrapeWidget(Widget):
    __driver: Optional[webdriver.Firefox] = None

    @property
    def driver(self) -> webdriver.Firefox:
        if self.__driver is None:
            driver_options = Options()
            driver_options.headless = True
            self.__driver = webdriver.Firefox(options=driver_options)

        return self.__driver


class EZPVAScrapeWidget(ScrapeWidget):
    def __init__(self):
        username = getenv("EZPVA_USERNAME")
        password = getenv("EZPVA_PASSWORD")
        self.driver.get("https://www.ezpassva.com/Login/Login.aspx")
        el_username = self.driver.find_element_by_name(
            "ctl00$VDOTContentPlaceHolder$txtUserName"
        )
        el_username.send_keys(username)
        el_password = self.driver.find_element_by_name(
            "ctl00$VDOTContentPlaceHolder$txtPassword"
        )
        el_password.send_keys(password)
        el_submit = self.driver.find_element_by_name(
            "ctl00$VDOTContentPlaceHolder$btnLogin"
        )
        el_submit.click()

    def evaluate(self) -> str:
        # Check balance
        css_balance = "#ctl00_VDOTContentPlaceHolder_grdAccountInfo > tbody > tr:nth-child(6) > td:nth-child(2)"
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_balance))
        )
        return element.text


if __name__ == "__main__":
    b = EZPVAScrapeWidget()

    print(f"returns: {b.evaluate()}")
