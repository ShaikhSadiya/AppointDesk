
from django.shortcuts import render, redirect
from .form import AppointmentForm
from  .models import Appointment
from django.contrib import messages



def add_appointment(request):

    form = AppointmentForm
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(
                request,
                'Appointment Added Successfully'
            )

            #return HttpResponse("Booked")
            return redirect('/appointments/')
    template_name='appointment/add_appointment.html'
    context = {'form':form}
    return render(request, template_name, context)


def appointments(request):
    if not request.GET:
         appointment = Appointment.objects.filter(user=request.user)
         template_name = 'appointment/appointments.html'
         context = {'appointment': appointment}
         return render(request, template_name, context)


    elif request.GET:
        search = request.GET.get('search')
        appointment = Appointment.objects.filter(user=request.user, customer_name__contains=search)
        template_name = 'appointment/appointments.html'
        context = {'appointment': appointment}
        return render(request, template_name, context)









def delete_view(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    messages.success(
        request,
        'Appointment Deleted Successfully'
    )

    return redirect('/appointments/')

def update_view(request, id):
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointments/')

    template_name = 'appointment/add_appointment.html'
    context = {'form': form}
    return render(request, template_name, context)


def info_view(request,id):
    appointment = Appointment.objects.get(id=id)
    template_name ='appointment/appointment_info.html'
    context = {'appointment':appointment}
    return render(request, template_name, context)

