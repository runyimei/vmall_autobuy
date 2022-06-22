from helium import *
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from configparser import ConfigParser
import logging

#
options = ChromeOptions()
options.add_argument('--start-maximized')
start_chrome(url='vmall.com', options=options)
driver = get_driver()
driver.get("www.baidu.com")

#  登录
click('请登录')
write('*****', into='手机号')
write('*****', into='密码')
click('登录')

go_to('https://www.vmall.com/product/10086368169358.html')
# go_to('https://www.vmall.com/product/10086300679105.html')
click(Text('秘银色'))
click(Text('5G全网通 8GB+128GB'))
click(Text('官方标配'))
click(Text('立即申购'))

while True:
    order_btn = S('#pro-operation > a.product-button02')
    text = order_btn.web_element.text
    if text == '立即下单':
        break
click(S('#pro-operation > a.product-button02'))
click('提交订单')
print('抢购成功')

hover(S('#up_loginName'))


print('aaa')

