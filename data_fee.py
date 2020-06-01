class data_fee:
    site_name = None
    parkingType = None
    systemType = None
    isAdmin = None
    parkingNum = None
    fee = None
    max_fee = None
    penalty = None
    membership = None
    promotion = None
    memo = None

    def dataNoneCheck(self, errorlist):
        ret = True
        if(len(self.site_name) == 0):
            print(self.site_name, "에서 오류 발생. 사이트 이름 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.parkingType) == 0):
            print(self.site_name, "에서 오류 발생. 주자창 타입 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.systemType) == 0):
            self.systemType = "없음"
        if(len(self.isAdmin) == 0):
            print(self.site_name, "에서 오류 발생. 관리자유무 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.parkingNum) == 0):
            print(self.site_name, "에서 오류 발생. 면수 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.fee) == 0):
            print(self.site_name, "에서 오류 발생. 요금정보 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.max_fee) == 0):
            print(self.site_name, "에서 오류 발생. 최대 요금 정보 없음")
            errorlist.append(self.site_name)
            ret = False
        if(len(self.penalty) == 0):
            self.penalty = "0"
        if(len(self.promotion) == 0):
            self.promotion = "X"
        if(len(self.membership) == 0):
            self.membership == "0"
        return ret


