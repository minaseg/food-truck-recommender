from django.contrib import admin
from django.urls import path

from recommend.views import recommend_food_trucks

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", recommend_food_trucks),
    path("recommend/", recommend_food_trucks),
]
