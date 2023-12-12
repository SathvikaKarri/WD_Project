from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import item, Cart

# Create your views here.
def index(request):
    return render(request, "bazaar/index.html",
                  {"items": item.objects.all()})


def cart(request):
    cart_items = Cart.objects.all()

    # Calculate the total price of items in the cart
    if not cart_items:
        # If the cart is empty, provide a message
        context = {'message': 'Your cart is empty.'}
    else:
        # Calculate the total price of items in the cart
        total_price = sum(item.item.price * item.quantity for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }

    return render(request, "bazaar/cart.html", context)

def add_to_cart(request, item_id):
    product = item.objects.get(pk=item_id)

    # Get the user's cart from the session or create an empty cart
    # cart = request.session.get('cart', {})

    # Add the selected product to the cart or increment its quantity
    # cart_item = cart.get(str(product_id), {'quantity': 0})
    # cart_item['quantity'] += 1
    # cart[str(product_id)] = cart_item

    # Update the cart in the session
    # request.session['cart'] = cart

     # Check if the product is already in the user's cart
    cart_item, created = Cart.objects.get_or_create(item=product)

    # If the item is already in the cart, increment its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # item ={"item": item.objects.all()}
    return redirect(index)


def remove_from_cart(request, item_id):
    try:
           
            cart_item = Cart.objects.get(id=item_id)

    
            # If the item is in the cart and its quantity is greater than 1, decrement the quantity
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                # If the quantity is 1 or less, remove the item from the cart
                cart_item.delete()

    except cart.DoesNotExist:
            # If the item is not in the cart, you may want to handle this case (e.g., show a message)
        pass

    # Redirect to the 'view_cart' view after removing from the cart
    return redirect(cart)


def Buy(request):
    return render(request, "bazaar/buy.html")


