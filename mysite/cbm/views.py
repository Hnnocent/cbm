from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from django.http import HttpRequest
from . import models
from . import forms
# Create your views here.




def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'cbm/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'cbm/login.html', locals())
        else:
            return render(request, 'cbm/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'cbm/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'cbm/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'cbm/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'cbm/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'cbm/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'cbm/register.html', locals())


def logout(request):
    pass
    return redirect("/login/")


def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'cbm/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def seed_display(request):
    """Renders the seed_display page."""
    assert isinstance(request, HttpRequest)
    all_seedinformation = models.Seed.objects.all()
    return render(
        request,
        'cbm/seed_display.html',
        {'all_seedinformation': all_seedinformation,
         }
    )


def seed_add(request):
    """Renders the seed_add page."""
    if request.method == 'POST':
        seedno = request.POST.get('seed_add')
        support = request.POST.get('support_add')
        origin = request.POST.get('origin_add')
        its1 = request.POST.get('its1_add')
        its2 = request.POST.get('its2_add')
        pcr_relf = request.POST.get('pcr_relf_add')
        species = request.POST.get('species_add')

        if models.Seed.objects.filter(seedno=seedno):
            return render(request, 'cbm/seed_add.html', {'error': '该种子已经存在'})

        # elif not seedno:
        #    return render(request,'cbm/seed_add.html',{'error':'种子编号不能为空'})

        else:
            '''
                        models.Seed.objects.create(seedno=seedno)
                        models.Seed.objects.create(support=support)
                        models.Seed.objects.create(origin=origin)
                        models.Seed.objects.create(species=species)
                        models.Seed.objects.create(its1=its1)
                        models.Seed.objects.create(its2=its2)
                        models.Seed.objects.create(rcrrelf=pcr_relf)
            '''
            new_seed = models.Seed()
            new_seed.seedno = seedno
            new_seed.support = support
            new_seed.origin = origin
            new_seed.species = species
            new_seed.its1 = its1
            new_seed.its2 = its2
            new_seed.pcr_relf = pcr_relf
            new_seed.save()

        return redirect('/seed_display/')

    # assert isinstance(request, HttpRequest)
    # all_seedinformation = models.Seed.objects.all()
    return render(
        request,
        'cbm/seed_add.html'
    )


def seed_del(request):
    """Renders the seed_del page."""
    # assert isinstance(request, HttpRequest)
    # all_seedinformation = models.Seed.objects.all()
    pk = request.GET.get('seedno')
    models.Seed.objects.filter(pk=pk).delete()

    return redirect('/seed_display/')


def seed_edit(request):
    """Renders the seed_eidt page."""
    # assert isinstance(request, HttpRequest)
    # all_seedinformation = models.Seed.objects.all()

    pk = request.GET.get('seedno')
    pub_obj = models.Seed.objects.filter(pk=pk)

    if request.method == 'GET':
        return render(request, 'seed_edit.html', {'pub_obj': pub_obj})

    else:
        pub_seedno = request.POST.get('seedno_add')
        pub_support = request.POST.get('support_add')
        pub_origin = request.POST.get('origin_add')
        pub_species = request.POST.get('species_add')
        pub_pcrrelf = request.POST.get('pcr_relf_add')
        pub_its1 = request.POST.get('its1_add')
        pub_its2 = request.POST.get('its2_add')

        pub_obj.seedno = pub_seedno
        pub_obj.support = pub_support
        pub_obj.origin = pub_origin
        pub_obj.species = pub_species
        pub_obj.rcrrelf = pub_pcrrelf
        pub_obj.its1 = pub_its1
        pub_obj.its2 = pub_its2
        pub_obj.save()
        return redirect('/seed_display/')
