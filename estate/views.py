from django.shortcuts import render
from django.views.generic import TemplateView
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

#get the listings 
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'estate/index.html',context)

#get the realtors
def about(request):
    realtors = Realtor.objects.order_by('-hired_date')

    mvp_realtors =Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors,
    }
    return render(request, 'estate/about.html',context)

