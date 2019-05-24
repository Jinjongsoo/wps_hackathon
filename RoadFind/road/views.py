from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

#object 생성하는 뷰 새로운 데이터를 넣을때
from django.views.generic.edit import CreateView

#회원가입 form - id / pw 만 확인 - 현재 form (이메일없기때문에 추가)
from django.contrib.auth.forms import UserCreationForm

# 이건 Django 1.x 버전꺼
#from django.core.urlresolvers import reverse_lazy
# 이건 Django 2.x 버전꺼
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.shortcuts import get_list_or_404
from .models import *
from django.db.models import Q


class IndexView(TemplateView): # template 상속
    template_name = 'road/index.html'



class CreateUserView(CreateView):
    template_name = 'registration/signup.html' # 연결
    form_class = CreateUserForm
    #form_class = UserCreationForm # 만든거 아님 위에꺼 그대로 쓴거
    success_url = reverse_lazy('create_user_done') # 성공하면 여기로


class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'


def Search_list(request):
    search_key = request.GET.get('search_key', None)
    search_type = request.GET.get('search_type', None)

    search_q = None

    if search_key and search_type:
        if 'Author' in search_type:
            temp_q = Q(author__username__icontains=search_key)
            search_q = search_q | temp_q if search_q else temp_q
        if 'Title' in search_type:
            temp_q = Q(title__icontains=search_key)
            search_q = search_q | temp_q if search_q else temp_q
        if 'Text' in search_type:
            temp_q = Q(text__icontains=search_key)
            search_q = search_q | temp_q if search_q else temp_q

        searchs = get_list_or_404(Search, search_q)
    else:
        searchs = get_list_or_404(Search)

    return render(request, 'road/base.html', {'object_list': searchs})

