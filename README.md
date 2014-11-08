网上订餐管理系统
===
## 环境
python 2.7 [Python官网](https://www.python.org/)  
Django 1.6.5 [Django官网](https://www.djangoproject.com/)  

## 运行
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
黄俊深 整体设计、非查询功能
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
