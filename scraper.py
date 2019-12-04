import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

# Open up Firefox to visit webpage
browser = webdriver.Firefox()
browser.get("https://www.comparethemarket.com/")

# Extract listsof "buyers and "prices based on xpath
cars = browser.find_element_by_xpath('//*[@id="Market_HomePage_HomepageHeroBlock_CarInsurance"]')
cars.click()

# Time delay
time.sleep(20)

# Search for vehicles by Manufacturer, Model and Year
# reg_unknown = browser.find_element_by_xpath("//*[@id=CarInsurance_YourVehicle_ManualVehicleLookup_Manufacturer]")
# reg_unknown.click()

# manufacturer_element = browser.find_element_by_xpath("//*[@id=CarInsurance_YourVehicle_ManualVehicleLookup_Manufacturer]")
# actions = ActionChains(browser)
# actions.move_to_element(manufacturer_element).perform()
# manufacturer = "/html/body/div[1]/div[1]/div/div[1]/div/section/div/div/fieldset[2]/div/div[1]/select/option[44]"
# wait(browser, 5).until(EC.visibility_of_element_located(By.XPATH, manufacturer)).click()

car_model_element = None 