from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

COLOR_CHOICE = (
    ('red','red'),
    ('green','green'),
    ('black','black'),
    ('yellow','yellow'),
    ('blue','blue'),
    ('orange','orange'),
    
)


SUBJECT_CHOICE = (
    ('math','math'),
    ('physics','physics'),
    ('history','history'),
    ('french','french'),
    ('english','english'),
    ('arabic','arabic'),

    
)

FRUITE_CHOICE = (
    ('orange','orange'),
    ('banana','banana'),
    ('mango','mango'),
    ('yosfi','yosfi'),
    ('watermelon','watermelon'),
    ('blueberry','blueberry'),
    
)
MOVIE_CHOICE = (
    ('horror','horror'),
    ('comedy','comedy'),
    ('action','action'),
    ('romance','romance'),
    ('science fiction' , 'science fiction')

    
)
HOBBY_CHOICE = (
    ('painting','painting'),
    ('football','football'),
    ('reading','reading'),
    ('gaming','gaming'),
    ('other_sport','other_sport'),
)

TEAM_CHOICE = (
    ('liverpool','liverpool'),
    ('real-madrid','real-madrid'),
    ('barca','barca'),
    ('juventus','juventus'),
    ('man-united','man-united'),
    ('man-city','man-city'),
    ('atletico-madrid','atletico-madrid'),
    ('arsenal','arsenal'),


)


class Personality(models.Model): 
    user = models.OneToOneField(User,  on_delete=models.CASCADE) 
    name = models.CharField( max_length=100 , null = True  , verbose_name='اسمك او لقبك الذي سيظهر في البحث' )
    age = models.CharField( max_length=50 , null = True , verbose_name='العمر' ) 
    color =   models.CharField( max_length=100 , null = True  , verbose_name='اللون المفضل' , choices= COLOR_CHOICE) 
    subject = models.CharField( max_length=100 , null = True  , verbose_name='المادة الاكاديمية المفضلة' ,choices= SUBJECT_CHOICE) 
    fruite =  models.CharField( max_length=100 , null = True  , verbose_name='الفاكهة المفضلة' ,choices= FRUITE_CHOICE)
    movie  =  models.CharField( max_length=100 , null = True  , verbose_name='نوع الافلام المفضلة ' ,choices= MOVIE_CHOICE) 
    hobby =   models.CharField( max_length=100 , null = True  , verbose_name='الهواية المفضلة',choices=HOBBY_CHOICE) 
    social =  models.BooleanField(null= True , verbose_name='هل انت اجتماعي' )
    team  =   models.CharField( max_length=100 , null = True  , verbose_name='الفريق العالمي المفضل'  ,choices=TEAM_CHOICE)
    facebook_profile_link= models.CharField( max_length=500  , verbose_name=' لينك بروفايل الفيسبوك ' , null = True)
    singer = models.CharField( max_length=150 , null = True , verbose_name='المغني العربي المفضل' ) 
   


    #img = models.ImageField( null = True)
    
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save , sender = User) 
def creat_user_personality(sender , instance , created , **kwargs): 
    if created: 
        Personality.objects.create(user= instance) 

