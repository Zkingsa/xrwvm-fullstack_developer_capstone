from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'user': user.username})
        return JsonResponse({'message': 'Invalid credentials'}, status=401)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

def dealers_view(request):
    dealers = [
        {"id": 1, "name": "CarMax", "city": "Los Angeles", "address": "123 Main St", "zip": "90001", "state": "CA"},
        {"id": 2, "name": "AutoNation", "city": "Houston", "address": "456 Oak Ave", "zip": "77001", "state": "TX"},
        {"id": 3, "name": "Carvana", "city": "Phoenix", "address": "789 Pine Rd", "zip": "85001", "state": "AZ"},
        {"id": 4, "name": "Enterprise", "city": "San Francisco", "address": "321 Elm St", "zip": "94101", "state": "CA"},
        {"id": 5, "name": "Hertz", "city": "Wichita", "address": "654 Maple Dr", "zip": "67201", "state": "KS"}
    ]
    return render(request, 'dealers.html', {'dealers': dealers, 'user': request.user})

def dealers_by_state_view(request, state):
    dealers = [
        {"id": 1, "name": "CarMax", "city": "Los Angeles", "address": "123 Main St", "zip": "90001", "state": "CA"},
        {"id": 2, "name": "AutoNation", "city": "Houston", "address": "456 Oak Ave", "zip": "77001", "state": "TX"},
        {"id": 3, "name": "Carvana", "city": "Phoenix", "address": "789 Pine Rd", "zip": "85001", "state": "AZ"},
        {"id": 4, "name": "Enterprise", "city": "San Francisco", "address": "321 Elm St", "zip": "94101", "state": "CA"},
        {"id": 5, "name": "Hertz", "city": "Wichita", "address": "654 Maple Dr", "zip": "67201", "state": "KS"}
    ]
    filtered_dealers = [d for d in dealers if d['state'] == state]
    return render(request, 'dealers.html', {'dealers': filtered_dealers, 'user': request.user})

def dealer_details_view(request, dealer_id):
    dealers = [
        {"id": 1, "name": "CarMax", "city": "Los Angeles", "address": "123 Main St", "zip": "90001", "state": "CA", "reviews": [{"user": "John", "text": "Great service!"}]},
        {"id": 2, "name": "AutoNation", "city": "Houston", "address": "456 Oak Ave", "zip": "77001", "state": "TX", "reviews": []},
        {"id": 3, "name": "Carvana", "city": "Phoenix", "address": "789 Pine Rd", "zip": "85001", "state": "AZ", "reviews": []},
        {"id": 4, "name": "Enterprise", "city": "San Francisco", "address": "321 Elm St", "zip": "94101", "state": "CA", "reviews": []},
        {"id": 5, "name": "Hertz", "city": "Wichita", "address": "654 Maple Dr", "zip": "67201", "state": "KS", "reviews": []}
    ]
    dealer = next((d for d in dealers if d['id'] == dealer_id), None)
    return render(request, 'dealer_details.html', {'dealer': dealer, 'user': request.user})

def post_review_view(request, dealer_id):
    return render(request, 'post_review.html', {'dealer_id': dealer_id, 'user': request.user})

@csrf_exempt
def submit_review_view(request):
    if request.method == 'POST':
        dealer_id = request.POST.get('dealer_id')
        review_text = request.POST.get('review')
        return render(request, 'review_submitted.html', {'dealer_id': dealer_id, 'review': review_text, 'user': request.user})
