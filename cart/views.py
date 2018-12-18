from django.shortcuts import render

# Create your views here.
def view_cart(request):
    """A view that renders the cart contents page"""
    """Een scherm die de inhoud van de winkelwagen prensenteerd"""
    return render(request, 'cart.html')