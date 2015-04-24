#-*- coding:utf-8 -*-
from django.shortcuts import render
import sys
from django.http.response import HttpResponse
reload(sys)
sys.setdefaultencoding('utf-8')

def index( request ):
    return render( request, 'index.html' )

def getDirectory( request ):
    return HttpResponse( "高数试卷.doc" )

def test( request ):
    return render(request,'test/test.html')