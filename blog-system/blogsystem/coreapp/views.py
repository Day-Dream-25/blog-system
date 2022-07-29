from coreapp.forms import ProfileForm, ContactUsForm
from coreapp.models import Profile
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail


class ProfileCreateView(CreateView):
    template_name = 'core.html'
    model = Profile
    form_class = ProfileForm
    success_url = "/login/"


class ProfileUpdate1View(UpdateView):
    model = Profile
    fields = ['gender', 'dob', 'bio', 'link']
    template_name = 'profile.html'
    success_url = '/blogs_list/'

    def get_success_url(self):
        return reverse('blogs_list')


def contact(request):
    form = ContactUsForm(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        message = request.POST.get('message')
        form_data = {
            'name': name,
            'email': email,
            'contact_no': contact_no,
            'message': message,
        }
        message = '''
            From:\n\t\t{}\n
            Message:\n\t\t{}\n
            Email:\n\t\t{}\n
            Phone:\n\t\t{}\n
            '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['contact_no'])
        send_mail('You got a mail!', message, '', ['dharti.pysquad@gmail.com'])

    return render(request, 'contact.html', {'form': form})
