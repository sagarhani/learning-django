from django.shortcuts import render

from .forms import SignUpForm, ContactForm
# Create your views here.
def home(request):
	title = "Welcome!"
	form = SignUpForm(request.POST or None)

	context = {
	    "title": title,
	    "form": form,
	}


	if form.is_valid():
		form.save()
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")

		#if not instance.full_name:
		#	instance.full_name == "Baymax"
		instance.save()
		context = {
		"title" : "Thank You"
		}
		
	return render(request, "home.html", context)
    

def contact(request):
	form = ContactForm(request.POST or None)
	context = {
		"form" : form,
	}
	return render(request, "forms.html", context)
