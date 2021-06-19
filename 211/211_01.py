import time
from itertools import product
import zipfile
import string, itertools

starttime = time.time() 
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
filepath = 'C:\python\koy.zip'
path = 'C:\python'
num = 4

with zipfile.ZipFile(filepath, 'r') as zip_data:
    for pwd in itertools.product(chars,repeat=num):
        password = ''.join(pwd)
        try:
            zip_data.extractall(path=path, pwd=password.encode("utf-8"))
            print(password)
            endtime = time.time() 
            elapsed_time = endtime-starttime
            print(f"経過時間：{elapsed_time}")
            exit()
        except RuntimeError:
            print(password)
        except zipfile.BadZipFile:
            print(password)

   