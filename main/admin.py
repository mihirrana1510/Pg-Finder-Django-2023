from django.contrib import admin
from .models import Login,Owner,User,PG,Ameneties,Favourites,Ratings,ContactOwner,PGImages,UserLogin

# Register your models here.
admin.site.register(Login)
admin.site.register(Owner)
admin.site.register(User)
admin.site.register(PG)
admin.site.register(Ameneties)
admin.site.register(Favourites)
admin.site.register(Ratings)
admin.site.register(ContactOwner)
admin.site.register(PGImages)
admin.site.register(UserLogin)
