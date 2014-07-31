from annoying.decorators import render_to
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import HttpResponse, render_to_response
from django.core import serializers
from resumize.models import *

@render_to('home.html')
def home(request):
    return locals()

@render_to('resume.html')
def resume(request):
    return locals()

@csrf_exempt
def submit_resume(request):
    r = Resume(data=request.body)
    r.save()
    ret = { id: r.pk }
    return HttpResponse(serializers.serialize('json', ret), content_type="application/json")

def view_resume(request, id):
    r = Resume.objects.filter(pk=id).get()
    print json.loads(r.data)
    return render_to_response('resume.html', json.loads(r.data))
