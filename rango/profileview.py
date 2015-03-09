
def profile(request, username):
    context_dict={}
    u = User.objects.get(username = username)
    if request.method == 'POST':
        
        profile_form = UserProfileForm(data = request.POST)
        
        # If the two forms are valid...
        if profile_form.is_valid():
            
            userProfile = UserProfile.objects.get(user = u)
            userProfile.picture = request.FILES['picture']
            userProfile.save()
            
        return HttpResponseRedirect('/rango/profile/' + username)
    
    else:
        cat_list = get_category_list()
        context_dict = {'cat_list': cat_list}
        
        try:
            up = UserProfile.objects.get(user=u)
        except:
            up = None
            
        context_dict['visitedUser'] = u
        context_dict['userprofile'] = up
        context_dict['profile_form'] = UserProfileForm()
        
    return render(request, 'rango/profile.html', context_dict)
