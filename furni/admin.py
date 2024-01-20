from django.contrib import admin
from .models import Home, Shop, AboutUs, OurTeam, BlogPost, Testimonials, Contact, Checkout, Services

# Register your models here.
admin.site.register(Home)
admin.site.register(Testimonials)
admin.site.register(Services)
admin.site.register(Shop)
admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(Checkout)
admin.site.register(OurTeam)




