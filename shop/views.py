#encoding=utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from shop.models import ShopModel

def index(request):
    shoptype2str = {}
    for code, s in ShopModel.TYPE_OF_SHOP_CHOICES:
        shoptype2str[code] = s

    shops = ShopModel.objects.all()
    # 做处理，把数据库中的数据换为输出的内容
    for shop in shops:
        shop.shoptype = shoptype2str[shop.shoptype]

    return render_to_response(
		'index.html',
		{
        'session' : request.session,
        'shops':shops,
		},
		context_instance=RequestContext(request)
	)

def viewShop(request, shopid):
    shop2str = {}
    
    shop2str['type'] = {}
    for code, s in ShopModel.TYPE_OF_SHOP_CHOICES:
        shop2str['type'][code] = s

    shop2str['status'] = {}
    for code, s in ShopModel.STATUS_OF_SHOP_CHOICES:
        shop2str['status'][code] = s

    shop = ShopModel.objects.get(id=shopid)
    shop.shoptype = shop2str['type'][shop.shoptype]
    shop.status = shop2str['status'][shop.status]

    cuisines = shop.cuisine_shop.all()

    return render_to_response(
        'shop.html',
        {
            'session' : request.session,
            'shop':shop,
            'cuisines':cuisines,
        },
        context_instance=RequestContext(request)
    )
