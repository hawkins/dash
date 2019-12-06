from os import getenv
from sys import stderr
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

from scrape_widget import ScrapeWidget


class WMATAScrapeWidget(ScrapeWidget):
    def render(self) -> str:
        # Log in to WMATA
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        card_id = getenv("WMATA_CARD_ID")
        username = getenv("WMATA_USERNAME")
        password = getenv("WMATA_PASSWORD")

        driver.get(
            f"https://smartrip.wmata.com/Card/CardSummary.aspx?card_id={card_id}"
        )
        el_username = driver.find_element_by_name(
            "ctl00$ctl00$MainContent$MainContent$txtUsername"
        )
        el_username.send_keys(username)
        el_password = driver.find_element_by_name(
            "ctl00$ctl00$MainContent$MainContent$txtPassword"
        )
        el_password.send_keys(password)
        el_submit = driver.find_element_by_name(
            "ctl00$ctl00$MainContent$MainContent$btnSubmit"
        )
        el_submit.click()

        # Check balance
        css_balance = "#left_wide > div.cardSummary > h2 > b"
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_balance))
        )
        return f"${element.text}"
