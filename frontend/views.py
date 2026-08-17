from django.shortcuts import render, redirect
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
        {"id": 1, "name": "CarMax", "state": "CA", "address": "123 Main St"},
        {"id": 2, "name": "AutoNation", "state": "TX", "address": "456 Oak Ave"},
        {"id": 3, "name": "Carvana", "state": "AZ", "address": "789 Pine Rd"},
        {"id": 4, "name": "Enterprise", "state": "CA", "address": "321 Elm St"},
        {"id": 5, "name": "Hertz", "state": "KS", "address": "654 Maple Dr"}
    ]
    return render(request, 'dealers.html', {'dealers': dealers, 'user': request.user})

def dealers_by_state_view(request, state):
    dealers = [
        {"id": 1, "name": "CarMax", "state": "CA", "address": "123 Main St"},
        {"id": 2, "name": "AutoNation", "state": "TX", "address": "456 Oak Ave"},
        {"id": 3, "name": "Carvana", "state": "AZ", "address": "789 Pine Rd"},
        {"id": 4, "name": "Enterprise", "state": "CA", "address": "321 Elm St"},
        {"id": 5, "name": "Hertz", "state": "KS", "address": "654 Maple Dr"}
    ]
    filtered_dealers = [d for d in dealers if d['state'] == state]
    return render(request, 'dealers.html', {'dealers': filtered_dealers, 'user': request.user})

def dealer_details_view(request, dealer_id):
    dealers = [
        {"id": 1, "name": "CarMax", "state": "CA", "address": "123 Main St", "reviews": [{"user": "John", "text": "Great service!"}]},
        {"id": 2, "name": "AutoNation", "state": "TX", "address": "456 Oak Ave", "reviews": []},
        {"id": 3, "name": "Carvana", "state": "AZ", "address": "789 Pine Rd", "reviews": []},
        {"id": 4, "name": "Enterprise", "state": "CA", "address": "321 Elm St", "reviews": []},
        {"id": 5, "name": "Hertz", "state": "KS", "address": "654 Maple Dr", "reviews": []}
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
        # Simulate success
        return render(request, 'review_submitted.html', {'dealer_id': dealer_id, 'review': review_text, 'user': request.user})
