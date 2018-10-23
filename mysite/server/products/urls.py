from django.urls import path

from .views import (
   products_list, products_detail
)

urlpatterns = [
    path ('', products_list),
    path ('<int:idx>', products_detail),
]
