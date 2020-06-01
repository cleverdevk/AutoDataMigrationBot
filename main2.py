from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pause
import macro_config as mc
import data_fee
import csv
import selenium.webdriver.support.expected_conditions


driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')
first = True
errorlist = list()
errorlist2 = list()

wait = WebDriverWait(driver, 10)

d = data_fee.data_fee()
f = open('fee_final.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

driver.get(mc.url)

parkingsysdictionary = {"LPR": 1, "Flap":2,"Gate":3,"주차권":4, "PP":4, "RF":3, "발권형":4, "리모컨":3, "리모콘":3}
systemdictionary = {"LPR": 1, "PP":2,"Flab Card":3,"RF":4, "원거리RF":5, "Gate":6, "터치식RF":7, "티머니카드(원거리RF)":8, "리모컨":9, "없음":10, "pp":2}

id_elem = wait.until(EC.element_to_be_clickable((By.NAME, "admId")))

pass_elem = driver.find_element_by_name("admPassword")

# mc.url = input("URL : ")
# mc.my_id = input("ID : ")
# mc.my_pw = input("PW : ")

id_elem.send_keys(mc.my_id)
pass_elem.send_keys(mc.my_pw)

login_elem = driver.find_element_by_id("btn_login")
login_elem.click()

site_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[3]/button')
site_elem.click()

site2_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[3]/ul[4]/li/a')
site2_elem.click()


for l in rdr:
    if first == True:
        first = False
        continue
    try:
        site3_elem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/form/div[1]/a")))
        site3_elem.click()
        if d.site_name is not None:
            print(d.site_name + "입력 완료")
    except Exception:
        print(d.site_name + " 데이터에서 문제 발생")
        errorlist2.append(d.site_name)
        site2_elem = driver.find_element_by_xpath('/html/body/div[1]/nav/ul/li[12]/ul[4]/li/a')
        site2_elem.click()
        site3_elem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/form/div[1]/a")))
        site3_elem.click()

    for i in range(0,len(l)):
        str = ''''''
        str += l[i]

        if i == 0:
            d.site_name = str
        if i == 1:
            d.parkingType = str
        if i == 2:
            d.systemType = str
        if i == 3:
            d.isAdmin = str[:2]
        if i == 4:
            d.parkingNum = str
        if i == 5:
            d.fee = str
        if i == 6:
            d.max_fee = str
        if i == 7:
            d.penalty = str
        if i == 8:
            d.membership = str
        if i == 9:
            d.promotion = str
        if i == 10:
            d.memo = str

    print(len(d.penalty))
    d.dataNoneCheck(errorlist2)

    site_search = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="frm_parkingLotsPay"]/div/table/tbody/tr[1]/td/div/div[2]/button')))
    site_search.click()

    site_search_text = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search_siteId"]')))
    site_search_text.send_keys(d.site_name)

    site_search_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-modal"]/div/div[1]/div[1]/div/div/div/div/button[1]')))
    site_search_button.click()

    site_search_check = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="siteId_ItemList"]/tr/td[1]/div')))
    site_search_check.click()

    site_search_OK = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search_modal_success_btn"]')))
    site_search_OK.click()

    parkingType = Select(driver.find_element_by_name('parkingTypes'))
    systemType = Select(driver.find_element_by_name('seasonTicketDivide'))


    keys = parkingsysdictionary.keys()
    if d.parkingType in keys:
        parkingType.select_by_index(parkingsysdictionary[d.parkingType])
    else:
        print(d.site_name + "에서 오류 발생. 주차 타입 오류, 해당 타입 : " + d.parkingType)
        errorlist2.append(d.site_name)
        continue


    keys = systemdictionary.keys()
    if d.systemType in keys:
        systemType.select_by_index(systemdictionary[d.systemType])
    else:
        print(d.site_name + "에서 오류 발생. 시스템 타입 오류, 해당 타입 : " + d.systemType)
        errorlist2.append(d.site_name)
        continue

    adminRadioTrue = driver.find_element_by_xpath('//*[@id="frm_parkingLotsPay"]/div/table/tbody/tr[4]/td/label[1]/label')
    adminRadioFalse = driver.find_element_by_xpath('//*[@id="frm_parkingLotsPay"]/div/table/tbody/tr[4]/td/label[2]/label')

    if d.isAdmin == "유인":
        adminRadioTrue.click()
    if d.isAdmin == "무인":
        adminRadioFalse.click()

    parkingNum = driver.find_element_by_xpath('//*[@id="vehicleAmount"]')
    fee = driver.find_element_by_xpath('//*[@id="price"]')
    max_fee = driver.find_element_by_xpath('//*[@id="maxPrice"]')
    penalty = driver.find_element_by_xpath('//*[@id="lostPrice"]')
    membership = driver.find_element_by_xpath('//*[@id="seasonTicketPrice"]')
    promotion = driver.find_element_by_xpath('//*[@id="salePrice"]')
    memo = driver.find_element_by_xpath('//*[@id="memo"]')

    parkingNum.send_keys(d.parkingNum)
    fee.send_keys(d.fee)
    max_fee.send_keys(d.max_fee)
    penalty.send_keys(d.penalty)
    membership.send_keys(d.membership)
    promotion.send_keys(d.promotion)
    memo.send_keys(d.memo)

    Okbutton = driver.find_element_by_xpath('//*[@id="btn_register"]')
    Okbutton.click()
    okokbutton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="confirm_regi"]/div/div/button[1]')))
    okokbutton.click()



    print("errorlist2 = ", errorlist2)

    # pause.sleep(10)




















print(errorlist)
print(errorlist2)
f.close()
