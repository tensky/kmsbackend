import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import firestore, credentials
import firebase_admin
import json
from firebaseapp.forms import KmsForm, KmsDeleteForm, KmsUpdateForm


# Create your views here.
@csrf_exempt
def fetchAll(request):
    if request.method != 'GET':
        response_data = {
            'status': '500',
            'reason': 'This is a GET method'
        }
        return JsonResponse(response_data)

    db = firestore.client()
    colref = db.collection(u'kms').stream()

    firebase_data = []

    for doc in colref:
        docdict = doc.to_dict()
        record = {
            'id': doc.id,
            'name': docdict['name'],
            'age': docdict['age'],
            'weight': docdict['weight'],
            'height': docdict['height'],
            'institution': docdict['institution'],
            'location': docdict['location'],
            'date': docdict['tanggal'],
        }
        firebase_data.append(record)

    response_data = {
        'status': 'ok',
        'data': firebase_data
    }

    return JsonResponse(response_data)


@csrf_exempt
def insert(request):
    db = firestore.client()
    colref = db.collection(u'kms')
    if request.method != 'POST':
        response_data = {
            'status': '500',
            'reason': 'This is a POST method'
        }
        return JsonResponse(response_data)
    form = KmsForm(request.POST)
    if form.is_valid():
        print(form['name'].value())
        data = {
            u'name': form['name'].value(),
            u'age': form['age'].value(),
            u'height': form['height'].value(),
            u'institution': form['institution'].value(),
            u'location': form['location'].value(),
            u'weight': form['weight'].value(),
            u'tanggal': datetime.datetime.now(),
        }
        colref.document().set(data)
    else:
        response_data = {
            'status': 'failed',
            'reason': 'Form not valid'
        }
        return JsonResponse(response_data)
    response_data = {
        'status': '200',
        'reason': 'Insert Success'
    }
    return JsonResponse(response_data)


@csrf_exempt
def delete(request):
    db = firestore.client()
    colref = db.collection(u'kms')
    if request.method != 'POST':
        response_data = {
            'status': '500',
            'reason': 'This is a POST method'
        }
        return JsonResponse(response_data)

    form = KmsDeleteForm(request.POST)

    if form.is_valid():
        print(form['document_id'].value())
        colref.document(u'' + form['document_id'].value()).delete()
    else:
        response_data = {
            'status': 'failed',
            'reason': 'Form not valid'
        }
        return JsonResponse(response_data)

    response_data = {
        'status': '200',
        'reason': 'Delete Success'
    }
    return JsonResponse(response_data)


@csrf_exempt
def update(request):
    db = firestore.client()
    colref = db.collection(u'kms')
    if request.method != 'POST':
        response_data = {
            'status': '500',
            'reason': 'This is a POST method'
        }
        return JsonResponse(response_data)
    form = KmsUpdateForm(request.POST)

    if form.is_valid():
        data = {
            u'name': form['name'].value(),
            u'age': form['age'].value(),
            u'height': form['height'].value(),
            u'institution': form['institution'].value(),
            u'location': form['location'].value(),
            u'weight': form['weight'].value(),
            u'tanggal': datetime.datetime.now(),
        }
        colref.document(u'' + form['document_id'].value()).set(data)
    else:
        response_data = {
            'status': 'failed',
            'reason': 'Form not valid'
        }
        return JsonResponse(response_data)
    response_data = {
        'status': '200',
        'reason': 'Update Success'
    }
    return JsonResponse(response_data)
