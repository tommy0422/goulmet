from django.urls import path
from .views import MyCalendar, MyCalendarUpdate, MyCalendarDelete
# from .views import mycalendar

app_name = "calendar_app"

urlpatterns = [
    path('mycalendar/', MyCalendar.as_view(), name='mycalendar'),
    path('mycalendar/<int:year>/<int:month>/<int:day>/', MyCalendar.as_view(), name='mycalendar'),
    path('calendar_update/<int:pk>', MyCalendarUpdate.as_view(), name='mycalendar_update'),
    path('calendar_delete/<int:pk>', MyCalendarDelete.as_view(), name='mycalendar_delete'),
]