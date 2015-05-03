#-*- coding:utf-8 -*-
__author__ = 'xuweitao'
from os import path, listdir
from datetime import datetime
import math

PATH_INI = u'/home/xuweitao/Projects/ToSFE/SourceShare/Storage'

class FileInfo( object ):
    """
    文件信息类，包括文件名称，文件类型（文件夹），文件最近一次修改时间等，详见数据交换格式文档1.1章节
    """
    UNITS  = [u'B', u'KB', u'MB', u'GB', u'TB']
    def __init__(self, file_name="", file_path="" ):
        self.file_name      = file_name
        self.file_path      = file_path
        if len(file_name)==0 and len(file_path)==0:
            self.file_type      = 0
            self.file_size      = 0
            self.modified_time  = ""
            self.download_count = 0
            self.uploader       = u"徐维涛"
        else:
            self.file_type      = 1 if path.isdir(file_path) else 0
            try:
                self.file_size      = self.__get_file_size
            except Exception,e:
                print e
            self.modified_time  = datetime.fromtimestamp( path.getmtime( file_path ) ).strftime( "%Y-%m-%d %R" )
            #TODO:download_count
            self.download_count = 0
            self.uploader       = u"徐维涛"

    def __unicode__(self):
        return self.file_name

    def __str__(self):
        return self.file_name

    @property
    def serialized(self):
        """
        将对象转成字典格式输出
        :return:
        """
        return { 'name':self.file_name, 'type':self.file_type,
                 'size':self.file_size, 'time':self.modified_time,
                 'uploader':self.uploader, 'download_count':self.download_count}

    @property
    def __get_file_size(self):
        """
        返回一个长度加单位的字串，长度小于1KB用字节，大于用MB，再大用GB,如果是文件夹或者文件路径不存在则返回字符串0
        :return:string,e.p:"1kb"
        """
        if self.file_path == "" or self.file_type == 1:
            return "0"
        else:
            size   = path.getsize( self.file_path )
            if size > 0:
                unit_i = math.floor( math.log(size, 1024) )
                return u" ".join( ( unicode( round( size / ( 1024 ** unit_i ), 2 ) ), self.UNITS[int(unit_i)] ) )
            else:
                return u"0 B"


def get_file_info_from_current_path( current_path ):
    all_file_info = list()
    current_path = PATH_INI + current_path
    if path.exists( current_path ):
        fileList = listdir( current_path )
        for elementName in fileList:
            now_path  = path.join(current_path, elementName)
            file_info = FileInfo( elementName, now_path ).serialized
            all_file_info.append( file_info )
        def sortMethod(x,y):
            if x['type'] > y['type']:
                return -1
            elif x['type'] < y['type']:
                return 1
            elif x['name'] < y['name']:
                return -1
            elif x['name'] > y['name']:
                return 1
            else:
                return 0
        all_file_info.sort( cmp=sortMethod)
    return all_file_info

if __name__ == "__main__":
    for one in get_file_info_from_current_path( '/home/xuweitao/Downloads' ):
        print one