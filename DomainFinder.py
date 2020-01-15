from selenium import webdriver
import requests
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import csv


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


green_fname = []
green_lname = []
green_desig = []
green_cname = []
green_loc = []
green_dom = []
global driver

        

def main():
    try:
        driver = webdriver.Firefox( executable_path = "C:\\Users\\Soft Access\\Desktop\\Lead_Generation_Automation_Tool_Project\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver.get('https://www.google.com/maps')
        global reader
        reader = csv.DictReader(open("fordomain.csv"))
        time.sleep(2)
    except Exception as e:
        print(e)
    for raw in reader:
        company_name = raw['Company Name']
        location = raw['Location']
        #cname_location = company_name + ', ' + location
        print(company_name)
        wait = WebDriverWait(driver, 10)
        inpt = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')) 
        )
        time.sleep(1)
        inpt.send_keys(company_name)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
        time.sleep(3)
        try:
            dom = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[10]/div/div[1]/span[3]/span[3]').text
            time.sleep(2)
        except Exception:
            try:
                driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[9]/div/div[1]/div/div/div[2]/div[1]/div[1]').click()
                time.sleep(2)
                dom = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[9]/div/div[1]/div/div/div[11]/div/div[1]/span[3]/span[3]').text
                time.sleep(2)
            except Exception:
                driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/a').click() 
                time.sleep(1)
                continue
        green_fname.append(raw['First Name'])
        green_lname.append(raw['Last Name'])
        green_desig.append(raw['Designation'])
        green_cname.append(raw['Company Name'])
        green_loc.append(raw['Location'])
        green_dom.append(dom)
        print(dom)
        driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/a').click() 
    driver.close()
    print(green_dom)
    print(green_fname)
    writeInCSV()

def writeInCSV():
    green = pd.DataFrame({'First Name':green_fname,'Last Name':green_lname,'Designation': green_desig, 'Company Name' : green_cname,'Location': green_loc,'Domain': green_dom})
    green.to_csv('foremail.csv', index=True, index_label='Sr. No.', encoding='utf-8')
    print('Successfully Done !!')

if __name__ == "__main__":
    main()
