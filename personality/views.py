from django.shortcuts import render , redirect
from .models import Personality 
from django.contrib.auth.models import User
from .forms import PersonalityForm 
from django.urls import reverse  
from django.contrib.auth.decorators import login_required
# Create your views here.




def profile(request): 
    profile = Personality.objects.get(user = request.user)
    return render(request , 'accounts/profile.html' , {'profile':profile} ) 


########################

@login_required
def create_personality(request): 
    if request.method == 'POST': 
        form = PersonalityForm(request.POST , instance=request.user) 
        if form.is_valid(): 
            myform = form.save(commit=False)
            myform.user = request.user                                                                       
            myform.save()                 
            return redirect(reverse('profile'))
    else: 
        form = PersonalityForm() 

    return render(request , 'accounts/add_personality.html' , {'form':form})

#########################

@login_required
def personality_list(request): 
    qs = Personality.objects.all()

    filter = Personality.objects.all().filter( 
        
        color__icontains=request.user.personality.color ,
        subject__icontains=request.user.personality.subject ,
        hobby__icontains=request.user.personality.hobby ,
        team__icontains=request.user.personality.team ,
        
         )
    
    return render(request , 'personality_list.html' , {'qs':filter})  


#########################


def personality_details(request, id): 
    personality_details = Personality.objects.get(id =id)
    return render(request , 'personality_detail.html' , {'personality':personality_details})



#########################


def search(request): 
    if request.method == 'GET': 
        search = request.GET.get("search")
        qs = Personality.objects.all().filter(name__icontains = search).order_by('-id')[:10]  
        return render(request , 'search.html' , {'qs':qs})

