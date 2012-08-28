# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feeds.latest_sku'
        db.delete_column('loadimages_feeds', 'latest_sku')

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Feeds.latest_sku'
        raise RuntimeError("Cannot reverse this migration. 'Feeds.latest_sku' and its values cannot be restored.")
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['loadimages']