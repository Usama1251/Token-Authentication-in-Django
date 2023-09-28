from django.urls import path
from app.views import Signin, Home, Logout, Signup
from app import views
urlpatterns = [
    path('signup/', Signup.as_view()),
    path('signin/', Signin.as_view()),
    path('home/', Home.as_view()),
    path('logout/', Logout.as_view()),
]