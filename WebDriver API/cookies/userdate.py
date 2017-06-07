# 利用浏览器的保存缓存的文件夹绕过登录，启动浏览器时使用用户原有的缓存文件，这样之前保存登录信息的网站打开直接就是登录状态了
from selenium import webdriver

option = webdriver.ChromeOptions()
# 使用add_argument()方法来添加参数
option.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data') # 这里是谷歌浏览器的缓存文件夹
driver = webdriver.Chrome(chrome_options=option)

driver.quit()