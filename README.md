网上订餐管理系统
===
## 环境
* Python 2.7 [Python官网](https://www.python.org/)  
* Django 1.6.5 [Django官网](https://www.djangoproject.com/)  
* python-mysql [下载链接](http://sourceforge.net/projects/mysql-python/)   

## 运行
1. 使用sqlite3:  
把`eatit/setting.py`中`DATABASES`中sqlite3部分的代码取消注释，并注释掉MySQL部分。  
使用命令行到主目录下执行`python manage.py syncdb`初始化数据库  
其中会提示创建网站后台管理员及密码  
使用sqlite3数据库的初始化到此结束。  

2. 使用MySQL数据库：  
安装MySQL[MySQL下载](http://www.mysql.com/downloads/)  
安装MySQL的python对接模块:python-mysql [下载链接](http://sourceforge.net/projects/mysql-python/)  

	python setup.py build

> 若安装时出现 EnvironmentError: mysql_config not found  
> 参考[这篇文章](http://www.unixdo.com/DataBase/mysql_config.html)  
> 修改`setup_posix.py`文件：  
> mysql_config.path = "/usr/local/mysql-5.0.67/bin/mysql_config"

在MySQL中创建名为`letseat`的数据库  
在 `eatit/` 目录下创建`passwd.py`,定义  

	MYSQL_USER = '数据库用户名'
	MYSQL_PASS = '数据库密码'
使用命令行到主目录下执行`python manage.py syncdb`初始化数据库  
其中会提示创建网站后台管理员及密码  
使用MySQL数据库的初始化到此结束。  

* 类Unix环境
./manage.py runserver  
然后在浏览器打开`http://localhost:8000`  
* Windows
配置好python的环境变量后，使用`启动服务器.bat`  
或者使用cmd命令行进入目录下运行`python manage.py runserver`  
然后在浏览器打开`http://localhost:8000`

## 框架
使用Django框架开发,数据库使用MySQL。

## 分工
主要负责人 职责  
黄俊深 整体框架设计、非查询功能  
GUI界面 林锦安  
SQL查询功能 张晓波、李伟荣  
刘俊良、阿卜力克木 E-R图绘制、文档撰写  

## 实体
#### 店铺(shop) ####
#### 菜式(cuisine) ####
#### 用户(user) ####
#### 订单(order) ####
#### 评价(comment) ####
#### 店长(shopkeeper) ####
#### 网站管理员(admin) ####

## 需要实现的查询
1. 按照店名查找菜式
2. 用户查找以往订单
3. 店长修改所选菜式
4. 店长查询销售情况
5. 按照销量排序
6. 按照价格排序
7. 按照评价排序
