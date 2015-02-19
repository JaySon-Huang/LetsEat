#encoding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eatit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 后台管理界面
    url(r'^admin/', include(admin.site.urls)),
)

# 处理浏览店铺菜式、下单等界面URL对应的view
urlpatterns += patterns('shop.views',
	# 首页
    url(r'^$', 'index'),
    # 浏览店铺菜式
    url(r'^shop/(\d+)/$','viewShop'),

)

# 处理顾客登录、修改个人资料等界面URL对应的view
urlpatterns += patterns('customer.views',
    url(r'^customer/signup/$','signup'),
    url(r'^customer/login/$','login'),
    url(r'^customer/logout/$','logout'),
    url(r'^customer/profile/$','profile'),
)

urlpatterns += patterns('cart.views',
    url(r'^cart/add/(?P<cuisineID>[^/]+)/$','add2Cart'),
    url(r'^cart/view/$','getCart'),
    url(r'^cart/clear/$','clearCart'),
    url(r'^cart/confirm/$','confirmCart'),
)
