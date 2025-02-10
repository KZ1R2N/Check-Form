# formapp/views.py
from django.shortcuts import render, redirect
from .forms import FormDataForm
from .models import FormData

def form_view(request):
    form_submitted = False
    form = FormDataForm()

    if request.method == 'POST':
        form = FormDataForm(request.POST)

        if form.is_valid():
            form_data = form.save(commit=False)  # Save form data without committing it yet

            # Only commit to the database if the checkbox is checked for a field
            if not form_data.is_number_checked:
                form_data.number_field = None
            if not form_data.is_text_checked:
                form_data.text_field = None
            if not form_data.is_date_checked:
                form_data.date_field = None

            form_data.save()  # Commit the data to the database

            # Redirect to a new page showing the submitted data
            return redirect('show_data')  # Redirect to the 'show_data' page

    return render(request, 'form/form.html', {
        'form': form,
        'form_submitted': form_submitted,
    })

def show_data(request):
    # Retrieve all the data stored in the database
    form_data = FormData.objects.all()
    
    return render(request, 'form/show_data.html', {
        'form_data': form_data,  # Pass the retrieved data to the template
    })
