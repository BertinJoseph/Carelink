from cart.models import *

def counter(request):
    item_count=0
    if request.user.is_authenticated:
        user=request.user
        try:
            cart=Medcart.objects.filter(user=user)
            for i in cart:
                item_count+=i.quantity
        except:
            item_count=0

    return {'count':item_count}