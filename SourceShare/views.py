#-*- coding:utf-8 -*-
#$-$=ToSFE前后台数据交换格式约定
from django.shortcuts import render
from os import path, listdir
import sys
from json import dumps, loads
from django.http.response import HttpResponse
from fileHandlers import get_file_info_from_current_path


reload(sys)
sys.setdefaultencoding('utf-8')

def index( request ):
    return render( request, 'index.html' )

def getDirectory( request ):
    """
    根据GET请求中的path参数获取path路径下的所有文件夹名称和文件名称
    :param request:request.path：文件路径
    :return:$-$1.1
    """
    directory = request.GET['path']
    res       = dict()
    res['path'] = directory
    res['filedata'] = get_file_info_from_current_path(directory)
    response =  HttpResponse( dumps( res, ensure_ascii=False ) )
    return response

def test( request ):
    return render(request,'test/test.html')