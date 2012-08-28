# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Feeds.filename'
        db.add_column('loadimages_feeds', 'filename',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Feeds.filename'
        db.delete_column('loadimages_feeds', 'filename')

    models = {
        'loadimages.failedskus': {
            'Meta': {'object_name': 'FailedSKUs'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loadimages.Feeds']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sku': ('django.db.models.fields.TextField', [], {})
        },
        'loadimages.feeds': {
            'Meta': {'object_name': 'Feeds'},
            'filename': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['loadimages']