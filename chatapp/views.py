from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def index(request):
    # if request.user.is_authenticated: 
    #     print(request.user,'User already logged in')
    #     return render(request,'admin/dashboard.html')
    # else:
        return render(request,'index.html')

def room(request, room):
    # print(request.GET['username'])
    if 'username' in request.GET.keys():
        username = request.GET.get('username')
        room_details = Room.objects.get(name=room)
        return render(request, 'room.html', {

            'username': username,
            'room': room,
            'room_details': room_details,
        })

    else:
         return redirect('index')

def checkview(request):
    if request.method == 'POST':
        room = request.POST.get('room_name')
        username = request.POST.get('username')

        if Room.objects.filter(name=room).exists():
            print('room alredy exist')
            return redirect('/'+room+'/?username='+username)
        else:
            room_db=Room.objects.create(name=room)
            room_db.save()
            print('new room created successfully')
            return redirect('/'+room+'/?username='+username)

    else:
        return redirect('index')


def send(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_id = request.POST['room_id']
        message = request.POST['message']

        Message.objects.create(
            value=message, user = username, room = room_id
        )

        return HttpResponse('Hii msg send ok')
    else:
        return redirect('index')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    # print(list(messages.values()))
    return JsonResponse({"messages": list(messages.values())})