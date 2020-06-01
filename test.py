from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pause
import macro_config as mc
import data_cctv
import csv
import selenium.webdriver.support.expected_conditions


driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')
first = True
errorlist = list()
errorlist2 = list()

wait = WebDriverWait(driver, 10)

d = data_cctv.data_cctv()
f = open('cctv_test.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

driver.get(mc.url)

id_elem = wait.until(EC.element_to_be_clickable((By.NAME, "admId")))

pass_elem = driver.find_element_by_name("admPassword")

# mc.url = input("URL : ")
# mc.my_id = input("ID : ")
# mc.my_pw = input("PW : ")

id_elem.send_keys(mc.my_id)
pass_elem.send_keys(mc.my_pw)

login_elem = driver.find_element_by_id("btn_login")
login_elem.click()

site_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[12]/button')
site_elem.click()


for l in rdr:

    if first:
        first = False
        continue



    site2_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[12]/ul[3]/li/a')
    site2_elem.click()

    isEntrance = False
    isExit = False
    isEntrance_Exit = False

    d.site_name = l[0]
    d.address = l[1][:-6]
    d.entrance = l[2]
    d.exit = l[3]
    d.entrance_exit = l[4]
    d.index_array = list()

    site_search = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="schKeyword_siteAll"]')))
    site_search.send_keys(d.site_name)
    site_search.send_keys(Keys.ENTER)
    pause.sleep(0.5)

    try:
        site_list_item = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/main/div/div/div[2]/div[1]/div[2]/a')))
        site_list_item.click()
        print(d.site_name, ", ", site_list_item.text)
    except Exception:
        print(d.site_name+"에서 문제 발생. 해당 사이트 없음.")
        errorlist.append(d.site_name)
        continue

f.close()
