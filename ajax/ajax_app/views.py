from django.http import request
from django.shortcuts import render

import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def call_backend(request):
    print('VIEW')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        checked= request.POST.get('checked')

        response_data = {}

        response_data['username'] = username
        response_data['password'] = password
        print(username,password,checked)
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )