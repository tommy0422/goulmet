from django.urls import path
from .views import session_save,GoulmetCalendar,calendar_save,reservation_check,reservation_save,reservation_confirm,reservation_goulmet,reservation_confirm_goulmet

app_name = "reservation"

urlpatterns = [
    path('session_save/',session_save,name='session_save'),
    path('goulmet_calendar/', GoulmetCalendar.as_view(), name='goulmet_calendar'),
    path('goulmet_calendar/<int:year>/<int:month>/<int:day>/', GoulmetCalendar.as_view(), name='goulmet_calendar'),
    path('calendar_save/<int:pk>',calendar_save, name='calendar_save'),
    path('reservation_check/',reservation_check, name='reservation_check'),
    path('reservation_save/',reservation_save, name='reservation_save'),
    path('reservation_confirm/',reservation_confirm, name='reservation_confirm'),
    path('reservation_confirm_goulmet/',reservation_confirm_goulmet, name='reservation_confirm_goulmet'),
    path('reservation_goulmet/<int:pk>',reservation_goulmet, name='reservation_goulmet'),
    path('reservation_confirm_goulmet/',reservation_confirm_goulmet, name='reservation_confirm_goulmet'),
]