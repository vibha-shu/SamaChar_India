from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=15)
    message=models.CharField(max_length=500)

    def __str__(self):
        return self.email

class hnews(models.Model):
    spick=models.ImageField(upload_to='static/category/', default="")
    sheadlines=models.CharField(max_length=400)
    city=models.CharField(max_length=200)
    subject=models.CharField(max_length=800)
    newsdes=models.TextField(max_length=8000)
    ndate = models.DateField()
    #ncategory=models.ForeignKey(category, on_delete=models.CASCADE)


class bnews(models.Model):
    bn=models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    subject = models.CharField(max_length=800)
    newsdes = models.TextField(max_length=8000)
    newspic = models.ImageField(upload_to='static/news', default="")
    ndate = models.DateField()
    #ncategory = models.ForeignKey(category, on_delete=models.CASCADE)

class category(models.Model):
    cname=models.CharField(max_length=30)
    cpick=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()
    def __str__(self):
        return self.cname

class newcategory(models.Model):
    ncategory=models.ForeignKey(category,on_delete=models.CASCADE)
    fpick=models.ImageField(upload_to='static/category/',default="")
    fcity = models.CharField(max_length=200)
    fsubject = models.CharField(max_length=800)
    fnewsdes = models.TextField(max_length=8000)
    fdate = models.DateField()
    fheadlines=models.CharField(max_length=400)
    sheadlines=models.CharField(max_length=400)
    scity = models.CharField(max_length=200)
    ssubject = models.CharField(max_length=800)
    snewsdes = models.TextField(max_length=8000)
    snewspic = models.ImageField(upload_to='static/news', default="")
    sdate = models.DateField()
    theadlines=models.CharField(max_length=400)
    tcity = models.CharField(max_length=200)
    tsubject = models.CharField(max_length=800)
    tnewsdes = models.TextField(max_length=8000)
    tnewspic = models.ImageField(upload_to='static/news', default="")
    tdate = models.DateField()
    foheadlines=models.CharField(max_length=400)
    focity = models.CharField(max_length=200)
    fosubject = models.CharField(max_length=800)
    fonewsdes = models.TextField(max_length=8000)
    fonewspic = models.ImageField(upload_to='static/news', default="")
    fodate = models.DateField()
    fiheadlines=models.CharField(max_length=400)
    ficity = models.CharField(max_length=200)
    fisubject = models.CharField(max_length=800)
    finewsdes = models.TextField(max_length=8000)
    finewspic = models.ImageField(upload_to='static/news', default="")
    fidate = models.DateField()

class trending(models.Model):
    ft=models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    subject = models.CharField(max_length=800)
    newsdes = models.TextField(max_length=8000)
    newspic = models.ImageField(upload_to='static/news', default="")
    ndate = models.DateField()
    ncategory = models.ForeignKey(category, on_delete=models.CASCADE)

class profile(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=20)
    ppick=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class news(models.Model):
    city=models.CharField(max_length=200)
    headlines=models.CharField(max_length=400)
    subject=models.CharField(max_length=800)
    newsdes=models.TextField(max_length=8000)
    newspic=models.ImageField(upload_to='static/news',default="")
    ndate=models.DateField()
    ncategory=models.ForeignKey(category,on_delete=models.CASCADE)

class tnews(models.Model):
    tnpick=models.ImageField(upload_to='static/news/', default="")
    tnheadlines=models.CharField(max_length=400)
    subject=models.CharField(max_length=800)
    newsdes=models.TextField(max_length=8000)
    city=models.CharField(max_length=200)
    ndate=models.DateField()
    ncategory=models.ForeignKey(category, on_delete=models.CASCADE)

class tsnews(models.Model):
    tspick=models.ImageField(upload_to='static/news/',default="")
    tsheadlines=models.CharField(max_length=400)
    subject=models.CharField(max_length=800)
    newsdes=models.TextField(max_length=8000)
    city=models.CharField(max_length=200)
    ndate=models.DateField()
    ncategory=models.ForeignKey(category, on_delete=models.CASCADE)

class videos(models.Model):
    #video=models.FileField(upload_to='static/videos/',default="")
    vheadlines=models.CharField(max_length=400)
    vdes=models.TextField(max_length=600,default="")
    thumb=models.ImageField(upload_to='static/thumbnail/',default="")
    vlink=models.URLField(default="")
    vdate=models.DateField(default="")
    city=models.CharField(max_length=200)
    vcategory=models.ForeignKey(category, on_delete=models.CASCADE)





