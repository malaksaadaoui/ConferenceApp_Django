from django.db import models
from django.core.validators import  RegexValidator,MinLengthValidator,FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
name_validator = RegexValidator(
    regex=r'^[a-zA-Z\s]+$',
    message="ce champs ne doit contenir que des lettres et des espaces "
)
class Conference(models.Model):
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,validators=[name_validator])
    THEME=[
        ("IA","Computer science & ia"),
        ("SE","Science & eng"),
        ("SC","Social sciences"),
    ]
    theme=models.CharField(max_length=255,choices=THEME)
    location=models.CharField(max_length=255)#charfield Stocke du texte court.
    start_date=models.DateField()
    end_date=models.DateField()
    description=models.TextField(validators=[
            MinLengthValidator(30, message="La description doit contenir au moins 30 caractères.")]) #Stocke du texte long
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("la date de début de la conférence doit être superieur à la date fin ")
        
    def __str__(self):
        return f"la conference a comme titre {self.name}"
import uuid
def generate_submission_id():
    return "SUB-"+uuid.uuid4().hex[:8].upper()
class Submission(models.Model):
    submission_id=models.CharField(primary_key=True,max_length=255,unique=True,editable=False)
    title=models.CharField(max_length=255)
    abstract=models.TextField(max_length=255)
    keywords=models.TextField(max_length=255)
    paper=models.FileField(
        upload_to="papers/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])]
    )
    STATUS=[
        ("submitted","submitted"),
        ("under review","under review"),
        ("accepted","accepted"),
        ("rejected","rejected"),
    ]
    status=models.CharField(max_length=255,choices=STATUS)
    submission_date=models.DateField(auto_now_add=True)
    payed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,
                           related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,
                                 related_name="submissions")
    def clean(self):
        keyword_list=[]
        if self.keywords :
            for k in self.keywords.split(",") :
                if k:
                    keyword_list.append(k)
        if len(keyword_list) > 10:
            raise ValidationError({"keywords": "Vous ne pouvez pas saisir plus de 10 mots-clés."})
        
        if self.submission_date and self.conference.start_date:
            if self.Conference.start_date < timezone.now().date():
                raise ValidationError("La soumission ne peut être faite que pour des conférences à venir.")
            
        if self.user_id:
            submission=Submission.objects.filter(
                user=self.user,
                submission_date=timezone.now().date()
            ).count()
            if submission>3:
                raise ValidationError("Vous ne pouvez pas soumettre plus de 3 conférences par jour.")
    
    def save(self,*args,**kwargs):
        if not self.submission_id:
            newid=generate_submission_id()
            while Submission.objects.filter(submission_id=newid).exists():
                newid=generate_submission_id()
            self.submission_id=newid
        super().save(*args,**kwargs)

class Organisation(models.Model):
    ROLE=[
        ("président","président"),
        ("co-président","co-président"),
        ("membres","membres"),
    ]
    comitee_role=models.CharField(max_length=255,choices=ROLE)
    join_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,
                           related_name="Organisation")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,
                                 related_name="Organisation")
    def __str__(self):
        return f"{self.user.username} - {self.commitee_role} ({self.conference.name})"


# Create your models here.









