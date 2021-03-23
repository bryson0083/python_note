# -*- coding: utf-8 -*-
"""
台灣身份證字號/居留證號檢查

說明:
    中華民國身分證、新舊式居留證，格式檢查、檢查碼驗證

"""
import re


def county_code_dic(param):
    """ 轉換縣市代碼為中文敘述 """

    code_dic = {
        "A": "台北市",
        "B": "台中市",
        "C": "基隆市",
        "D": "台南市",
        "E": "高雄市",
        "F": "新北市",
        "G": "宜蘭縣",
        "H": "桃園市",
        "I": "嘉義市",
        "J": "新竹縣",
        "K": "苗栗縣",
        "L": "台中縣",
        "M": "南投縣",
        "N": "彰化縣",
        "O": "新竹市",
        "P": "嘉義縣",
        "Q": "雲林縣",
        "R": "台南縣",
        "S": "高雄縣",
        "T": "屏東縣",
        "U": "花蓮縣",
        "V": "台東縣",
        "W": "金門縣",
        "X": "澎湖縣",
        "Y": "陽明山管理局",
        "Z": "連江縣",
    }
    rt_parm = code_dic.get(param, "")
    return rt_parm


def cal_id_check_code(id_number):
    """ 國民身分證、新式居留證，檢查碼驗證 """

    is_valid = False
    idchk = "0123456789ABCDEFGHJKLMNPQRSTUVXYWZIO"
    const_list = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    p1 = idchk.find(id_number[0])
    id_list = list(str(p1)+id_number[1:-1])

    weighted_list = [(int(a) * b) % 10 for a, b in zip(id_list, const_list)]
    chk_code = 10 - sum(weighted_list, 0) % 10
    if chk_code == int(id_number[-1:]):
        is_valid = True

    return is_valid


def cal_id_check_code_for_old_resident_cert(id_number):
    """ 舊式居留證Resident Certificate，檢查碼驗證 """

    is_valid = False
    idchk = "0123456789ABCDEFGHJKLMNPQRSTUVXYWZIO"
    const_list = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    p1 = idchk.find(id_number[0])
    p2 = str(idchk.find(id_number[1]))[-1:]
    id_list = list(str(p1) + p2 + id_number[2:-1])

    weighted_list = [(int(a) * b) % 10 for a, b in zip(id_list, const_list)]
    chk_code = 10 - sum(weighted_list, 0) % 10
    if chk_code == int(id_number[-1:]):
        is_valid = True

    return is_valid


def twpid_format_check(id_number):
    """
    檢查格式，判別類別是本國身分證或外籍居留證
    回傳
    is_validity(是否為合法身分證/居留證號): True | False
    is_citizen(是否為本國人/外籍人士): True | False
    cert_type(證件類別): 國民身分證/新式居留證/舊式居留證
    personal_status(身分別):
        舊式居留證(性別A, B): 無戶籍國民、大陸地區人民及港澳居民
        舊式居留證(性別C, D): 外國人
        新式居留證(性別8, 9): 第3碼(0~6) -> 外國人或無國籍人士
                            第3碼(7) -> 無戶籍國民
                            第3碼(8) -> 港澳居民
                            第3碼(9) -> 大陸地區人民
        國民身分證(性別1, 2): 第3碼(0~5) -> 國人
                            第3碼(6) -> 外國人或無國籍人士
                            第3碼(7) -> 無戶籍國民
                            第3碼(8) -> 港澳居民
                            第3碼(9) -> 大陸地區人民
    gender(性別): F(女) | M(男)
    county_code(縣市代號): 見"註1"
    county_desc(縣市中文敘述): 見"註1"
    """

    id_number = id_number.upper()
    is_validity = False
    is_citizen = False
    cert_type = ""
    personal_status = ""
    gender = ""
    county_code = ""
    county_desc = ""

    # 身分證&居留證(新式2021起)
    id_pattern = '^[A-Z]{1}[1-2|8-9]{1}[0-9]{8}$'
    if re.match(id_pattern, id_number):
        # 檢查碼驗證
        is_validity = cal_id_check_code(id_number)

        if is_validity:
            if id_number[1] in ["1", "2"]:
                is_citizen = True
                cert_type = "國民身分證"
                if "0" <= id_number[2] <= "5":
                    personal_status = "國人"
                elif id_number[2] == "6":
                    personal_status = "外國人或無國籍人士"
                elif id_number[2] == "7":
                    personal_status = "無戶籍國民"
                elif id_number[2] == "8":
                    personal_status = "港澳居民"
                else:
                    personal_status = "大陸地區人民"

            else:
                cert_type = "新式居留證"
                if "0" <= id_number[2] <= "6":
                    personal_status = "外國人或無國籍人士"
                elif id_number[2] == "7":
                    personal_status = "無戶籍國民"
                elif id_number[2] == "8":
                    personal_status = "港澳居民"
                else:
                    personal_status = "大陸地區人民"

            # 判斷性別
            if id_number[1] in ["1", "8"]:
                gender = "M"
            else:
                gender = "F"

    # 居留證(舊式2021前)
    old_pattern = '^[A-Z]{1}[A-D]{1}[0-9]{8}$'
    if re.match(old_pattern, id_number):
        # 檢查碼驗證
        is_validity = cal_id_check_code_for_old_resident_cert(id_number)

        if is_validity:
            cert_type = "舊式居留證"

            if id_number[1] in ["A", "B"]:
                personal_status = "無戶籍國民、大陸地區人民及港澳居民"
            else:
                personal_status = "外國人"

            # 判斷性別
            if id_number[1] in ["A", "C"]:
                gender = "M"
            else:
                gender = "F"

    if is_validity:
        county_code = id_number[0]
        county_desc = county_code_dic(county_code)

    return {
        "is_validity": is_validity,
        "is_citizen": is_citizen,
        "cert_type": cert_type,
        "personal_status": personal_status,
        "gender": gender,
        "county_code": county_code,
        "county_desc": county_desc,
    }


if __name__ == "__main__":
    # 國民身分證測試
    print(twpid_format_check("A123456789"))

    # 舊式居留證測試
    # print(twpid_format_check("AC01234567"))

    # 新式居留證測試
    # print(twpid_format_check("A800000014"))
