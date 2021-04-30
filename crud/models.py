from django.db import models


# Create your models here.
class emp_details(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=200)
    # image=models.ImageField(upload_to='pics')
    technology=models.DataField(max_length=200)
    domain=models.CharField(max_length=200)
    project=models.CharField(max_length=500)
    blogs=models.CharField(max_length=500)
    score=models.IntegerField(null=True)
    placed=models.BooleanField(default=False)

    data=[id,name,email,location,technology,domain,project,blogs,score]

    def return_data(self):
        self.data

