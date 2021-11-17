from django.urls import path
from api.views import post_slot, get_slot

urlpatterns = [
    path('post_slot/', post_slot.as_view(), name="post"),
    path('get_slot/', get_slot.as_view(), name="get_slot"),
]