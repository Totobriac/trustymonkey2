from django.contrib import admin

from places.models import (DessertPic, InsidePic, MainPic, MenuPic, OutsidePic,
                           Restaurant, RestaurantReview, StarterPic)

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(RestaurantReview)
admin.site.register(StarterPic)
admin.site.register(MainPic)
admin.site.register(DessertPic)
admin.site.register(MenuPic)
admin.site.register(OutsidePic)
admin.site.register(InsidePic)
