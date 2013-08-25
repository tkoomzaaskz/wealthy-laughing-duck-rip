from django.db import models

class User(models.Model):
    """System user"""
    class Meta:
        db_table = 'users'
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
    """Finance category"""
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

class Income(models.Model):
    """Financial incomes"""
    class Meta:
        db_table = 'income'
    category = models.ForeignKey(Category)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, db_column='created_by', related_name='createdIncomes')

class Outcome(models.Model):
    """Financial outcomes"""
    class Meta:
        db_table = 'outcome'
    category = models.ForeignKey(Category)
    comment = models.TextField()
    cash_total = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, db_column='created_by', related_name='createdOutcomes')
