from django.shortcuts import render

def post_list(request): # Take request, return template
    return render(request, 'blog/post_list.html', {})
