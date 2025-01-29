from django.shortcuts import render, redirect
from markdown2 import Markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
from django import forms
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(
        label="title", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-8', 'placeholder': 'Titulo de la entrada'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control col-md-8 col-lg-8', 'placeholder': 'Contenido de la entrada'})
    )
    edit = forms.BooleanField(
        initial=False,
        widget=forms.HiddenInput(),
        required=False
    )

def edit(request, entry):
    entry_page = util.get_entry(entry)
    if entry_page is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "The requested page was not found."
        })
    else:
        form = NewEntryForm(initial={'title': entry, 'content': entry_page, 'edit': True})
        form.fields["title"].widget = forms.HiddenInput()
        return render(request, "encyclopedia/new_entry.html", {
            "form": form,
            "existing": True,
            "entry": entry
        })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdown = Markdown()
    entry_content = util.get_entry(entry)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "The requested page was not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown.convert(entry_content),
            "entry_title": entry
        })

def search(request):
    value = request.GET.get('q', '')
    if util.get_entry(value):
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': value}))
    else:
        substring_entries = [entry for entry in util.list_entries() if value.upper() in entry.upper()]
        return render(request, "encyclopedia/index.html", {
            "entries": substring_entries,
            "search": True,
            "value": value
        })

def new_entry(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if util.get_entry(title) is None or form.cleaned_data['edit']:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("entry", kwargs={'entry': title}))
            else:
                return render(request, "encyclopedia/error.html", {
                    "error_message": "The entry already exists.",
                    "form": form,
                    "existing": True,
                    "entry": title
                })
        else:
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/new_entry.html", {
            "form": NewEntryForm(),
            "existing": False
        })

def random_entry(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'entry': random_entry}))

def error_404_view(request, exception):
    return render(request, 'encyclopedia/404.html', {
        "error_message": "The requested page was not found."
    })


