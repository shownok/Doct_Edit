from django.shortcuts import render, redirect
from . models import document, documentRoom
from .forms import documentsForm
from django.contrib import messages

from django.http import HttpResponseForbidden
from lock_tokens.exceptions import AlreadyLockedError, UnlockForbiddenError
from lock_tokens.sessions import check_for_session, lock_for_session, unlock_for_session


def home(request):
    return render(request, 'welcome.html')


def docRoom(request):
    room = documentRoom.objects.all()
    context = {
        'room': room
    }
    return render(request, 'index.html', context)


def docRoomContent(request, id):
    roomContent = document.objects.all().filter(docRoom=id)

    context = {
        'roomContent': roomContent
    }
    return render(request, 'roomContent.html', context)


def viewDoc(request, pk):
    docFile = document.objects.get(pk=pk)
    return render(request, 'singlePage.html', {'docFile': docFile})


def createDoc(request):
    form = documentsForm()
    if request.method == "POST":
        form = documentsForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            messages.success(request, 'Successfully Saved')
            return redirect(docRoom)
    else:
        form = documentsForm()

    return render(request, 'form.html', {'form': form})


def editDoc(request, id):
    items= document.objects.get(pk=id)
    form = documentsForm(instance=items)
    try:
        lock_for_session(items, request.session)
        if request.method == "POST":
            form = documentsForm(request.POST, instance=items)
            form.save(commit=True)
            messages.success(request, 'Updated Successfully')
            unlock_for_session(items, request.session)
            return redirect(docRoom)
    except AlreadyLockedError:
        return HttpResponseForbidden("This resource is locked, sorry !")

    return render(request, 'editDoc.html', {'form': form})
