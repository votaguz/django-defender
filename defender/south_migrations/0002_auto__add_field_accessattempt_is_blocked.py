# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AccessAttempt.is_blocked'
        db.add_column(u'defender_accessattempt', 'is_blocked',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AccessAttempt.is_blocked'
        db.delete_column(u'defender_accessattempt', 'is_blocked')


    models = {
        u'defender.accessattempt': {
            'Meta': {'ordering': "[u'-attempt_time']", 'object_name': 'AccessAttempt'},
            'attempt_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '1025'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['defender']