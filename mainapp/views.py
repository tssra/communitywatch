from django.shortcuts import render,render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse
from mainapp.models import Story,Comment,Watch
import os

scores = {}

# Create your views here.
def index(request):
	title = 'Community Watch'
	stories = Story.objects.all()
	return render_to_response("mainapp/index.html", locals(), context_instance=RequestContext(request))

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

	stories = Story.objects.all()

	for s in stories:
		comments = Comment.objects.filter(story = s)
		tot = 0
		for c in comments:
			tot = tot + calcScore(c.description)
		avg = tot/comments.count()
		s.senti = avg
		s.save()


	return HttpResponse("dd")
