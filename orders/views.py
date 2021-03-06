from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from  django.contrib.auth.models import User
# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get('product_id')
    qty = data.get('qty')
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInCard.objects.filter(id = product_id).update(is_active=False)

    else:
    #     some code
        new_product, created = ProductInCard.objects.get_or_create(session_key=session_key,
                                                                   is_active = True,
                                                                   product_id=product_id,
                                                                   defaults={'qty':qty} )
        if not created:
            new_product.qty +=int(qty)
            new_product.save(force_update=True)

    products_in_cart = ProductInCard.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_qty = products_in_cart.count()
    return_dict["products_total_qty"] = products_total_qty

    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["id"] = item.id
        product_dict["qty"] = item.qty
        product_dict["total_price"] = item.total_price
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    product_in_cart = ProductInCard.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)
    if (request.POST):
        print(request.POST)
        if (form.is_valid()):
            print("yes")
            data = request.POST
            phone = data['phones']
            name = data['name']
            user, created = User.objects.get_or_create(username = phone, defaults={"first_name":name})

            order = Order.objects.create(user=user,
                                         costomer_name = name,
                                         customer_phone = phone,
                                         status_id = 1)

            for name, value in data.items():
                if name.startswith("product_in_cart_"):
                    product_in_cart_id  = name.split("product_in_cart_")[1]
                    product_in_cart = ProductInCard.objects.get(id=product_in_cart_id)
                    product_in_cart.qty = value
                    product_in_cart.order = order
                    product_in_cart.is_active = False
                    product_in_cart.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_cart.product,
                                                  qty = product_in_cart.qty,
                                                  price =product_in_cart.price,
                                                  total_price = product_in_cart.total_price,
                                                  order=order)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print("no")
    return render(request, 'orders/checkout.html', locals())