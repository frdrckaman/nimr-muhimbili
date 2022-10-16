from django.urls import path
from .views import (
    AboutView, ContactView, HomeView, ProfileView, DPFinanceView, DPHritdView,
    DPLabView, DPResearchView, DPPmuView, DPMonitoringView, TeamView)

app_name = "nimr_web"

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<staff>', ProfileView.as_view(), name='profile'),
    path('team/', TeamView.as_view(), name='team'),
    path('department/finance', DPFinanceView.as_view(), name='finance'),
    path('department/hritd', DPHritdView.as_view(), name='hritd'),
    path('department/lab', DPLabView.as_view(), name='lab'),
    path('department/monitoring', DPMonitoringView.as_view(), name='monitoring'),
    path('department/pmu', DPPmuView.as_view(), name='pmu'),
    path('department/research', DPResearchView.as_view(), name='research'),
    path('', HomeView.as_view(), name='home'),
]