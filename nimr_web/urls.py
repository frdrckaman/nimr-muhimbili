from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from .views import (
    AboutView, ContactView, HomeView, ProfileView, DPFinanceView, DPHritdView,
    DPLabView, DPResearchView, DPPmuView, DPMonitoringView, TeamView, PublicationView,
    DownloadView)

admin.site.site_header = settings.NIMR_MUHIMBILI

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
    path('publications/', PublicationView.as_view(), name='publications'),
    # path('download/<str:file_name>', DownloadView.as_view(), name='download'),
    path('', HomeView.as_view(), name='home'),
]

urlpatterns += static(settings.NEWS_URL, document_root=settings.NEWS_ROOT)
