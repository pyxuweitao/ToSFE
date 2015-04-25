#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class FileInfo( models.Model ):
    class Meta:
        db_table = "fileInfo"
        ordering = ['filename']

    fileName      = models.CharField( max_length=30 )
    path          = models.FileField( u'文件存放路径' )
    downloadCount = models.BigIntegerField( default=0 )
    #uploaduser    = models.
    def __unicode__(self):
        return self.fileName

