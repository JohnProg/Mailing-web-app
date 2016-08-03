# coding=utf-8
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from apps.extra.utils import json_response


class HomeView(TemplateView):
    template_name = "public/home.html"


def login_user(request):
    """
    Login a user

    :param request: web request
    :return: json
    """
    status = 200
    data = {'user': {'id': None}, 'errors': None, 'success': False}
    if request.method == 'POST':
        json_obj = json.loads(request.body)
        username = json_obj.get('username', u'')
        password = json_obj.get('password', u'')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data.update(
                    {
                        'user': {
                            'id': user.id,
                            'is_active': user.is_active
                        },
                        'success': True
                    })
            else:
                data.update({'user': {'id': None}})
                data.update({'errors': [100001]})
                data.update({'success': False})

        else:
            data.update({'errors': [100000]})
            data.update({'success': False})
        return json_response(data)
    else:
        return render(request, "public/login.html", data)
    return redirect("/")


def logout_user(request):
    """
    Logout a user

    :param request: web request
    :return: json
    """
    try:
        request.session.flush()
        logout(request)
        for skey in request.session.keys():
            del request.session[skey]
        data = {'success': True}
    except Exception as e:
        data = {'success': False, 'errors': e.args}

    return json_response(data)


@login_required(login_url='/login')
def admin_view(request):
    return render(request, "admin/dashboard.html", {})
