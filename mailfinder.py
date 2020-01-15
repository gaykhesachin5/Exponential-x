from selenium import webdriver
import requests
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
import csv

driver = None
i=1
email_combination = []
red_fname = []
red_lname = []
red_desig = []
red_cname = []
red_loc = []
red_dom = []
red_mailid = []
green_fname = []
green_lname = []
green_desig = []
green_cname = []
green_loc = []
green_dom = []
green_mailid = []

def main():
    try:
        driver = webdriver.Firefox( executable_path = "C:\\Users\\Soft Access\\Desktop\\Lead_Generation_Automation_Tool_Project\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver.get('http://mailtester.com/testmail.php')
        reader = csv.DictReader(open("products.csv"))
        time.sleep(2)
    except Exception as e:
        print(e)
    for raw in reader:
        f=False
        fname = raw['First Name']
        lname = raw['Last Name']
        domain = raw['Domain']
        temp= fname + lname + domain
        email_combination.append(temp)
        temp = fname + '.' +lname+domain
        email_combination.append(temp)
        temp = fname[0] + lname+domain
        email_combination.append(temp)
        temp = fname+domain
        email_combination.append(temp)
        for i in email_combination:
            wait = WebDriverWait(driver, 10)
            inpt = wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td/input'))
            )
            time.sleep(1)
            inpt.send_keys(i)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[2]/td/input').click()
            time.sleep(2)
            flag = driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[1]/td[1]').get_attribute('bgcolor')
            driver.find_element_by_xpath('//*[@id="content"]/form/table/tbody/tr[1]/td/input').clear()
            if(flag == '#00DD00'):
                green_fname.append(raw['First Name'])
                green_lname.append(raw['Last Name'])
                green_desig.append(raw['Designation'])
                green_cname.append(raw['Company Name'])
                green_loc.append(raw['Location'])
                green_dom.append(raw['Domain'])
                green_mailid.append(i)
                f=True
                break
        #FFBB00 -> Orange
        #00DD00 -> Green
        #FF4444 -> Red
        if(f==False):
            red_fname.append(raw['First Name'])
            red_lname.append(raw['Last Name'])
            red_desig.append(raw['Designation'])
            red_cname.append(raw['Company Name'])
            red_loc.append(raw['Location'])
            red_dom.append(raw['Domain'])    
        email_combination.clear()
    driver.close()
    writeInCSV()

def writeInCSV():
    red = pd.DataFrame({'First Name':red_fname,'Last Name':red_lname,'Designation': red_desig, 'Company Name' : red_cname,'Location': red_loc,'Domain': red_dom })
    green = pd.DataFrame({'First Name':green_fname,'Last Name':green_lname,'Designation': green_desig, 'Company Name' : green_cname,'Location': green_loc,'Domain': green_dom ,'Email' : green_mailid })

    red.to_csv('red.csv', index=True, index_label='Sr. No.', encoding='utf-8')
    green.to_csv('green.csv', index=True, index_label='Sr. No.', encoding='utf-8')
    print('Successfully Done !!')

if __name__ == "__main__":
    main()
