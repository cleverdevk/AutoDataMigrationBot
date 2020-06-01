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
f = open('cctv_add.csv', 'r', encoding='utf-8')
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

site_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[3]/button')
site_elem.click()

site2_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[3]/ul[3]/li/a')
site2_elem.click()

def add_cctv(site_name, cctv_name, cctv_number, cctv_address, cctv_area_index):
    cctv_add = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/main/div/div/div[2]/a')))
    cctv_add.click()

    cctv_site_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="siteId_fake"]')))
    cctv_site_name.click()

    cctv_site_search = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search_siteId"]')))
    cctv_site_search.send_keys(site_name)

    cctv_site_search_ok = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div/div/button[1]')
    cctv_site_search_ok.click()

    pause.sleep(3)

    cctv_site_check = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[1]/div[2]/table/tbody/tr[1]/td[1]')))
    cctv_site_check.click()

    cctv_site_ok = driver.find_element_by_xpath('//*[@id="search_modal_success_btn"]')
    cctv_site_ok.click()

    pause.sleep(0.3)
    cctv_area_dropdown = Select(driver.find_element_by_xpath('//*[@id="areaId"]'))
    cctv_area_dropdown.select_by_visible_text(cctv_name)

    cctv_name_label = driver.find_element_by_xpath('//*[@id="cctvName"]')
    cctv_name_label.send_keys(cctv_name)

    # if len(cctv_number) == 1:
    #     cctv_number = "0" + cctv_number
    # cctv_address = str(cctv_address) + str(cctv_number) + "_rec"
    cctv_address = str(cctv_address) + str(cctv_number)

    cctv_address_label = driver.find_element_by_xpath('//*[@id="cctvAddress"]')
    cctv_address_label.send_keys(cctv_address)

    cctv_area_register = driver.find_element_by_xpath('//*[@id="btn_reigster"]')
    cctv_area_register.click()

    cctv_area_register_ok = driver.find_element_by_xpath('//*[@id="confirm_register"]/div/div/button[1]')
    cctv_area_register_ok.click()

    print(site_name + " [" + cctv_name + "] 입력 완료.")

    return

for l in rdr:
    if first:
        first = False
        continue

    isEntrance = False
    isExit = False
    isEntrance_Exit = False

    d.site_name = l[0]
    d.address = l[1]
    d.entrance = l[2]
    d.exit = l[3]
    d.entrance_exit = l[4]
    d.index_array = list()

    #print(d.address)

    site_search = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="schKeyword_siteAll"]')))
    site_search.clear()
    site_search.send_keys(d.site_name)
    site_search.send_keys(Keys.ENTER)
    pause.sleep(0.5)

    try:
        site_list_item = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/main/div/div/div[2]/div[1]/div[2]/a')))
        site_list_item.click()
        # if d.site_name == site_list_item.text:
        #     print(d.site_name,",", site_list_item.text)
        # else:
        #     print('[ERR] 불일치 : ', d.site_name, site_list_item.text)
    except Exception:
        print(d.site_name+"에서 문제 발생. 해당 사이트 없음.")
        errorlist.append(d.site_name)
        continue




    if len(d.entrance) > 0:
        isEntrance = True
        d.index_array.append(1)
    else:
        d.index_array.append(-1)
    if len(d.exit) > 0:
        isExit = True
        if d.index_array[0] == 1:
            d.index_array.append(2)
        else:
            d.index_array.append(1)
    else:
        d.index_array.append(-1)
    if len(d.entrance_exit) > 0:
        isEntrance_Exit = True
        if d.index_array[1] == 2:
            d.index_array.append(3)
        elif d.index_array[1] == 1:
            d.index_array.append(2)
        else:
            d.index_array.append(1)
    else:
        d.index_array.append(-1)



    site_area_add = driver.find_element_by_xpath('//*[@id="regist-toggle-button"]')
    site_area_label = driver.find_element_by_xpath('//*[@id="regist-field"]')
    site_area_ok = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div[2]/div[2]/form/div[3]/div/div/button')

    site_area_add.click()

    if isEntrance:
        site_area_label.send_keys('입구')
        site_area_ok.click()
        print(d.site_name + " [입구] 구역 등록완료.")
    pause.sleep(1)
    if isExit:
        site_area_label.clear()
        site_area_label.send_keys('출구')
        site_area_ok.click()
        print(d.site_name + " [출구] 구역 등록완료.")
    pause.sleep(1)
    if isEntrance_Exit:
        site_area_label.clear()
        site_area_label.send_keys('입/출구')
        site_area_ok.click()
        print(d.site_name + " [입/출구] 구역 등록완료.")
    pause.sleep(3)

    cctv_side = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[23]/a')
    cctv_side.click()

    if isEntrance:
        add_cctv(d.site_name, "입구", d.entrance, d.address, d.index_array[0])
    if isExit:
        add_cctv(d.site_name,"출구",d.exit,d.address, d.index_array[1])
    if isEntrance_Exit:
        add_cctv(d.site_name,"입/출구",d.entrance_exit,d.address, d.index_array[2])

    site_elem = driver.find_element_by_xpath('/html/body/div[1]/nav/ul/li[3]/button')
    site_elem.click()

    site2_elem = driver.find_element_by_xpath('/html/body/div[1]/nav/ul/li[3]/ul[3]/li/a')
    site2_elem.click()

print("error = ", errorlist)

f.close()
