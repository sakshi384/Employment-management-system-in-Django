from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
# Create your models here.
class trial_details(models.Model):
    name=models.CharField(max_length=200,default="")
    email=models.EmailField(max_length=100,default="")
    location=models.CharField(max_length=200,default="")
    # image=models.ImageField(upload_to='pics',default="")
    technology=models.CharField(max_length=200,default="")
    domain=models.CharField(max_length=200,default="")
    project=models.CharField(max_length=500,default="")
    blogs=models.CharField(max_length=500,default="")
    # score=models.IntegerField(validators=[MaxLengthValidator(11),MinLengthValidator(11)], unique=True)
    # placed=models.BooleanField(default=False)

    # data=[name,email,location,technology,domain,project,blogs,score]


