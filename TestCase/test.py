#!/usr/bin/python3
# -*- coding: utf-8 -*-
from util.BrowserDriver import BrowserDriver
from pages.HomePage import HomePage

driver = BrowserDriver('driver')
driver = driver.openbrowser(driver)

homepage = HomePage('driver')
if homepage.is_visibility(homepage.GEO_location_close):
    homepage.click(homepage.GEO_location_close)
elif homepage.is_visibility(homepage.newsletter_popup_close):
    homepage.click(homepage.newsletter_popup_close)
else:
    print('no pop-up appear')
homepage.send_key(homepage.search_box, 'Ray Ban')
homepage.click(homepage.search_button)
