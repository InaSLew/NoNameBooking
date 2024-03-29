from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages

from .models import Booking
from .forms import BookingForm, DeleteBookingForm, RescheduleBookingForm
from polls.models import Question, Choice

def index(request):
    if request.method == 'GET':
        return render(request, 'index/homepage.html')

def book_table(request):
    contexts = dict()
    
    # Need to replace this one with Form.has_error(field_name, code)
    error_occurence = False
    
    time_slots = ['11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30'
        ,'19:00','19:30','20:00','20:30','21:00']

    if request.method == 'GET':
        contexts['time_slots'] = time_slots
        form = BookingForm()
    
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            print('form is valid')
            new_reservation = form.save()
            print('form is saved')
            messages.add_message(request, messages.SUCCESS, f'Reservation successful! Your BookingID is { new_reservation.booking_id.hex[:5].upper() }. BookingID is needed if you later wish to reschedule/cancel your reservation')
            return HttpResponseRedirect(reverse('index:homepage'))
        else:
            error_occurence = True
            print('form is invalid')
            
            contexts = {
                'form': form,
                'search_query': form.cleaned_data,
                'error_occurence': error_occurence,
                'time_slots': time_slots,
            }

    return render(request, 'index/book_table.html', contexts)

def reschedule_or_cancel(request):
    if request.method == 'GET':
        time_slots = ['11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30'
        ,'19:00','19:30','20:00','20:30','21:00']
        return render(request, 'index/reschedule_or_cancel.html', { 'time_slots': time_slots })

def reschedule_reservation(request):
    if request.method == 'POST':
        form = RescheduleBookingForm(request.POST)

        if form.is_valid():
            print('form is valid')
            print(form.cleaned_data.keys())
            customer_who_request = Booking.objects.get(email=form.cleaned_data['email'])
            customer_who_request.booked_date = form.cleaned_data['booked_date']
            customer_who_request.booked_time = form.cleaned_data['booked_time']
            customer_who_request.save()
            messages.add_message(request, messages.SUCCESS, 'Reservation successfully rescheduled.')
            return HttpResponseRedirect(reverse('index:homepage'))
        else:
            print('form data is invalid')
            time_slots = ['11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30'
        ,'19:00','19:30','20:00','20:30','21:00']
            contexts = {
                'reschedule_form': form,
                'reschedule_form_search_query': form.cleaned_data,
                'reschedule_form_invalid_email': form.has_error('email', code='invalid'),
                'reschedule_form_invalid_booking_id': form.has_error('booking_id', code='invalid'),
                'reschedule_form_invalid_date': form.has_error('booked_date', code='invalid'),
                'reschedule_form_invalid_time': form.has_error('booked_time', code='invalid'),
                'time_slots': time_slots,
            }
            return render(request, 'index/reschedule_or_cancel.html', contexts)


def cancel_reservation(request):
    
    # To cancel a reservation
    if request.method == 'POST':
        
        # get the input from the form and match with the existing reservations
        form = DeleteBookingForm(request.POST)

        if form.is_valid():
            print('form is valid')
            customer_who_request = Booking.objects.get(email=form.cleaned_data['email'])
            print(f'{customer_who_request.get_booking_id()} requested to cancel reservation.')
            customer_who_request.delete()
            print('Reservation deleted.')
            messages.add_message(request, messages.SUCCESS, 'Reservation successfully cancelled. We look forward to seeing you again soon!')
            return HttpResponseRedirect(reverse('index:homepage'))

        else:
            print('form data is invalid')
            contexts = {
                'delete_form': form,
                'delete_form_search_query': form.cleaned_data,
                'delete_form_invalid_email': form.has_error('email', code='invalid'),
                'delete_form_invalid_booking_id': form.has_error('booking_id', code='invalid'),
            }
            return render(request, 'index/reschedule_or_cancel.html', contexts)

def vote(request):
    for key, value in request.POST.items():
        if key != 'csrfmiddlewaretoken':
            question = get_object_or_404(Question, question_text=key)
            try:
                selected_choice = question.choice_set.get(choice_text=value)
            except (KeyError, Choice.DoesNotExist):
                return Http404('Something was wrong')
            else:
                selected_choice.votes += 1
                selected_choice.save()
                print(f'Choice {selected_choice} is saved.')
    
    # If nothing goes wrong inbetween:
    print('Nothing goes wrong inbetween! Woohoo!!')
    messages.add_message(request, messages.SUCCESS, 'Thank you! Your answers are recorded.')
    return HttpResponseRedirect(reverse('index:homepage'))