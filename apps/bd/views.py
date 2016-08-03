# coding=utf-8
import csv
import json
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.shortcuts import render
from apps.bd.models import ModuleContactListDB, Contact
from apps.client.models import Client
from apps.extra.utils import json_response


@login_required(login_url='/')
def get_module_db(request, module_db_id):
    """
    Gets data from selected mailing module_db
    :param request:
    :param module_db_id:
    """
    success = False
    errors = []
    module_db = None
    try:
        module_db = ModuleContactListDB.objects.get(id=module_db_id, owner__user=request.user)
        module_db = module_db.as_dict2
        success = True
    except ModuleContactListDB.DoesNotExist:
        errors = 200000
    data = {'module_db': module_db, 'errors': errors, 'success': success}
    return json_response(data)


@login_required(login_url='/')
def create_or_modify_module_db(request, module_db_id=None):
    """
    Create a new mailing module_db, or modify an existing one

    :param request:
    :param module_db_id:
    """
    success = False
    data_obj = {}
    errors = []
    try:
        if request.method == 'POST':
            json_obj = json.loads(request.body)
            list_name = json_obj.get('list_name', None)
            status = json_obj.get('status', None)
            origin = json_obj.get('origin', None)
            destination = json_obj.get('destination', None)
            if list_name:
                if module_db_id:
                    list_db = ModuleContactListDB.objects.get(id=module_db_id)
                    list_db.list_name = list_name
                    list_db.status = status
                    list_db.origin = origin
                    list_db.destination = destination
                    list_db.save()
                    data_obj = list_db.as_dict
                else:
                    current_user = Client.objects.get(user=request.user)
                    list_db = ModuleContactListDB.objects.create(
                        list_name=list_name,
                        owner=current_user,
                        origin=origin,
                        destination=destination,
                        status=status
                    )
                    data_obj = list_db.as_dict
                success = True
    except Exception as e:
        errors = e.args

    data = {'success': success, 'errors': errors, 'data': data_obj}
    return json_response(data)


@login_required(login_url='/')
def import_file_to_mailing_db(request, module_db_id):
    """
    Imports CSV file to mailing database
    :type list_id:
    :param request:
    :param event_id:
    """
    errors = []
    success = False
    if request.method == 'POST':
        try:
            file_data = request.FILES['file']
            if file_data:
                list_db = ModuleContactListDB.objects.get(id=module_db_id)
                if file_data.content_type == "text/csv":
                    csv_data = csv.reader(file_data, delimiter=',')
                    for row in csv_data:
                        if list_db.origin == 1 and list_db.destination == 2:
                            name = row[0]
                            email = row[1]
                            success, name, email = add_contact_to_db(
                                name, email, list_db.id)
                        elif list_db.origin == 2 and list_db.destination == 1:
                            name = row[1]
                            email = row[0]
                            success, name, email = add_contact_to_db(
                                name, email, list_db.id)
        except Exception as e:
            errors = e.args

    data = {'success': success,
            'errors': errors}
    return json_response(data)


def add_contact_to_db_by_one(name, email, module_db_id, contact_id):
    """
    Add imported line to db if data is correct
    :param email:
    :param name:
    :param list_db:
    """
    success = False
    if name is not None:
        try:
            done_email = email.lower().strip()
            validate_email(done_email)

            if contact_id:
                try:
                    contact = Contact.objects.get(id=contact_id, list_owner_id=module_db_id)
                    contact.name_and_last_name = name
                    contact.email = email
                    contact.status = 1
                    contact.save()
                    success = True
                except Contact.DoesNotExist:
                    pass
            else:
                contact, created = Contact.objects.get_or_create(list_owner_id=module_db_id, email=email)
                if created and contact:
                    contact.name_and_last_name = name
                    contact.status = 1
                    contact.save()
                    success = True
        except Exception as e:
            print(e.args)

    return success, name, email


def add_contact_to_db(name, email, module_db_id):
    """
    Add imported line to db if data is correct
    :param email:
    :param name:
    :param list_db:
    """
    success = False
    if name is not None:
        try:
            done_email = email.lower().strip()
            validate_email(done_email)

            contact, created = Contact.objects.get_or_create(list_owner_id=module_db_id, email=email)
            if created and contact:
                contact.name_and_last_name = name
                contact.email = email
                contact.status = 1
                contact.save()
                success = True
            else:
                success = False
        except Exception as e:
            print(e.args)
            contact, created = Contact.objects.get_or_create(list_owner_id=module_db_id, email=email)
            if created and contact:
                contact.name_and_last_name = name
                contact.email = email
                contact.status = 0
                contact.save()
                success = True
            else:
                success = False

    return success, name, email


@login_required(login_url='/')
def add_contact_data_to_contact_list(request, module_db_id):
    """
    Create new contact data to current list
    :param request:
    :param event_id:
    :param list_id:
    :return: :rtype:
    """
    success = False
    errors = []
    data_obj = None
    if request.method == 'POST':
        try:
            json_obj = json.loads(request.body)
            new_name = json_obj.get('name', '')
            new_email = json_obj.get('email', '')
            contact_id = json_obj.get('id', '')
            list_db = ModuleContactListDB.objects.get(id=module_db_id)

            success, name, email = add_contact_to_db_by_one(
                new_name, new_email, list_db.id, contact_id)
            if success:
                contact_data = Contact.objects.get(email=email)
                data_obj = contact_data.as_dict
            else:
                errors = ['630400']
        except ModuleContactListDB.DoesNotExist:
            errors = ['620404']

        except Exception as e:
            errors = e.args

    data = {'data': data_obj,
            'success': success,
            'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def module_db_list(request):
    """
    Lists all mailing module_db for this client

    :param request:
    :type request:
    :return:
    :rtype:
    """
    mailings = None
    errors = []
    try:
        mailings = ModuleContactListDB.objects.filter(owner__user=request.user)
        mailings = [m.as_dict for m in mailings]

    except Exception as e:
        errors = e.args

    data = {'module_dbs': mailings, 'errors': errors}
    return json_response(data)


@login_required(login_url='/')
def delete_module_db(request, module_db_id):
    """
    Removes mailing_db from client

    :param request:
    :param module_db_id:
    :return: :rtype:
    """
    errors = None
    success = False
    if request.method == 'DELETE':
        try:
            mailing = ModuleContactListDB.objects.get(id=module_db_id, owner__user=request.user)
            mailing.delete()
            success = True
        except ModuleContactListDB.DoesNotExist:
            errors = 200000

    data = {'success': success, 'errors': errors}
    return json_response(data)\

@login_required(login_url='/')
def delete_contacts_module_db(request, module_db_id):
    """
    Removes mailing_db from client

    :param request:
    :param module_db_id:
    :return: :rtype:
    """
    errors = None
    success = False
    if request.method == 'POST':
        try:
            json_obj = json.loads(request.body)
            list_ids = json_obj.get('list', '')
            try:
                for item_id in list_ids:
                    contact = Contact.objects.get(list_owner__id=module_db_id, id=item_id)
                    contact.delete()
                success = True
            except Contact.DoesNotExist as e:
                errors = e.args
        except ModuleContactListDB.DoesNotExist as e:
            errors = e.args

    data = {'success': success, 'errors': errors}
    return json_response(data)