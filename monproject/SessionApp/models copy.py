from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import  RegexValidator
room_verify= RegexValidator(
    regex=r'^[a-zA-Z0-9]+$',
    message="ce champ contient que des chiffres et des lettres"
)
def verify_time(start_time,end_time):
    if start_time and end_time:
        if start_time > end_time:
            raise ValidationError("start_time doit etre toujours supérieure à end_time!")
def verify_session_day (conference , session_day):
    if conference and session_day:
        if not conference.start_date <= session_day <=conference.end_date:
            raise ValidationError(f"la date de la session doit etre entre {conference.start_date} and {conference.end_date}")
class Session(models.Model):
    session_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    topic=models.CharField(max_length=255)
    session_day=models.DateField()
    start_time=models.DateField()
    end_time=models.DateField()
    room=models.CharField(max_length=255,validators=[room_verify])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    conference=models.ForeignKey("ConferenceApp.Conference",
                                  on_delete=models.CASCADE,
                                 related_name="sessions")
    def clean(self):
        verify_session_day (self.conference ,self.session_day)
        '''if self.start_time and self.end_time:
            if self.start_time>self.end_time:
                raise ValidationError("start_time doit etre toujours supérieure à end_time!")'''        
        verify_time(self.start_time,self.end_time)
        '''if self.session_day and self.conference:
            if not self.conference.start_date <= self.session_day <=self.conference.end_date:
                raise ValidationError(f"la date de la session {self.session_day} doit etre entre {self.conference.start_date} et {self.conference.end_date}")
'''

# Create your models here.
