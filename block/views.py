from django.shortcuts import render
from block.models import Block
from django.template import RequestContext

# Create your views here.


def block_list(request):
    #block_infos = Block.objects.all().order_by("-id")
    #block_infos = Block.objects.filter(status__lt=0).order_by("-id")
    block_infos = Block.objects.all().order_by("-id")
    return render(request,'block_list.html',{"blocks": block_infos})
