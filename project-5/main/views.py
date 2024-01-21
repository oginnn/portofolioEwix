from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from .models import Certificate, ReportingResult
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you, I will contact you soon')
            return redirect('/')
    else:
        form = ContactForm()

    return render(request, 'main/index.html', {'form': form})

class index_view(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reporting_results = ReportingResult.objects.filter(is_active=True).order_by('-date')[:6]

        context['reporting_results'] = reporting_results

        return context
    
class certificates_view(ListView):
    model = Certificate
    template_name = 'main/certificate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = Certificate.objects.filter(is_active=True)

        context['certificates'] = certificates

        return context
    
class reporting_view(ListView):
    model = ReportingResult
    template_name = 'main/reporting.html'
    context_object_name = 'reporting'
    paginate_by = 10

    def get_queryset(self):
        return ReportingResult.objects.filter(is_active=True).order_by('-date')
    
class reporting_result_view(DetailView):
    model = ReportingResult
    template_name = "main/reporting-detail.html"