# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class Type(models.Model):
    class Meta:
        verbose_name = u"Tipo"
        verbose_name_plural = u"Tipo"

    title = models.CharField(max_length=200, verbose_name=u'Título')
    info = models.CharField(max_length=500, verbose_name=u'Información')
    publish_date = models.DateTimeField(verbose_name=u'Fecha de publicación', default=datetime.now, blank=True)

    def __unicode__(self):
        return u"%s" % self.title


class Location(models.Model):
    class Meta:
        verbose_name = u"Lugar"
        verbose_name_plural = u"Lugar"

    name = models.CharField(max_length=200, verbose_name=u'Nombre')
    details = models.CharField(max_length=500, verbose_name=u'Detalles')
    publish_date = models.DateTimeField(verbose_name=u'Fecha de publicación', default=datetime.now, blank=True)

    def __unicode__(self):
        return u"%s" % self.name


class Card(models.Model):
    class Meta:
        verbose_name = u"Tarjeta"
        verbose_name_plural = u"Tarjetas"

    title = models.CharField(max_length=200, verbose_name=u'Título')
    info = models.CharField(max_length=500, verbose_name=u'Información')
    type = models.ForeignKey(Type, related_name='cards_by_type', verbose_name=u'Tipo')
    location = models.ForeignKey(Location, related_name='cards_by_locations', verbose_name=u'Lugar')
    link = models.CharField(max_length=500, verbose_name=u'Liga')
    publish_date = models.DateTimeField( verbose_name=u'Fecha de publicación',  default=datetime.now, blank=True)

    def __unicode__(self):
        return u"%s" % self.title

