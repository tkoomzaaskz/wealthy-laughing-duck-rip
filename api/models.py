from django.db import models

class User(models.Model):
    """System user"""
    class Meta:
        db_table = 'sf_guard_user'
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    username = models.CharField(max_length=128)
    is_active = models.NullBooleanField()
    is_super_admin = models.NullBooleanField()
    last_login = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __unicode__(self):
        return self.first_name + " " + self.last_name
