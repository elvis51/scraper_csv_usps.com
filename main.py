# import library
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# url request site
URL = 'https://tools.usps.com/zip-code-lookup.htm?byaddress'

# open data csv
with open("input.csv", "r") as f:
    input_data = csv.DictReader(f)
    # create data csv vith check
    with open('new_data.csv', 'w', newline='') as f:
        fieldnames = ['Company', 'Street', 'City', 'St', 'ZIPCode', 'valid']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    # function for check data
    for k in input_data:
        # get dickt for chek
        keys = list(k.values())
        # print(keys)

        # add driver
        web = webdriver.Chrome()
        web.get(URL)
        # submit form fields
        Company = keys[0]
        tCompany = web.find_element(By.XPATH, '//*[@id="tCompany"]')
        tCompany.send_keys(Company)

        Address = keys[1]
        tAddress = web.find_element(By.XPATH, '//*[@id="tAddress"]')
        tAddress.send_keys(Address)

        City = keys[2]
        tCity = web.find_element(By.XPATH, '//*[@id="tCity"]')
        tCity.send_keys(City)

        State = keys[3]
        tState = Select(web.find_element(By.XPATH, '//*[@id="tState"]'))
        tState.select_by_value(State)

        Zip = keys[4]
        tZip = web.find_element(By.XPATH, '//*[@id="tZip-byaddress"]')
        tZip.send_keys(Zip)

        Find = web.find_element(By.ID, 'zip-by-address')
        Find.click()


        confirmation = web.find_element(By.ID, 'street-address')
        # print(confirmation.text)
        # check valid adress or not
        if confirmation.text == Address:
            vaild = 'Vaild'
            print(vaild)

        else:
            vaild = 'Not_Vaild'
            print("error")
        #add data to new file
        with open('new_data.csv', 'a', newline='') as f:
            fieldnames = ['Company', 'Street', 'City', 'St', 'ZIPCode', 'valid']
            writer = csv.DictWriter(f,fieldnames = fieldnames)
            writer.writerow({'Company': keys[0],
                             'Street': keys[1],
                             'City': keys[2],
                             'St': keys[3],
                             'ZIPCode': keys[4],
                             'valid': vaild, })

            continue
