from .models import Category

def categories(request):
  allcats = Category.objects.all()

  return {'cats':allcats}


# def cartcount(request):
#   allitems = Orderdetail.objects.filter(order_placed=False).filter(user__username=request.user.username)
#   total_quantity = 0
#   for item in allitems:
#     total_quantity += item.quantity
#   return {'prodcount':total_quantity}