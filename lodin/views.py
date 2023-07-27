from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
@staff_member_required
def search_users(request):
    query = request.GET.get('q')
    if query:
        # Perform the user search based on the query
        # For example, you can search by username or email
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()

    context = {'users': users}
    return render(request, 'search_results.html', context)

