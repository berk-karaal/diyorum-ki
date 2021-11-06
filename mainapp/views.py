from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import Post

post_per_page = 10

# homepage view
def home(request):
    posts = Post.objects.order_by("-date_created")
    paginator = Paginator(posts, post_per_page)
    page_obj = paginator.get_page(request.GET.get("sayfa"))

    return render(
        request,
        "mainapp/home.html",
        {"page_obj": page_obj, "home_page": "active", "best_posts_page": ""},
    )


# "best posts page" view
def best_posts(request):
    posts = Post.objects.order_by("-like_count", "-date_created")
    paginator = Paginator(posts, post_per_page)
    page_obj = paginator.get_page(request.GET.get("sayfa"))

    return render(
        request,
        "mainapp/home.html",
        {"page_obj": page_obj, "home_page": "", "best_posts_page": "active"},
    )


# liking a post
def like(request, id):
    if request.method == "POST":
        try:
            post = Post.objects.get(id=id)
            post.like_count += 1
            post.save()
            # return only like_count because we use HTMX to update text on page
            return HttpResponse(str(post.like_count))
        except Post.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)


from django.contrib import messages
from django.utils.safestring import mark_safe
from .forms import new_post_form


# create new post page
def new_post(request):
    if request.method == "POST":
        form = new_post_form(request.POST)

        if form.is_valid():
            if not contains_bad_word(str(form.cleaned_data["content"])):
                form.save()
                return redirect("home")

            messages.warning(
                request, mark_safe("Araya garip kelimeler mi karıştı acaba? &#9940;")
            )
    else:
        form = new_post_form()
    return render(request, "mainapp/new_post.html", {"form": form})


# check content for blacklisted words
def contains_bad_word(content: str) -> bool:
    content = content.lower().split(" ")

    try:
        with open("mainapp/wordBlacklist.txt", "r", encoding="utf-8") as file:
            bad_words_list = file.read().splitlines()
            contains = any([word in bad_words_list for word in content])
            return contains
    except:
        # allow (don't check) if there is problem
        return False
