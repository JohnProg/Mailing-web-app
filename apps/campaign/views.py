# coding=utf-8
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.bd.models import ModuleContactListDB, Contact
from apps.campaign.models import ModuleCampaign
from apps.client.models import Client
from apps.extra.utils import json_response, send_mail_via_mandrill, get_info_from_tags, get_info_from_messages
from apps.template.models import ModuleTemplate


@login_required(login_url='/')
def get_mailing_campaign(request, mailing_id):
    """
    Gets data from selected mailing campaign
    :param request:
    :param mailing_id:
    """
    success = False
    errors = []
    campaign = None
    try:
        campaign = ModuleCampaign.objects.get(id=mailing_id, owner__user=request.user)
        campaign = campaign.as_dict2
        success = True
    except ModuleCampaign.DoesNotExist:
        errors = 200000
    data = {'campaign': campaign, 'errors': errors, 'success': success}
    return json_response(data)


@login_required(login_url='/')
def create_or_modify_mailing_campaign(request, mailing_id=None):
    """
    Create a new mailing campaign, or modify an existing one

    :param request:
    :param mailing_id:
    """
    success = False
    data_obj = {}
    errors = []
    try:
        if request.method == 'POST':
            json_obj = json.loads(request.body)
            campaign_name = json_obj.get('campaign_name', None)
            from_name = json_obj.get('from_name', None)
            reply_email = json_obj.get('reply_email', None)
            subject = json_obj.get('subject', None)
            link_redirect_to = json_obj.get('link_redirect_to', None)
            title = json_obj.get('title', None)
            subtitle = json_obj.get('subtitle', None)
            body_section1 = json_obj.get('body_section1', None)
            body_section2 = json_obj.get('body_section2', None)
            type = json_obj.get('type', None)
            template_id = json_obj.get('template_id', None)
            db_ids = json_obj.get('db_ids', None)

            current_template = ModuleTemplate.objects.get(id=template_id)

            if mailing_id:
                mailing = ModuleCampaign.objects.get(id=mailing_id, owner__user=request.user)
                mailing.campaign_name = campaign_name
                mailing.from_name = from_name
                mailing.reply_email = reply_email
                mailing.subject = subject
                mailing.link_redirect_to = link_redirect_to
                mailing.title = title
                mailing.subtitle = subtitle
                mailing.body_section1 = body_section1
                mailing.body_section2 = body_section2
                mailing.template_campaign = current_template

                mailing, recipients = set_and_get_contacts_list(mailing, db_ids)
                mailing.save()
                data_obj = mailing.as_dict
            else:
                current_user = Client.objects.get(user=request.user)
                mailing = ModuleCampaign.objects.create(
                    campaign_name=campaign_name,
                    from_name=from_name,
                    reply_email=reply_email,
                    owner=current_user,
                    template_campaign=current_template,
                    subject=subject,
                    link_redirect_to=link_redirect_to,
                    title=title,
                    status=1,
                    subtitle=subtitle,
                    body_section1=body_section1,
                    body_section2=body_section2

                )
                mailing, recipients = set_and_get_contacts_list(mailing, db_ids)
                mailing.save()
                data_obj = mailing.as_dict
            # send campaign
            if type == 2:
                send_mail_via_mandrill(None, None, mailing.subject, "test_practicas",
                                       get_template_context_for_mailing(mailing), recipients,
                                       mailing.reply_email, mailing.from_name, mailing.id)
                mailing.date_send = datetime.datetime.now()
                mailing.save()
            success = True
    except Exception as e:
        errors = e.args

    data = {'success': success, 'errors': errors, 'data': data_obj}
    return json_response(data)

def get_template_context_for_mailing(mailing):
    template_content = [
        {'name': 'redirect_to', 'content': mailing.link_redirect_to},
        {'name': 'title', 'content': mailing.title},
        {'name': 'subtitle', 'content': mailing.subtitle},
        {'name': 'body_section1', 'content': mailing.body_section1},
        {'name': 'body_section2', 'content': mailing.body_section2},
    ]
    add_colors_to_template_content(mailing, template_content)
    return template_content

def add_colors_to_template_content(mailing, template_content):
    colors = json.loads(mailing.template_campaign.colors)
    for key in colors.keys():
        if colors.get(key, ''):
            template_content.append({
                'name': key,
                'content': colors.get(key, '')
            })
    return template_content

def set_and_get_contacts_list(mailing, db_ids):
    recipients = []
    mailing.list_contacts.clear()
    for list_db in db_ids:
        list_db = ModuleContactListDB.objects.get(id=list_db)
        mailing.list_contacts.add(list_db)
        recipients += [c.as_dict for c in Contact.objects.filter(list_owner=list_db, status=1)]

    return mailing, recipients


@login_required(login_url='/')
def mailing_list(request):
    """
    Lists all mailing campaign for this client

    :param request:
    :type request:
    :return:
    :rtype:
    """
    mailings = None
    errors = []
    try:
        mailings = ModuleCampaign.objects.filter(owner__user=request.user)
        mailings = [m.as_dict for m in mailings]
    except Exception as e:
        errors = e.args

    data = {'campaigns': mailings, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def delete_mailing(request, mailing_id):
    """
    Removes mailing_db from client

    :param request:
    :param mailing_id:
    :return: :rtype:
    """
    errors = None
    success = False
    if request.method == 'DELETE':
        try:
            mailing = ModuleCampaign.objects.get(id=mailing_id, owner__user=request.user)
            mailing.delete()
            success = True
        except ModuleCampaign.DoesNotExist:
            errors = 200000

    data = {'success': success, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def get_data_from_tag_for_statistics(request, mailing_id=None):
    """
    Get data from the mailing campaign's emails
    :param request:
    :param mailing_id:
    """
    errors = []
    data = []
    try:
        data = get_info_from_tags(mailing_id)
    except Exception as e:
        errors = e.args
    data = {'data': data, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def get_data_info_from_tag_for_statistics(request, mailing_id=None):
    """
    Get data info(email, name) from the mailing campaign's emails
    :param request:
    :param mailing_id:
    """
    errors = []
    data = []
    try:
        data = get_info_from_messages(mailing_id)
    except Exception as e:
        errors = e.args
    data = {'data': data, 'errors': errors}
    return json_response(data)