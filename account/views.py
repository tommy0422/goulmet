from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from .forms import UserUpdateForm, MyPasswordChangeForm, GoulmetUpdateForm, OptionUpdateForm
from myuser.models import CustomUser
from .models import GoulmetModel, OptionModel
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

# Create your views here.
@login_required
def user_update(request):
    """ユーザー情報の更新"""
    # urlを基に、CustomUserを取得
    user = get_object_or_404(CustomUser, pk=request.session['_auth_user_id'])

     # フォームに、取得したCustomUserを紐付ける
    form = UserUpdateForm(request.POST, request.FILES or None, instance=user)

    # method = POST、つまり送信ボタン押下時、入力内容に問題なければ
    if request.method == 'POST' and 'FILES' and form.is_valid():
        form.save()
        return redirect('account:user_detail')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': user
    }
    return render(request, 'account/user_info.html', context)

@login_required
def user_detail(request):
    """ユーザー情報更新成功"""
    object = CustomUser.objects.get(pk=request.session['_auth_user_id'])
    return render(request, 'account/user_detail.html', {'object': object})

@login_required
def logout(request):
    """ログアウト処理"""
    django_logout(request)
    return redirect('register:login')

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('account:pass_change_done')
    template_name = 'account/pass_change.html'


class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'account/pass_change_done.html'

@login_required
def goulmet_create(request):
    """Goulmet情報登録"""
    user_count = GoulmetModel.objects.filter(user_id=request.session['_auth_user_id']).count()
    if user_count == 0:
        form = GoulmetUpdateForm(request.POST or None)
        if request.method == 'POST':
            object = GoulmetModel.objects.create(
                user_id = request.user,
                self_introduction = request.POST['self_introduction'],
                area = request.POST['area'],
                plan = request.POST['plan'],
                base_price = request.POST['base_price'],
                )
            object.save()
            return redirect('account:judge_start')
        else:
            return render(request,'account/goulmet_create.html')
    else:
        return render(request, 'account/judge_start.html')

@login_required
def judge_start(request):
    """審査開始"""
    return render(request, 'account/judge_start.html')

@login_required
def judge_clear(request):
    """審査開始"""
    return render(request, 'account/judge_clear.html')

@login_required
def goulmet_update(request):
    """Goulmet情報更新"""
    # urlを基に、GoulmetModelを取得
    goulmet = get_object_or_404(GoulmetModel, user_id=request.session['_auth_user_id'])

    #フォームに、取得したGoulmetModelを紐付ける
    form = GoulmetUpdateForm(request.POST or None, instance=goulmet)

    if goulmet.is_pass ==True:
        # method = POST、つまり送信ボタン押下時、入力内容に問題なければ
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('account:goulmet_detail')

        # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
        context = {
            'form': goulmet,
        }
        return render(request, 'account/goulmet_update.html', context)
    else:
        return HttpResponse('あなたはまだGoulmetに認定されていません。')

@login_required
def goulmet_detail(request):
    """Goulmet情報の更新成功"""
    object = GoulmetModel.objects.get(user_id=request.session['_auth_user_id'])
    return render(request, 'account/goulmet_detail.html', {'object': object})
    
@login_required
def option_list(request):
    """追加オプションリスト"""
    object_list = OptionModel.objects.all().filter(user_id=request.session['_auth_user_id'])
    return render(request,'account/option_list.html',{'object_list':object_list})

@login_required
def additional_option(request):
    """追加オプション登録"""
    form = OptionModel(request.POST or None)  

    if request.method == 'POST':
        
        object = OptionModel.objects.create(
            user_id = request.user,
            option = request.POST['option'],
            price = request.POST['price'],
            )
        object.save()
        return redirect('account:option_list')
    else:
        return render(request,'account/additional_option.html')

class OptionDelete(DeleteView):
    template_name = 'account/option_delete.html'
    model = OptionModel
    success_url = reverse_lazy('account:option_list')

class OptionUpdate(UpdateView):
    template_name = 'account/option_update.html'
    form_class =  OptionUpdateForm
    model = OptionModel
    success_url = reverse_lazy('account:optionlist')


        





