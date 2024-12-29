from django.shortcuts import render
from django.views.generic import ListView
from .models import Classes, Teachers, Massage, Gallery, ContactMassage
# Create your views here.


class HomePageView(ListView):
    model = Classes
    context_object_name = "classes"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teachers.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get("name")
        email = self.request.POST.get("email")
        select_class = self.request.POST.get("selected")

        getclass = Classes.objects.get(id=int(select_class))

        Massage.objects.create(
            name=name,
            email=email,
            select_class=getclass
        )
        return self.get(request, *args, **kwargs)

def gallery_view(request):
    gallerys = Gallery.objects.all()
    return render(request, "gallery.html", context={"gallerys":gallerys})

class ContactPageViews(ListView):
    model = ContactMassage
    context_object_name = "contacts"
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):
        your_name = self.request.POST.get("your name")
        your_email = self.request.POST.get("your email")
        subject = self.request.POST.get("subject")
        massage = self.request.POST.get("massage")

        ContactMassage.objects.create(
            your_name=your_name,
            your_email=your_email,
            subject=subject,
            massage=massage
        )

        return self.get(request, *args, **kwargs)




