from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings
    }
    return render(request, 'estate/index.html',context)


class aboutView(TemplateView):
    template_name ="estate/about.html"