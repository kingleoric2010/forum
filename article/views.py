# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from block.models import Block
from article.models import Article
# Create your views here.


def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    article_infos = Article.objects.filter(block=block).order_by("-id")
    paginator = Paginator(article_infos,3,2)
    page = request.GET.get('page')
    try:
        articl = paginator.page(page)
    except PageNotAnInteger:
        articl = paginator.page(1)
    except EmptyPage :
        articl = paginator.page(paginator.num_pages)
    print (articl)
    print (type(articl))
    print (paginator.page_range)
    #print (articl.page_range)
    #assert False
    return render(request,'article_list.html', {"article_page": articl, "b":block_id,"articles": article_infos })
#    return render(request,'article_list.html',{"articles": article_infos,"b":block_id})

def article_detail(request, article_id):
    article_id = int(article_id)
    article = Article.objects.get(id=article_id)
    print (article)
    return render(request, "article_detail.html", {"article": article})
'''
def article_create(request,block_id):
    block_id = int(block_id)
    if request.method == "GET":
        return render(request, 'article_create.html',{"b": block_id})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article(block_id=block_id, title=form.cleaned_data["title"],owner=request.user, content=form.cleaned_data["title"], status=0)
            article.save()
            return redirect("/article_list/%s" %block_id)
        else:
            return render(request,"article_create.html",{"b":block_id,"form":form})

'''
'''
def article_create(request,block_id):
    block_id = int(block_id)
    if request.method == "GET":
        return render(request, 'article_create.html',{"b": block_id})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block_id = block_id
            article.status = 0
            article.save()
            return redirect("/article_list/%s" %block_id)
        else:
            return render(request,"article_create.html",{"b":block_id,"form":form})
'''


def article_create(request,block_id):
    block_id = int(block_id)
    if request.method == "GET":
        return render(request, 'article_create.html',{"b": block,"error":error})
    else:
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()
        if not title or not content:
            return render(request,"article_create.html",{"b":block_id, "error":"标题和内容不能为空", "title":title, "content": content})
        if len(title) > 100 or not len(content) > 100000:
            return render(request,"article_create.html",{"b":block_id,"error": "标题和内容太长"})
        add_article = Article(block_id=block_id,title=title,owner=request.user, content=content,status=0)
        add_article.save()
        article_infos = Article.objects.filter(block=block_id).order_by("-id")
        return render(request,'article_list.html',{"articles": article_infos,"b":block_id})
        #return redirect(reverse("article.views.article_list", args=[block_id]))
        #return HttpResponseRedirect(reverse("article_list", args=(block_id,)))
        #return redirect(reverse("article_list", args=[block_id]))
        #return redirect(reverse("article_list", kwargs={"block_id": block_id}))
