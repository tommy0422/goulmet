from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from myuser.models import CustomUser
from account.models import GoulmetModel
from .models import RoomModel, ChatModel

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
def user_chat(request,pk):
    room_object = RoomModel.objects.get(pk=pk)
    object_list = ChatModel.objects.all().filter(room_id=room_object)
    return render(request, 'chat/user_chat.html', {'room_object':room_object,'object_list': object_list})

@login_required
def userchat_create(request):
    if request.method == 'POST':
        user_object = CustomUser.objects.get(pk=request.session['_auth_user_id'])
        room_id = RoomModel.objects.get(pk=request.POST['room_id'])
        object = ChatModel.objects.create(
                user_id = user_object,
                room_id = room_id,
                text = request.POST['text'],
                )
        object.save()
        return redirect('chat:user_chat',pk=request.POST['room_id'])
    else:
        return redirect('chat:chat_list')

@login_required
def goulmet_chat(request,pk):
    room_object = RoomModel.objects.get(pk=pk)
    object_list = ChatModel.objects.all().filter(room_id=room_object)
    return render(request, 'chat/goulmet_chat.html', {'room_object':room_object,'object_list': object_list})

@login_required
def goulmetchat_create(request):
    if request.method == 'POST':
        user_object = CustomUser.objects.get(pk=request.session['_auth_user_id'])
        goulmet_object = GoulmetModel.objects.get(user_id=user_object)
        room_id = RoomModel.objects.get(pk=request.POST['room_id'])
        object = ChatModel.objects.create(
                goulmet_id = goulmet_object,
                room_id = room_id,
                text = request.POST['text'],
                )
        object.save()
        return redirect('chat:goulmet_chat',pk=request.POST['room_id'])
    else:
        return redirect('chat:chat_list_goulmet')