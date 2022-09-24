from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from .models import Staff

def dashboard(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff
    }
    return render(request, 'dashboard/dashboard.html', context)

def payslip(request, pk):
    staff = Staff.objects.get(id=pk)
    template_path = 'dashboard/staff_payslip.html'
    context = {
        'staff': staff
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="payslip.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # return render(request, 'staff/staff_payslip.html', context)

