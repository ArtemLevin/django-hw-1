from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_and_tails/', views.heads_and_tails, name="HeadsNTails"),
    path('about_me_html/', views.about_me_html, name="About me")
]
