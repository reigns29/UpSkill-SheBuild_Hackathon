from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "home"),
    path("signup/" , views.signup , name = "signup"),
    path("login" , views.login_user , name = "login"), 
    path("decider/" , views.decider , name = "decider"),
    path("profile/" , views.profile , name = "home"),
    path("logout" , views.logout_user , name = "logout"),
    path("profile/newsletter" , views.newsletter , name = "newsletter"),
    path("locate/" , views.locate , name = "locate"),
    path("locate/<str:state>" , views.locate_api , name = "locate_api"),
    path("chatbot/" , views.chatbot , name = "chatbot"),
    
]