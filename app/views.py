from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reminder , Coding_profile_detail

def reminder_page(request):
    profile_data = Coding_profile_detail.objects.all().first()
    return render(request, 'reminders/index.html', {'profile_data': profile_data})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import ContactSubmission

@csrf_exempt
@require_POST
def contact_submit_api(request):
    try:
        data = json.loads(request.body)
        
        # Validate data
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return JsonResponse({
                'success': False,
                'error': 'All fields are required'
            }, status=400)
        
        # Save to database
        submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.',
            'data': {
                'id': submission.id,
                'name': submission.name,
                'created_at': submission.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)