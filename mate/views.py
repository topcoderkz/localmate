from django.shortcuts import render
from .models import Mate

def mate_listing(request):
    """A view of all mates."""
    mates = Mate.objects.all()
    return render(request, 'mate/mate_listing.html', {'mates': mates})
