import os
import random
import subprocess
import hashlib
import pickle
import sqlite3
import requests

PASSWORD = "admin123"  # Hardcoded password
API_KEY = "SECRET-KEY-123456"  # Hardcoded secret

def login(username, password):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    # SQL Injection 漏洞
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return bool(result)

def ping_host(ip):
    # Command Injection 漏洞
    os.system("ping -c 1 " + ip)

def hash_password(password):
    # 使用過時弱加密算法 (MD5)
    return hashlib.md5(password.encode()).hexdigest()

def recursive():
    # 無限遞迴 Bug
    return recursive()

def unsafe_exception():
    try:
        x = 1 / 0
    except: # 空白 except 壞習慣
        pass

def test_return():
    return True
    print("Never execute") # 無法觸及的死碼 Bug

def append_item(item, items=[]): # 可變動預設參數 Bug
    items.append(item)
    return items
