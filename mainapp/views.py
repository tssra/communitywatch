from django.contrib import auth
from django.http import HttpResponse
from mainapp.models import Story,Comment,Watch
from django.shortcuts import render,render_to_response, RequestContext, get_object_or_404,redirect

# Create your views here.
def index(request):
	title = 'Community Watch'
	stories = Story.objects.all()
	return render(request,"mainapp/index.html",{'stories':stories})

def show_story(request,storyid):
    s = get_object_or_404(Story, pk=storyid)
    title = 'Community Watch | ' + s.title
    return render_to_response("mainapp/story.html", locals(), context_instance=RequestContext(request))

def calcScore(text):
	tot = 0
	words = text.split(" ")
	words_scores = [scores[word] for word in words if word in scores]
	tot = sum(words_scores)
	return tot

def senti(request):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'static/mainapp/AFINN-111.txt')
	# return HttpResponse(file_path)
	afinnfile = open(file_path)
    
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	senti = calcScore("I am disappointed")

	return HttpResponse(senti)

def login(request):
    if(request.method=='GET'):
        return render(request, 'mainapp/login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if(user):
                auth.login(request,user)
                return redirect('index')
            else:
                return render(request,'mainapp/login.html',{'message':'Cook not found'})
        else:
            return render(request,'mainapp/login.html',{'message':'Invalid login'})

def logout(request):
    auth.logout(request)
    return redirect('index')
