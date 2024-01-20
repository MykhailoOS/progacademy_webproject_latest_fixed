from .models import Home, Shop, BlogPost, Testimonials, OurTeam, Services


# Context processors
def home(request):
    items = Home.objects.filter(is_visible=True)
    return {'items': items}


def blog(request):
    items = BlogPost.objects.filter(is_visible=True)
    return {'blogs': items}


def shop(request):
    items = Shop.objects.filter(is_visible=True)
    return {'shop': items}


def reviews(request):
    items = Testimonials.objects.filter(is_visible=True)
    return {'testimonials': items}


def services(request):
    items = Services.objects.filter(is_visible=True)
    return {'services': items}


def team(request):
    items = OurTeam.objects.filter(is_visible=True)
    return {'team': items}