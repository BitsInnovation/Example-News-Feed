from django.shortcuts import render

from django.contrib.auth.models import User
from feed.models import UserProfile

def user_feed(request, username):
    # Retrieve the user from the database since we aren't doing any kind of authentication.
    user = User.objects.get(username=username)

    # Retrieve all the posts from the user's this person is following.
    posts = map(lambda x: x.user.post_set.all(), UserProfile.objects.get(user=user).following.all())

    # Append user's posts as well.
    posts.append(user.post_set.all())

    # The result is a list of lists, this line will combine the arrays into one list.
    posts = [item for sublist in posts for item in sublist]

    # This will sort the array of posts by date posted DESCENDING
    posts.sort(key=lambda x: x.date, reverse=True)

    # This will render the posts.
    return render(request, 'feed/index.html', {'posts': posts})
