from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, name):
    

    page_name = util.get_entry(name)
    if page_name == None:
        return render(request, "encyclopedia/error.html" )

    page_converted = Markdown().convert(page_name)
    
    context = {"content": page_converted}
    title = name
    return render(request, "encyclopedia/title.html",context)
    

def search(request):
    name = request.POST.get("q")
    check_page = util.get_entry(name)
    if check_page == None:
        return render(request, "encyclopedia/error.html")
    check_page_converted = Markdown().convert(check_page)
    return render(request, "encyclopedia/title.html", {"content": check_page_converted})

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    if request.method == "POST":
        page_name = request.POST.get("name")
        page_content = request.POST.get("content")
        util.save_entry(page_name, page_content)
        return HttpResponseRedirect(reverse("index"))

def random_page(request):
    list_pages = util.list_entries()
    page_name = random.choice(list_pages)
    page_main = util.get_entry(page_name)
    page_main_converted = Markdown().convert(page_main)
    context = {"content": page_main_converted}
    return render(request, "encyclopedia/title.html", context)

def edit_title(request):
    if request.method == "GET":
        
        return render(request, "encyclopedia/edittitle.html")

def edit_page(request):
    if request.method == "GET":
        page_name = request.GET.get("name")
        page_entry = util.get_entry(page_name)
        if page_entry == None:
            return render(request, "encyclopedia/error.html")
        context = {"content": page_entry,
        "page_name": page_name}
        return render(request, "encyclopedia/edit.html", context)

    if request.method == "POST":
        content = request.POST.get("content")
        name = request.POST.get("name")
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("index"))
        
        
    




