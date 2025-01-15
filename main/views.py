from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .utils import CVGenerator
import json


def landing_page(request):
    return render(request, 'main/landingpage.html')


@login_required
def dashboard_view(request):
    # Pass any required context for the dashboard
    return render(request, 'main/dashboard.html')

@require_http_methods(["POST"])
def preview_cv(request):
    """Generate CV preview"""
    try:
        cv_generator = CVGenerator(request.POST)
        
        template_choice = request.POST.get('template')
        if template_choice == '1':
            preview = cv_generator.generate_professional_preview()
        elif template_choice == '2':
            preview = cv_generator.generate_modern_preview()
        else:
            preview = cv_generator.generate_creative_preview()
            
        return JsonResponse({
            'status': 'success',
            'preview': preview,
            'message': 'Preview generated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@require_http_methods(["POST"])
def download_cv(request):
    """Download CV in specified format"""
    try:
        format_type = request.GET.get('format', 'pdf')
        cv_generator = CVGenerator(request.POST)
        
        if format_type == 'pdf':
            buffer = cv_generator.generate_pdf_document()
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
        else:
            buffer = cv_generator.generate_word_document()
            response = HttpResponse(buffer.getvalue(), 
                                 content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="cv.docx"'
            
        return response
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)