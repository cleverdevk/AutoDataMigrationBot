class data:
    site_name = None
    address = None
    site_code = None
    project_code = None
    work_name = None
    openAt = None
    contractAt = None
    expirationAt = None
    admingroup = None
    workStatusTypes = None
    contractTypes = None
    parkingTypes = None
    parkingNum = None
    parkingNumTypes = None
    equipmentName = None
    parkingSysTypes = None
    region = None

def isNotNone(input, site_name, errorlist):
    if input is None or '':
        print(site_name + "에서 오류 발생. " + input + "없음")
        errorlist.append(input)
        return False
    return True

