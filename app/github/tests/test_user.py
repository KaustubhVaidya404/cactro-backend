"""Test to get user data from github"""

from django.test import TestCase
from django.urls import reverse

import os

import requests

URL = reverse('github:getgithubdata')

class GitHubAPITestCase(TestCase):
    def test_get_github_data(self):
        """Test for getting data from github"""
        username = "KaustubhVaidya404"
        token = os.environ.get('GITHUB_ACCESS_TOKEN')

        headers = {
            'Authorization': f'token {token}'
        }

        followers_response = requests.get(f"https://api.github.com/users/{username}/followers", headers=headers)
        following_response = requests.get(f"https://api.github.com/users/{username}/following", headers=headers)
        repos_response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)

        self.assertEqual(followers_response.status_code, 200)
        self.assertEqual(following_response.status_code, 200)
        self.assertEqual(repos_response.status_code, 200)

        followers = followers_response.json()
        following = following_response.json()
        repos = repos_response.json()

        response = self.client.get(URL)

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data['followers_count'], len(followers))
        self.assertEqual(data['following_count'], len(following))
        self.assertEqual(data['repositories'], [repo['name'] for repo in repos])
