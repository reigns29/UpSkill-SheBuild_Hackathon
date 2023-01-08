from django.urls import path
from . import views

urlpatterns = [
    path("" , views.list_posts , name = "list_posts"),
    path("<int:post_id>" , views.view_post , name = "view_posts"),
    path("new" , views.new_post , name = "new_posts"),
    path("top" , views.top_posts , name = "top_posts"),
    path("count" , views.count , name = "count")
]