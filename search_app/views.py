from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from account.models import GoulmetModel, OptionModel
from myuser.models import CustomUser
from calendar_app.models import Schedule
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class SearchView(TemplateView):
    template_name = 'search/search_form.html'


class ResultView(ListView):
    model = GoulmetModel
    template_name = 'search/search_list.html'

    def get_queryset(self):
        queryset = GoulmetModel.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(area__icontains=keyword)
        return queryset

@login_required
def goulmet_info(request, pk):
    if 'options' in request.session:
        del request.session['options']
    if 'base_price' in request.session:
        del request.session['base_price']
    if 'goulmet_id' in request.session:
        del request.session['goulmet_id']
    if 'date' in request.session:
        del request.session['date']  
    object = GoulmetModel.objects.get(pk=pk)
    customuser = object.user_id.pk
    object2 = OptionModel.objects.all().filter(user_id=customuser)
    liked = False
    if object.like.filter(id=request.user.id).exists():
       liked = True
    return render(request, 'search/goulmet_info.html', {'object': object,'object2': object2,'liked': liked})