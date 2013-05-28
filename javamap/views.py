#!/usr/bin/python
#-*-coding:utf-8-*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse,Http404

def index(request):
    return render_to_response("index.html",context_instance = RequestContext(request))

def javamap(request):

    if request.is_ajax():
        years = ["2012","2013"]
        months = [[12,14,13,15,17,16,14,31,21,11,17,19],[12,19,10,13,40]]
        series = []
        for i,j in enumerate(years):
            series.append({
                'name':years[i],
                'data':months[i]
            })

        return HttpResponse(simplejson.dumps(series), mimetype='application/json')
    raise Http404 
