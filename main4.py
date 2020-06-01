from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pause
import macro_config as mc
import developer_data
import csv
import selenium.webdriver.support.expected_conditions

first = True

driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')

errorlist = list()
errorlist2 = list()

wait = WebDriverWait(driver, 10)

d = developer_data.data()
f = open('developer_mode.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

driver.get(mc.url)

id_elem = wait.until(EC.element_to_be_clickable((By.NAME, "admId")))

pass_elem = driver.find_element_by_name("admPassword")

id_elem.send_keys(mc.my_id)
pass_elem.send_keys(mc.my_pw)

login_elem = driver.find_element_by_id("btn_login")
login_elem.click()

site_elem = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/nav/ul/li[3]/button')))
site_elem.click()

site_elem2 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/nav/ul/li[3]/ul[1]/li/a')))
site_elem2.click()
for l in rdr:

    if first:
        first = False
        continue

    d.site_name = l[0]
    d.developer = l[1]

    search_box = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/div/div[2]/div/input')))
    search_box.clear()
    search_box.send_keys(d.site_name)

    search_btn = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[3]/div/div[2]/div/div/button[1]')
    search_btn.click()


    detail = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/main/div/div/div/div[4]/table/tbody/tr/td[1]/button')))
    detail.click()

    developAdminSearch = driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/form/div/table/tbody/tr[7]/td[1]/div/div/button')
    developAdminSearch.click()
    devSearchArea = driver.find_element_by_id('search_action1')
    devSearchButton = driver.find_element_by_xpath('//*[@id="search-modal"]/div/div[1]/div[1]/div/div/div/div/button[1]')
    devSearchArea.send_keys(d.developer)
    devSearchButton.click()
    try:
        devCheckbox = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="action1_ItemList"]/tr/td[1]')))
        devCheckbox.click()
        devOkButton = driver.find_element_by_xpath('//*[@id="search_modal_success_btn"]').click()

        site_elem3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btn_modify"]')))
        site_elem3.click()

        site_elem4 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="confirm_regi"]/div/div/button[1]')))
        site_elem4.click()

        print(d.site_name, " 성공")

    except:
        print(d.site_name, "에서 개발자 없음.")
        errorlist.append(d.site_name)

        site_elem2 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/nav/ul/li[3]/ul[1]/li/a')))
        site_elem2.click()






print(errorlist)
print(errorlist2)


