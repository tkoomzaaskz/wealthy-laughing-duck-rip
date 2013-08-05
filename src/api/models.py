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

class Category(models.Model):
    """finance category"""
    class Meta:
        db_table = 'category'
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=32)
    TYPES = (
        ('outcome', 'outcome'),
        ('income', 'income'),
    )
    type = models.CharField(max_length=7,choices=TYPES)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_by = models.ForeignKey(User, db_column='created_by', related_name='createdCategories')
    updated_by = models.ForeignKey(User, db_column='updated_by', related_name='updatedCategories')
    def __unicode__(self):
        return self.first_name + " " + self.last_name