from django.urls import path
from . import views

app_name = 'mate'

urlpatterns = [
    path('', views.mate_listing, name='mate-list'),
    # path('mates/<int:mate_id>/', views.mate_detail, name='mate-detail'),
    # path('mates/search/', views.mate_search, name='mate-search'),
]
