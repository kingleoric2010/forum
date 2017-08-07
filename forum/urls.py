"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from block.views import block_list
from article.views import article_list, article_detail,article_create
#article_detail, create_article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^block_list/(?P<block_id>\d+)/$', block_list,name='block_id'),
    url(r'^block_list/', block_list),
    url(r'^article_list/(?P<block_id>\d+)/$$', article_list,name='article-list'),
    url(r'^article_create/(?P<block_id>\d+)/$', article_create,name='create_article'),
    url(r'^article_detail/(?P<article_id>\d+)/$', article_detail),
    #url(r'^article_detail/(?P<page_num>\d+)$', article_detail,name="article_detail"),
]
