import json
from datetime import date, time, datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import mixins
from calendar_app.models import Schedule
from myuser.models import CustomUser
from .models import OrderModel, OrderOption
from account.models import GoulmetModel, OptionModel
from django.views.generic import TemplateView

# Create your views here.
@login_required
def session_save(request):
    if request.method == 'POST': 
            request.session['options'] = request.POST.getlist('option')
            request.session['base_price'] = request.POST['base_price']
            request.session['goulmet_id'] = request.POST['goulmet_id'] 
            return redirect('reservation:goulmet_calendar')
    else:
         return render('search/search_form.html')
        
class GoulmetCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin,TemplateView):
    """カレンダー予約"""
    template_name = 'calendar/goulmet_calendar.html'
    model = Schedule
    date_field = 'date'

    def get_queryset(self):
        goulmet = GoulmetModel.objects.get(user_id=self.request.session['goulmet_id'])
        queryset = Schedule.objects.all().filter(user_id=goulmet)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

@login_required
def calendar_save(request,pk):
    """カレンダー予約（バック）"""
    object = Schedule.objects.get(pk=pk)
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, (datetime, date, time)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))

    request.session['date'] = json_serial(object.date)
    request.session['start_time'] = json_serial(object.start_time)
    request.session['end_time'] = json_serial(object.end_time)
    return redirect('reservation:reservation_check')

@login_required
def reservation_check(request):
    """最終確認"""
    if 'base_price' and 'goulmet_id' and 'date' and 'start_time' and 'end_time' in request.session.keys():
        goulmet_object = GoulmetModel.objects.get(pk=request.session['goulmet_id'])
        order_option = []
        option_sum = 0
        for opt in request.session['options']:
            order_option.append(OptionModel.objects.get(pk=opt))
            option_object = OptionModel.objects.get(pk=opt)
            option_sum =+ option_object.price
        sum = goulmet_object.base_price + option_sum
        print(sum)

        return render(request,'reservation/reservation_check.html',{'goulmet_object':goulmet_object,'order_option':order_option,'sum':sum})
    else: 
        return redirect('search_app:search_form')

@login_required
def reservation_save(request):
    """予約データ保存"""
    if 'base_price' and 'goulmet_id' and 'date' and 'start_time' and 'end_time' in request.session.keys():
        user_object = CustomUser.objects.get(id=request.session['_auth_user_id'])
        order = OrderModel.objects.create(
            user_id =  user_object,
            base_price = request.session['base_price'],
            goulmet_id = GoulmetModel.objects.get(id=request.session['goulmet_id']),
            date = request.session['date'],
            start_time = request.session['start_time'],
            end_time = request.session['end_time'],      
            )
        order.save()
        if request.session['options']:
            for item in request.session['options']:
                option_object = OptionModel.objects.get(id=item)
                object_price = option_object.price
                order_object = OrderModel.objects.get(id=order.id)
                option = OrderOption.objects.create(
                    order_id = order_object,
                    option_id = option_object,
                    option_price = object_price
                )
            option.save()
        return redirect('reservation:reservation_confirm')
    else:
        return redirect('search_app:search_form')
        
@login_required
def reservation_confirm(request):
    """予約リスト"""
    user = CustomUser.objects.get(id=request.session['_auth_user_id'])
    object_list = OrderModel.objects.all().filter(user_id=user)
    return render(request, 'reservation/reservation_confirm.html', {'object_list': object_list})

@login_required
def reservation_goulmet(request,pk):
    """予約したgoulmetの情報"""
    object = OrderModel.objects.get(pk=pk)
    object2 = OrderOption.objects.all().filter(order_id=pk)
    option_sum = 0
    for option in object2:
        option_sum =+ option.option_id.price
    sum = object.base_price + option_sum
    print(sum)
    return render(request, 'reservation/reservation_goulmet.html', {'object': object,'object2':object2,'sum':sum})



        
        




