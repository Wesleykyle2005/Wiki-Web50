"""Views for the encyclopedia app."""

import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from markdown2 import Markdown
from . import util


class NewEntryForm(forms.Form):
    """Form for creating or editing encyclopedia entries."""

    title = forms.CharField(
        label="title",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control col-md-8 col-lg-8",
                "placeholder": "Title of the entry",
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control col-md-8 col-lg-8",
                "placeholder": "Content of the entry",
            }
        )
    )
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)


def edit(request, entry_title):
    """View to edit an existing entry."""
    entry_page = util.get_entry(entry_title)
    if entry_page is None:
        return render(
            request,
            "encyclopedia/error.html",
            {"error_message": "The requested page was not found."},
        )
    form = NewEntryForm(
        initial={"title": entry_title, "content": entry_page, "edit": True}
    )
    form.fields["title"].widget = forms.HiddenInput()
    return render(
        request,
        "encyclopedia/new_entry.html",
        {"form": form, "existing": True, "entry": entry_title},
    )


def index(request):
    """View to display the index page with all entries."""
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, entry_title):
    """View to display a specific entry."""
    markdown = Markdown(extras=["fenced-code-blocks"])
    entry_content = util.get_entry(entry_title)
    if entry_content is None:
        return render(
            request,
            "encyclopedia/error.html",
            {"error_message": "The requested page was not found."},
        )
    return render(
        request,
        "encyclopedia/entry.html",
        {"entry": markdown.convert(entry_content), "entry_title": entry_title},
    )


def search(request):
    """View to handle search queries."""
    value = request.GET.get("q", "")
    if util.get_entry(value):
        return HttpResponseRedirect(reverse("entry", kwargs={"entry_title": value}))
    substring_entries = [e for e in util.list_entries() if value.upper() in e.upper()]
    return render(
        request,
        "encyclopedia/index.html",
        {"entries": substring_entries, "search": True, "value": value},
    )


def new_entry(request):
    """View to create a new entry or edit an existing one."""
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is None or form.cleaned_data["edit"]:
                util.save_entry(title, content)
                return HttpResponseRedirect(
                    reverse("entry", kwargs={"entry_title": title})
                )
            return render(
                request,
                "encyclopedia/error.html",
                {
                    "error_message": "The entry already exists.",
                    "form": form,
                    "existing": True,
                    "entry": title,
                },
            )
        return render(request, "encyclopedia/new_entry.html", {"form": form})
    return render(
        request,
        "encyclopedia/new_entry.html",
        {"form": NewEntryForm(), "existing": False},
    )


def random_entry(_request):
    """View to redirect to a random entry."""
    entries = util.list_entries()
    random_choice = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={"entry_title": random_choice}))


def error_404_view(_request, _exception):
    """Custom 404 error view."""
    return render(
        _request,
        "encyclopedia/404.html",
        {"error_message": "The requested page was not found."},
    )
