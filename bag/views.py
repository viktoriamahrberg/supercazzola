from django.shortcuts import render

def view_bag(request):
    """ View to return shopping bag page """

    return render(request, 'bag/bag.html')
