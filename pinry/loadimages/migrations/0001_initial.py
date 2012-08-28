# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feeds'
        db.create_table('loadimages_feeds', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('latest_sku', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('loadimages', ['Feeds'])

    def backwards(self, orm):
        # Deleting model 'Feeds'
        db.delete_table('loadimages_feeds')

    models = {
        'loadimages.feeds': {
            'Meta': {'object_name': 'Feeds'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_sku': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['loadimages']