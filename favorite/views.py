from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from account.models import GoulmetModel
from myuser.models import CustomUser
from django.http import HttpResponse
from django.views.generic import TemplateView

@login_required
def favorite(request):
   goulmet = get_object_or_404(GoulmetModel, id=request.POST.get('goulmet_id'))
   liked = False
   if goulmet.like.filter(id=request.user.id).exists():
       goulmet.like.remove(request.user)
       liked = False
   else:    
       goulmet.like.add(request.user)
       liked = True
   return redirect('search_app:goulmet_info', pk=goulmet.pk) 

@login_required
def favorite_list(request):
    object = CustomUser.objects.get(id=request.session['_auth_user_id'])
    object_count = GoulmetModel.objects.all().filter(like=object).count()
    if object_count >= 1:
        object_list = GoulmetModel.objects.all().filter(like=object)
        return render(request, 'favorite/favorite_list.html', {'object_list': object_list}) 
    else:
        return redirect('favorite:not_favorite')

class NotFavorite(TemplateView):
    template_name = 'favorite/not_favorite.html'




