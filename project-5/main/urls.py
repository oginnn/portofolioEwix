from django.urls import path, re_path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.index_view.as_view(), name="home"),
    path('contact/', views.contact_view, name='contact_view'),
    path('certificate/', views.certificates_view.as_view(), name='certificate'),
    re_path('reporting/(?P<page>\d+)', views.reporting_view.as_view(), name='reports'),
    path('reporting/<slug:slug>', views.reporting_result_view.as_view(), name="reporting"),
]