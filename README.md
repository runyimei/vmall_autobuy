# vmall_autobuy



1.  **环境安装**：
   1）python 下载： 
     windows 64位： https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe
     windows 32位： https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe
   2) chrome浏览器下载：
       https://www.google.cn/chrome/
   3）chromedriver 下载：
       https://chromedriver.chromium.org/downloads



2.  **项目配置**
   1） 下载项目源码到本地电脑中。 https://github.com/runyimei/vmall_autobuy
   2） 进入项目目录，安装项目依赖包:  pip install -r requirements

   3）配置 chromedriver
     a. 将 chromedriver 分别放在 chrome浏览器的安装目录
     b. 将 chromedriver 配置成本地环境变量
     c. chromedriver 放在项目的 venv/Scripts 中



3. **配置 抢购信息**

   ​	进入 项目的目录，打开 app/vmall.ini 文件，填写 vmall 的登录用户名、密码，抢购的手机页面url ， 手机颜色、版本、套餐。

   

4.  **运行项目**

   ​      进入 项目的目录， 进入 app 目录， 打开命令行，运行 python vmall_auto_buy.py即可。在vmall 的登录页面手动输入用户名和密码



