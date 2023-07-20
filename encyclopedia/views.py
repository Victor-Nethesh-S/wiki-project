from django.shortcuts import render, redirect
from django.http import HttpResponse
import markdown
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def get_title(request, title):
    content = util.get_entry(title)
    if not content is None:
        return render(request, "encyclopedia/title.html", {
            'title': title,
            'body': markdown.markdown(content)
        })
    list = util.filename_with_substring(title)
    if list:
        return render(request, "encyclopedia/index.html", {
            "entries": list
        })

    return render(request, "encyclopedia/title.html", {
        'title': title,
        'body': "Requested page was not found"
    })


def form(request):
    if request.method == 'GET':
        title = request.GET.get('q', '')
        if title:
            return redirect('get_title', title=title)
    return HttpResponse("No title specified")


def create(request):
    if request.method == 'GET':
        title = request.GET.get('title', '')
        markdown = request.GET.get('markdown', '')
        list = util.list_entries()
        if title == '':
            return render(request, "encyclopedia/create.html")
        if title in list:
            return HttpResponse("title not valid")
        util.save_entry(title, markdown)
        return redirect('get_title', title=title)

    return render(request, "encyclopedia/create.html")


def edit(request):
    if request.method == 'GET':
        title = request.GET.get('q', '')
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title': title,
            'content': content
        })
    elif request.method == 'POST':
        title = request.POST.get('t', '')
        content = request.POST.get('c', '')
        util.save_entry(title, content)
        return redirect('get_title', title=title)

    # return render(request, 'encyclopedia/edit.html' {})


def random_title(request):
    list = util.list_entries()
    title = random.choice(list)
    return redirect('get_title', title=title)
