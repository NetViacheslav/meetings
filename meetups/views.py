from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'locations': 'Ostrava',
            'slug': 'first-meetups'
        },
        {
            'title': 'A Second Meetup',
            'locations': 'Poruba',
            'slug': 'second-meetups'
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
