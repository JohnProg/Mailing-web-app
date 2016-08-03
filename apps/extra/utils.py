# coding=utf-8
import json
from django.http import HttpResponse
import mandrill
from apps.campaign.models import MandrillSent

from apps.extra.mandrill_app.auth import MANDRILL_TOKEN_AUTH


def json_response(response_dict, status=200):
    """
    Returns a JSON dumped from a dict

    :param response_dict: dictionary to convert to json
    :param status: Response status
    :return: json
    """
    response = HttpResponse(
        json.dumps(response_dict),
        content_type="application/json", status=status)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response


def send_mail_via_mandrill(person_email, person_name, mail_subject,
                           template_name, template_content, recipients=None,
                           sender_email=None, sender_name=None, tag=None):
    """
    Sends email to person using MandrillApp
    :param person_email:
    :param person_name:
    :param mail_subject:
    :param template_name:
    :param template_content:
    :param recipients:
    :param sender_name:
    :param sender_email:
    :raise:
    """
    try:
        if not recipients:
            recipients = [{'email': person_email,
                           'name': person_name,
                           'type': 'to'}]
        mandrill_client = mandrill.Mandrill(MANDRILL_TOKEN_AUTH)
        message = {
            'from_email': sender_email if sender_email else 'no-reply@demo.com',
            'from_name': sender_name if sender_name else 'demo',
            'global_merge_vars': template_content,
            'merge': True,
            'subject': mail_subject,
            'tags': [tag],
            'to': recipients,
            'url_strip_qs': None,
        }
        mandrill_responses = mandrill_client.messages.send_template(
            template_name=template_name,
            template_content=template_content,
            message=message, async=True)
        for mandrill_response in mandrill_responses:
            status = mandrill_response.get('status', '')
            _id = mandrill_response.get('_id', '')
            email = mandrill_response.get('email', '')
            reject_reason = mandrill_response.get('reject_reason', '')
            MandrillSent.objects.create(
                status=status, _id=_id, email=email,
                reject_reason=reject_reason)

    except mandrill.Error, e:
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        raise


def get_info_from_tags(tag):
    mandrill_client = mandrill.Mandrill(MANDRILL_TOKEN_AUTH)
    result = mandrill_client.tags.info(tag=tag)
    return result


def get_info_from_messages(tag):
    mandrill_client = mandrill.Mandrill(MANDRILL_TOKEN_AUTH)

    tags = [tag]
    result = mandrill_client.messages.search(query='*',
                                             date_from=None,
                                             date_to=None,
                                             tags=tags,
                                             api_keys=None,
                                             limit=100)
    return result