from .models import Post

def sidebar_data(request): #Side bar to get the top 5 posts
    return {
        'latest_posts': Post.objects.order_by('-date_posted')[:5]
    }
