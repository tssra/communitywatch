from django.shortcuts import render
from django.http import HttpResponse
import os

scores = {}

# Create your views here.
def index(request):
	return render(request,'mainapp/base.html',)

def show_story(request):
	return render(request,'mainapp/story.html',)



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
