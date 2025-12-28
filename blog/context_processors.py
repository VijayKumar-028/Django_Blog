from .models import Post

def sidebar_data(request):
    return {
        'latest_posts': Post.objects.order_by('-date_posted')[:5]
    }
