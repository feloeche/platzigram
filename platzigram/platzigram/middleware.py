#Platzigram middleware catalog

#Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    #Ensure every user thtat is interecting whith the platform
    #have theyir profile picture
    def __init__(self, get_response):
            self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users:logout')]:
                        return redirect('users:update')

        response = self.get_response(request)


        return response