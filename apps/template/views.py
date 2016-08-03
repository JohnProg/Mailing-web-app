# coding=utf-8
import json
from django.contrib.auth.decorators import login_required
from apps.client.models import Client
from apps.extra.constants import TEMPLATE_TYPE_CHOICES
from apps.extra.utils import json_response
from apps.template.models import ModuleTemplate, Template


@login_required(login_url='/')
def get_module_template(request, module_template_id):
    """
    Gets data from selected module template
    :param request:
    :param module_template_id:
    """
    success = False
    errors = []
    module_template = None
    try:
        module_template = ModuleTemplate.objects.get(id=module_template_id, owner__user=request.user)
        module_template = module_template.as_dict
        success = True
    except ModuleTemplate.DoesNotExist:
        errors = 300000
    data = {'module_template': module_template, 'errors': errors, 'success': success}
    return json_response(data)


@login_required(login_url='/')
def create_or_modify_module_template(request, module_template_id=None):
    """
    Create a new module template, or modify an existing one

    :param request:
    :param module_template_id:
    """
    success = False
    data_obj = {}
    errors = []
    try:
        if request.method == 'POST':
            data_obj = json.loads(request.body)
            if module_template_id:
                module_template = ModuleTemplate.objects.get(id=module_template_id)
                module_template.template_name = data_obj.get('name')
                module_template.status = data_obj.get('status')
                module_template.colors = data_obj.get('colorsJSON', '')
                module_template.save()
            else:
                current_user = Client.objects.get(user=request.user)
                ModuleTemplate.objects.create(
                    template_name=data_obj.get('name'),
                    status=data_obj.get('status'),
                    colors=data_obj.get('colorsJSON', ''),
                    owner=current_user
                )
            success = True
    except Exception as e:
        errors = e.args

    data = {'success': success, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def module_template_list(request):
    """
    Lists all module template for this client

    :param request:
    :type request:
    :return:
    :rtype:
    """
    module_templates = None
    errors = []
    try:
        module_templates = ModuleTemplate.objects.filter(owner__user=request.user)
        module_templates = [m.as_dict for m in module_templates]

    except Exception as e:
        errors = e.args

    data = {'module_templates': module_templates, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def delete_module_template(request, module_template_id):
    """
    Removes module template from client

    :param request:
    :param module_template_id:
    :return: :rtype:
    """
    errors = None
    success = False
    if request.method == 'DELETE':
        try:
            module_template = ModuleTemplate.objects.get(id=module_template_id, owner__user=request.user)
            module_template.delete()
            success = True
        except ModuleTemplate.DoesNotExist:
            errors = 300000

    data = {'success': success, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def template_list(request):
    """
    Lists all template from the system

    :param request:
    :type request:
    :return:
    :rtype:
    """
    success = False
    templates = None
    errors = None
    try:
        templates = []
        template_type = request.GET.get('type', None)
        if template_type:
            if template_type == '0' or template_type == '1':
                templates = Template.objects.filter(type='' + template_type)
                templates = [template.as_dict for template in templates]
                success = True
            else:
                errors = 300001
        else:
            templates = Template.objects.filter(id=1)
            templates = [template.as_dict for template in templates]
            success = True
    except Exception as e:
        errors = e.args

    data = {'templates': templates, 'errors': errors, 'success': success}
    return json_response(data)
