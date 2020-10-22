import datetime
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule
from account.models import CustomUser, GoulmetModel

# Create your views here.
class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, CreateView):
    """カレンダーの登録"""
    template_name = 'calendar/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        user_objects = CustomUser.objects.get(pk=self.request.session['_auth_user_id'])
        goulmet_id = GoulmetModel.objects.get(user_id=user_objects)
        schedule.user_id = goulmet_id
        schedule.save()
        return redirect('calendar_app:mycalendar', year=date.year, month=date.month, day=date.day)

class MyCalendarUpdate(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, UpdateView):
    """カレンダーの更新"""
    template_name = 'calendar/mycalendar_update.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def form_valid(self, form):
        object = Schedule.objects.get(pk=self.kwargs['pk'])
        date = object.date
        schedule = form.save(commit=False)
        schedule.date = date
        user_objects = CustomUser.objects.get(pk=self.request.session['_auth_user_id'])
        goulmet_id = GoulmetModel.objects.get(user_id=user_objects)
        schedule.user_id = goulmet_id
        schedule.save()
        return redirect('calendar_app:mycalendar', year=date.year, month=date.month, day=date.day)

class MyCalendarDelete(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, DeleteView):
    """カレンダーの削除"""
    template_name = 'calendar/mycalendar_delete.html'
    model = Schedule
    form_class = BS4ScheduleForm
    date_field = 'date'
    success_url = reverse_lazy('calendar_app:mycalendar')