from typing import Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from widget import Widget


class ScrapeWidget(Widget):
    __driver: Optional[webdriver.Firefox] = None

    @property
    def driver(self) -> webdriver.Firefox:
        if self.__driver is None:
            driver_options = Options()
            driver_options.headless = True
            self.__driver = webdriver.Firefox(options=driver_options)

        return self.__driver
