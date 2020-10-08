from django.urls import path
from .views import SearchView, ResultView, goulmet_info

app_name = "search_app"

urlpatterns = [
    path('search_form/', SearchView.as_view(), name='search_form'),
    path('search_list/', ResultView.as_view(), name='search_list'),
    path('goulmet_info/<int:pk>', goulmet_info, name='goulmet_info'),
]