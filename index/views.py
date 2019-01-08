from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.forms import ValidationError
from django.contrib import messages

from .models import Booking, BookingForm
from polls.models import Question, Choice

def index(request):

        # Just so I can see what's going on through the terminal
        # for key, value in request.POST.items():
        #     print(f'{key}:{value}(Data type: {type(value)})')

    
    if request.method == 'GET':
        return render(request, 'index/homepage.html')

def book_table(request):
    contexts = dict()
    error_occurence = False
    time_slots = ['11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30'
        ,'19:00','19:30','20:00','20:30','21:00']

    if request.method == 'GET':
        contexts['time_slots'] = time_slots
        form = BookingForm()
    
    if request.method == 'POST':
        form = BookingForm(request.POST)

        '''
            1. [DONEish?]Still need to sanitize the data
            2. Also need to check if the chosen date or time has been booked up or too ahead.
            3. [DONE]Display a success message modal if booking was successful.
        '''
        if form.is_valid():
            print('form is valid')
            new_reservation = form.save()
            print('form is saved')
            messages.add_message(request, messages.SUCCESS, 'Reservation successful! We\'ve sent you a confirmation email.')
            return HttpResponseRedirect(reverse('index:homepage'))
        else:
            error_occurence = True
            print('form is invalid')
            print(form.errors.as_data())
            
            contexts = {
                'form': form,
                'search_query': form.cleaned_data,
                'error_occurence': error_occurence,
                'time_slots': time_slots,
            }

    return render(request, 'index/book_table.html', contexts)

def change_or_cancel(request):
    if request.method == 'GET':
        return render(request, 'index/change_or_cancel.html')
    
    # To cancel a reservation
    if request.method == 'DELETE':
        pass

    # To reschedule to another date or time:
    if request.method == 'PATCH':
        pass

def vote(request):
    for key, value in request.POST.items():
        # print(f'{key}:{value}(Data type: {type(value)})')
        if key != 'csrfmiddlewaretoken':
            print(key)
            question = get_object_or_404(Question, question_text=key)
            print(f'Question {key} is created')
            try:
                selected_choice = question.choice_set.get(choice_text=value)
            except (KeyError, Choice.DoesNotExist):
                return HttpResponse('Something was wrong')
            else:
                selected_choice.votes += 1
                selected_choice.save()
                print(f'Choice {selected_choice} is saved.')
    
    # If nothing goes wrong inbetween:
    print('Nothing goes wrong inbetween! Woohoo!!')
    messages.add_message(request, messages.SUCCESS, 'Thank you! Your answers are recorded.')
    return HttpResponseRedirect(reverse('index:homepage'))
