#encoding=utf-8
import json
import datetime

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from shop.models import CuisineModel
from customer.models import CustomerModel, OrderModel

from models import Cart

def add2Cart(request, cuisineID):
    # FIXME: 如果餐厅在“打烊”状态，应该无法添加到购物车,返回错误
    cart = request.session.get('cart', None)
    if cart is None:
        cart = Cart()
    res = {'size':cart.add(int(cuisineID))}
    request.session['cart'] = cart
    return HttpResponse(json.dumps(res))

def getCart(request):
    totalCost = 0.0
    cuisines = []
    for cuisineID, num in request.session['cart'].items.items():
        cuisine = CuisineModel.objects.get(id=cuisineID)
        totalCost += cuisine.price*num
        cuisines.append((cuisine, num))
    return render_to_response(
        'cart.html',
        {
        'session':request.session,
        'totalCost':totalCost,
        'cuisines':cuisines,
        },
        context_instance=RequestContext(request)
    )

def clearCart(request):
    request.session['cart'] = Cart()
    return HttpResponse(json.dumps({'size':0}))

def confirmCart(request):
    user = CustomerModel.objects.get(id=request.session['uid'])
    cuisines = []
    order = OrderModel(
        status=1
    )
    is_valid_order = True
    shop = None
    for cuisineID, num in request.session['cart'].items.items():
        cuisine = CuisineModel.objects.get(id=cuisineID)
        if not shop:
            shop = cuisine.shop
        else:
            print shop, cuisine.shop
            if not shop.id == cuisine.shop.id:
                is_valid_order = False
                break
        # 把点餐的信息先存储到cuisines中
        cuisines.append( (cuisine,num) )
    if not is_valid_order:
        length = request.session['cart'].size
        return HttpResponse(json.dumps({'size':length,'error':'所点的餐来自不同餐厅!'}))
    order.shop = shop
    order.customer = user
    # 进行save之后才有order的id进行多对多的存储
    order.save()
    
    # 进行order与cuisine多对多的绑定
    print dir(order)
    for i in xrange(num):
        order.cuisine.add(cuisine)
    order.save()

    # 把购物车清空
    request.session['cart'] = Cart()
    length = request.session['cart'].size
    return HttpResponse(json.dumps({'size':length}))
