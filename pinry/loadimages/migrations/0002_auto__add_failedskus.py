# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FailedSKUs'
        db.create_table('loadimages_failedskus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loadimages.Feeds'])),
            ('sku', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('loadimages', ['FailedSKUs'])

    def backwards(self, orm):
        # Deleting model 'FailedSKUs'
        db.delete_table('loadimages_failedskus')

    models = {
        'loadimages.failedskus': {
            'Meta': {'object_name': 'FailedSKUs'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loadimages.Feeds']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.TextField', [], {})
        },
        'loadimages.feeds': {
            'Meta': {'object_name': 'Feeds'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_sku': ('django.db.models.fields.IntegerField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['loadimages']