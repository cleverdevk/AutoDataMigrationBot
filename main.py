from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pause
import macro_config as mc
import data
import csv
import selenium.webdriver.support.expected_conditions

first = True

driver = webdriver.Firefox(executable_path=r'C:/geckodriver.exe')

errorlist = list()
errorlist2 = list()

wait = WebDriverWait(driver, 10)

d = data.data()
f = open('last_site.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

driver.get(mc.url)

admindictionary = {"영업1팀": 3, "영업2팀":4,"영업3팀":5,"영남영업팀":6}
developerdictionary = {"영업1팀": "김재빈", "영업2팀":"정종현","영업3팀":"박준호","영남영업팀":"조윤경"}
contractdictionary = {"임대차": 1, "위수탁":2,"수익배분":3,"유지보수":4}
parkingtypedictionary = {"ST": 1, "TPS":2,"PUBLIC":3,"PROJECT":4}
parkingnumtypedictionary = {"소형": 1, "중형":2,"대형":3,"초대형":4}
equipmentdictionary = {"HANMEC": 1, "AMANO" : 2, "NEXPA":4, "PARKING CLOUD":5, "기타":6}
parkingsysdictionary = {"LPR": 1, "Flap":2,"Gate":3,"주차권":4, "PP":4, "RF":3, "발권형":4, "리모컨":3, "리모콘":3}
regiondictionary = {"서울시":1, "경기도":2, "인천시":3, "영남권":4, "강원도":5, "광주시":6, "대전/세종":7, "전북":8, "충남":9, "충북":10}

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



str = '1994-04-16'


for l in rdr:

    if first:
        first = False
        continue
    print(l)
    try:
        site3_elem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div/div[2]/a")))
        site3_elem.click()
        if d.site_name is not None:
            print(d.site_name + "입력 완료")
    except Exception:
        print(d.site_name, " 데이터에서 문제 발생")
        errorlist2.append(d.site_name)
        # site2_elem = driver.find_element_by_xpath('/html/body/div[1]/nav/ul/li[3]/button')
        # site2_elem.click()
        site3_elem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div/div[2]/a")))
        site3_elem.click()

    site_name = wait.until(EC.element_to_be_clickable((By.NAME,'siteName')))
    address2 = wait.until(EC.element_to_be_clickable((By.NAME,'address2')))
    site_code = wait.until(EC.element_to_be_clickable((By.NAME,'siteCode')))
    project_code = wait.until(EC.element_to_be_clickable((By.NAME,'projectCode')))
    work_name = wait.until(EC.element_to_be_clickable((By.NAME,'workName')))
    openAt = wait.until(EC.element_to_be_clickable((By.NAME,'openAt')))
    contractAt = wait.until(EC.element_to_be_clickable((By.NAME,'contractAt')))
    expirationAt = wait.until(EC.element_to_be_clickable((By.NAME,'expirationAt')))
    admingroup = Select(driver.find_element_by_name('adminGroupsId'))
    workStatusTypes = Select(driver.find_element_by_name('workStatusTypes'))
    contractTypes = Select(driver.find_element_by_name('contractTypes'))
    parkingTypes = Select(driver.find_element_by_name('parkingTypes'))
    parkingNum = wait.until(EC.element_to_be_clickable((By.NAME,'parkingLotsNum')))
    parkingNumTypes = Select(driver.find_element_by_name('parkingNumTypes'))
    equipmentName = Select(driver.find_element_by_name('equipmentName'))
    parkingSysTypes = Select(driver.find_element_by_name('parkingSysTypes'))
    region = Select(driver.find_element_by_name('region'))

    d.site_name = l[0]
    d.address = l[1]
    d.admingroup = l[2]
    if l[3] is None or '':
        print(d.site_name + "에서 오류 발생. 사이트 코드 없음")
        continue
    d.site_code = l[3]
    if len(d.site_code) == 1:
        d.site_code = "000" + d.site_code
    if len(d.site_code) == 2:
        d.site_code = "00" + d.site_code
    if len(d.site_code) == 3:
        d.site_code = "0" + d.site_code
    if len(d.site_code) > 4:
        print(d.site_name + "에서 오류 발생. 사이트 코드 오류. 해당 코드 : " + d.site_code)

    d.project_code = l[4]
    d.contractTypes = l[5]
    d.parkingTypes = l[6]
    d.parkingNum = l[7]
    d.parkingNumTypes = l[8]
    d.equipmentName = l[9]
    d.parkingSysTypes = l[10]
    d.region = l[11]
    d.openAt = l[12]
    d.contractAt = l[13]
    d.expirationAt = l[14]

    # if data.isNotNone(d.site_name, d.site_name, errorlist2):
    #     continue
    # if data.isNotNone(d.address, d.site_name, errorlist2):
    #     continue
    if len(d.admingroup) == 0:
        print(d.site_name + "에서 오류 발생. 담당팀 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.project_code) == 0:
        print(d.site_name + "에서 오류 발생. 프로젝트 코드 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.contractTypes) == 0:
        print(d.site_name + "에서 오류 발생. 계약 타입 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.parkingTypes) == 0:
        print(d.site_name + "에서 오류 발생. 주차 타입 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.parkingNum) == 0:
        print(d.site_name + "에서 오류 발생. 면수 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.parkingNumTypes) == 0:
        print(d.site_name + "에서 오류 발생. 면수구분 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.equipmentName) == 0:
        print(d.site_name + "에서 오류 발생. 장비 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.parkingSysTypes) == 0:
        print(d.site_name + "에서 오류 발생. 시스템 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.region) == 0:
        print(d.site_name + "에서 오류 발생. 지역구분 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.openAt) == 0:
        print(d.site_name + "에서 오류 발생. 오픈일자 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.contractAt) == 0:
        print(d.site_name + "에서 오류 발생. 계약일자 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.expirationAt) == 0:
        print(d.site_name + "에서 오류 발생. 만료일자 없음")
        errorlist2.append(d.site_name)
        continue
    if len(d.openAt) != 10:
        print(d.site_name + "에서 오류 발생. 오픈일자 포맷 오류. 해당 오픈일자 : " + d.openAt)
        errorlist2.append(d.site_name)
        continue
    if len(d.contractAt) != 10:
        print(d.site_name + "에서 오류 발생. 계약일자 포맷 오류. 해당 계약일자 : " + d.contractAt)
        errorlist2.append(d.site_name)
        continue
    if len(d.expirationAt) != 10:
        print(d.site_name + "에서 오류 발생. 만료일자 포맷 오류. 해당 만료일자 : " + d.expirationAt)
        errorlist2.append(d.site_name)
        continue

    site_name.send_keys(d.site_name)
    address2.send_keys(d.address)
    site_code.send_keys(d.site_code)
    project_code.send_keys(d.project_code)
    work_name.send_keys(d.site_name)
    openAt.send_keys(d.openAt)
    contractAt.send_keys(d.contractAt)
    expirationAt.send_keys(d.expirationAt)
    parkingNum.send_keys(d.parkingNum)

    admingroup.select_by_index(admindictionary[d.admingroup])
    workStatusTypes.select_by_index(1)
    contractTypes.select_by_index(contractdictionary[d.contractTypes])
    parkingTypes.select_by_index(parkingtypedictionary[d.parkingTypes])
    parkingNumTypes.select_by_index(parkingnumtypedictionary[d.parkingNumTypes])
    equipmentName.select_by_index(equipmentdictionary[d.equipmentName])
    keys = regiondictionary.keys()
    if d.region in keys:
        region.select_by_index(regiondictionary[d.region])
    else:
        print(d.site_name + "에서 오류 발생. 지역구분 오류")
        errorlist2.append(d.site_name)
        continue
    keys = parkingsysdictionary.keys()
    if d.parkingSysTypes in keys:
        parkingSysTypes.select_by_index(parkingsysdictionary[d.parkingSysTypes])
    else:
        print(d.site_name + "에서 오류 발생. 시스템 타입 오류, 해당 타입 : " + d.parkingSysTypes)
        errorlist2.append(d.site_name)
        continue

    developAdminSearch = driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/form/div/table/tbody/tr[7]/td[1]/div/div/button')
    developAdminSearch.click()
    devSearchArea = driver.find_element_by_id('search_action1')
    devSearchButton = driver.find_element_by_xpath('//*[@id="search-modal"]/div/div[1]/div[1]/div/div/div/div/button[1]')
    devSearchArea.send_keys(developerdictionary[d.admingroup])
    devSearchButton.click()
    devCheckbox = driver.find_element_by_xpath('//*[@id="action1_ItemList"]/tr/td[1]')
    devCheckbox.click()
    devOkButton = driver.find_element_by_xpath('//*[@id="search_modal_success_btn"]').click()

    MarketingAdminSearch = driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/form/div/table/tbody/tr[7]/td[2]/div/div/button')
    MarketingAdminSearch.click()
    MarSearchArea = driver.find_element_by_id('search_action2')
    MarSearchButton = driver.find_element_by_xpath('//*[@id="search-modal"]/div/div[1]/div[1]/div/div/div/div/button[1]')
    MarSearchArea.send_keys(developerdictionary[d.admingroup])
    MarSearchButton.click()
    MarCheckbox = driver.find_element_by_xpath('//*[@id="action2_ItemList"]/tr/td[1]')
    MarCheckbox.click()
    MarOkButton = driver.find_element_by_xpath('//*[@id="search_modal_success_btn"]').click()

    AddressSearchButton = driver.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/form/div/table/tbody/tr[3]/td/div/div/button').click()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="__daum__layer_1"]/iframe'))
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="__daum__viewerFrame_1"]'))
    driver.implicitly_wait(1)
    AddressText = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="region_name"]')))
    AddressText.send_keys(d.address)
    AddressText.send_keys(Keys.ENTER)
    pause.sleep(2)
    try:
        AddressResult = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul/li/dl/dd[2]/span/button[1]/span[1]')
        AddressResult.click()

    except Exception:
        print(d.site_name +"에서 오류 발생. 주소 검색 결과 없음.")
        errorlist.append(d.site_name)
        driver.switch_to.default_content()
        closeButton = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="btnCloseLayer"]')))
        closeButton.click()
        site2_elem = driver.find_element_by_xpath('//*[@id="sidebar"]/nav/ul/li[12]/ul[1]/li/a')
        site2_elem.click()
        # site3_elem = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div[2]/a")))
        # site3_elem.click()
        continue

    driver.switch_to.default_content()
    try:
        registerButton = driver.find_elements_by_id('btn_register')
        registerButton[1].click()
        regOkButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        regOkButton.click()
    except Exception:
        print(d.site_name+"에서 오류 발생")


    print('error status')
    print('errorlist1 = ', errorlist)
    print('errorlist2 = ', errorlist2)

print(errorlist)
print(errorlist2)
f.close()
