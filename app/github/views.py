"""Views for external API"""

from django.http import JsonResponse
import requests
import os

def get_github_data(request):
    """View to get user data from GitHub"""

    username = 'KaustubhVaidya404'
    headers = {
        'Authorization': os.environ.get('GITHUB_ACCESS_TOKEN')
    }

    followers_url = f"https://api.github.com/users/{username}/followers"
    following_url = f"https://api.github.com/users/{username}/following"
    repos_url = f"https://api.github.com/users/{username}/repos"

    followers = requests.get(followers_url, headers=headers).json()
    following = requests.get(following_url, headers=headers).json()
    repos = requests.get(repos_url, headers=headers).json()

    data = {
        "followers_count": len(followers),
        "following_count": len(following),
        "repositories": [repo["name"] for repo in repos]
    }

    return JsonResponse(data)
