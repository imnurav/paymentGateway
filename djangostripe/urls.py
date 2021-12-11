
from django.contrib import admin
from django.urls import path
from products.views import cancel, home, checkout, success
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),



]
