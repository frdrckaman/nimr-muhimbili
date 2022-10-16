from django.urls import path
from .views import AboutView, ContactView, HomeView, ProfileView, TeamView

app_name = "nimr_web"

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<staff>', ProfileView.as_view(), name='profile'),
    path('team/', TeamView.as_view(), name='team'),
    path('', HomeView.as_view(), name='home'),
]