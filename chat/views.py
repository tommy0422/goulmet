from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from myuser.models import CustomUser
from account.models import GoulmetModel
from .models import RoomModel

# Create your views here.
@login_required
def chat_list(request):
    object_list = RoomModel.objects.all().filter(user_id=request.session['_auth_user_id'])
    return render(request, 'chat/chat_list.html', {'object_list': object_list})

@login_required
def chat_list_goulmet(request):
    user = CustomUser.objects.get(pk=request.session['_auth_user_id'])
    if GoulmetModel.objects.filter(user_id=user).exists():
        goulmet_object = GoulmetModel.objects.get(user_id=user)
        object_list = RoomModel.objects.all().filter(goulmet_id=goulmet_object)
        return render(request, 'chat/chat_list_goulmet.html', {'object_list': object_list})
    else:
        return HttpResponse('あなたはまだGoulmetに認定されていません。')


@login_required
def user_chat(request):
    return HttpResponse()



