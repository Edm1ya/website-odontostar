from .models import SocialNetwork



def context_dic(request):
    context  = {}
    links = SocialNetwork.objects.all()
    for link in links:
        context[link.key] = link.url
    return context 

