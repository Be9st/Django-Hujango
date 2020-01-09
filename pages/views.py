from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    names = ['Sasha', 'Pasha', 'SirGay', 'VsyoYasno']
    return render(request, 'pages/base_block.html', context={'names':names})