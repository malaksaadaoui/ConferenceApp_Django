from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import  RegexValidator
import uuid
def generate_id():
    return "USER"+uuid.uuid4().hex[:4].upper()
def verify_email(email):
    domaines=["esprit.tn","seasame.com","tek.tn","central.net"]
    email_domaine=email.split("@")[1]
    if email_domaine not in domaines:
        raise ValidationError("l'email est invalide et doit appartenir à un domaine universitaire privé")
    
name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s-]+$',
    message="ce champs ne doit contenir que des lettres et des espaces "
)
class User(AbstractUser):
    user_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name=models.CharField(max_length=255,validators=[name_validator])
    last_name=models.CharField(max_length=255,validators=[name_validator])
    affiliation=models.CharField(max_length=255)
    ROLE=[
        ("participant","participant"),
        ("commitee","organizing commitee member"),
    ]
    role=models.CharField(max_length=255,choices=ROLE,default="participant")
    nationality=models.CharField(max_length=255)
    email=models.EmailField(unique=True,validators=[verify_email])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        if not self.user_id:
            newid=generate_id()
            while User.objects.filter(user_id=newid).exists():
                newid=generate_id()
            self.user_id=newid
        super().save(*args,**kwargs)
# Create your models here.














