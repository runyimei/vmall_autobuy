from helium import *
from selenium.webdriver import ChromeOptions
from configparser import ConfigParser
import logging
import time
import logging.config
from datetime import datetime, timedelta

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('mylog')


class VmallAutoBuy:
    def __init__(self):
        self.read_config()
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        start_chrome(url='vmall.com', options=options)
        logger.info('访问主页面 vmall.com')

    def read_config(self):
        cfg = ConfigParser()
        cfg.read('vmall.ini', encoding='utf-8')
        self.login_username = cfg.get('login', 'username')
        self.login_password = cfg.get('login', 'password')
        self.product_url = cfg.get('product', 'productURL')
        self.product_color = cfg.get('product', 'productColor')
        self.product_edition = cfg.get('product', 'productEdition')
        self.product_plan = cfg.get('product', 'productPlan')
        self.rushTime = cfg.get('purchase', 'rushTime')  # 抢购时间
        self.readyTime = datetime.strptime(self.rushTime, "%Y-%m-%d %H:%M:%S") - timedelta(minutes=3)  # 准备抢购时间

        logger.info('读取配置文件成功，抢购信息： [页面url] %s ; [颜色] %s ; [版本] %s ; [套餐] %s ',
                    self.product_url, self.product_color, self.product_edition, self.product_plan)

    def login(self):
        logger.info('开始登录')
        click('请登录')
        write(self.login_username, into='手机号')
        write(self.login_password, into='密码')
        click('登录')
        continue_flag = False
        while continue_flag is False:
            try:
                wait_until(Text('首页').exists)
                continue_flag = True
            except:
                continue_flag = False
        refresh()

    def auto_buy(self):
        logger.info('进入产品页面: %s', self.product_url)
        go_to(self.product_url)

        #  等待 抢购时间的到来
        self.wait_for_ready_time()

        #  提前选好 产品的配置
        go_to(self.product_url)
        refresh()
        logger.info('选择产品颜色: %s', self.product_color)
        click(Text(self.product_color))
        logger.info('选择版本: %s', self.product_edition)
        click(Text(self.product_edition))
        logger.info('选择套餐： %s', self.product_plan)
        click(Text(self.product_plan))

        # 等待 抢购按钮可以 点击
        self.wait_for_btn_enable()

        #  开始抢购
        logger.info('立即下单')
        click(S('#pro-operation > a.product-button02'))
        logger.info('提交订单')
        click('提交订单')
        logger.info('抢购成功，请尽快付款')

    def wait_for_ready_time(self):
        while True:
            now = datetime.now()
            if (self.readyTime - now).seconds > 60:
                refresh()
                time.sleep(60)
            else:
                break

    #  等待 抢购按钮可以点击
    def wait_for_btn_enable(self):
        while True:
            order_btn = S('#pro-operation > a.product-button02')
            text = order_btn.web_element.text
            if text == '立即申购':
                break
            time.sleep(0.01)

    def notify_user(self):
        pass

    def logout(self):
        pass


if __name__ == '__main__':
    logger.info('抢购脚本开始运行...')
    client = VmallAutoBuy()
    client.login()
    client.auto_buy()
    client.logout()
