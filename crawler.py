import os

# 故意硬編碼敏感資訊 (SonarQube 會抓到漏洞)
API_KEY = "12345-ABCDE-SECRET-KEY" 

def get_data():
    # 故意用 eval，存在安全隱患
    user_input = "print('Hello')"
    eval(user_input) 

    # 故意宣告了但沒使用的變數
    unused_variable = 999 
    print("Fetching data...")

get_data()
