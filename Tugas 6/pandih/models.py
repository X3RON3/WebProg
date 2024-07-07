from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.functions import RandomUUID
from django.utils import timezone
from django.utils.html import escape, mark_safe
import uuid


# Create your models here.
class AccountUser(models.Model):
    account_user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    account_user_related_user = models.CharField(max_length=255, null=False, editable=False)
    account_user_fullname = models.CharField(max_length=255, null=False, editable=False)
    account_user_student_number = models.CharField(max_length=20, null=False)
    account_user_created_by = models.CharField(max_length=255, null=False)
    account_user_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    account_user_updated_by = models.CharField(max_length=255, null=True)
    account_user_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def _str_(self):
        return self.account_user_related_user

    def _unicode_(self):
        return '%s' % self.account_user_related_user

    @property    
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.account_user_id), 
            escape(self.account_user_related_user),            
            escape(self.account_user_fullname), 
            escape(self.account_user_student_number),            
            escape(self.account_user_created_by), 
            escape(self.account_user_created_date),            
            escape(self.account_user_updated_by), 
            escape(self.account_user_updated_date)
        )

    class Meta:
        ordering = ('account_user_related_user',)
        indexes = [models.Index(
            fields=[
                'account_user_id',                
                'account_user_related_user']), ]
        

class course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    course_name = models.CharField(max_length=255, null=False, editable=False)
    course_created_by = models.CharField(max_length=255, null=False)
    course_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    course_updated_by = models.CharField(max_length=255, null=True)
    course_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def _str_(self):
        return self.course_id

    def _unicode_(self):
        return '%s' % self.course_id

    @property    
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.course_id), 
            escape(self.course_name),           
            escape(self.course_created_by), 
            escape(self.course_created_date),            
            escape(self.course_updated_by), 
            escape(self.course_updated_date)
        )

    class Meta:
        ordering = ('course_id',)
        indexes = [models.Index(
            fields=[
                'course_id']), ]
        
class attendcourse(models.Model):
    attendcourse_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    attendcourseid = models.ForeignKey("course", on_delete=models.CASCADE)
    attendcourse_accountprofileid = models.CharField(max_length=255, null=False)
    attendcourse_created_by = models.CharField(max_length=255, null=False)
    attendcourse_created_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    attendcourse_updated_by = models.CharField(max_length=255, null=True)
    attendcourse_updated_date = models.DateTimeField(editable=False, null=False, auto_now_add=True)

    def _str_(self):
        return self.attendcourse_accountprofileid

    def _unicode_(self):
        return '%s' % self.attendcourse_accountprofileid

    @property    
    def friendly_profile(self):
        return mark_safe(u"%s <%s>") % (
            escape(self.attendcourse_id),
            escape(self.attendcourseid),
            escape(self.attendcourse_accountprofileid),             
            escape(self.attendcourse_created_by), 
            escape(self.attendcourse_created_date),            
            escape(self.attendcourse_updated_by), 
            escape(self.attendcourse_updated_date)
        )

    class Meta:
        ordering = ('attendcourse_id',)
        indexes = [models.Index(
            fields=[
                'attendcourse_id',                
                'attendcourse_id']), ]