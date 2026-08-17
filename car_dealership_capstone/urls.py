from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from frontend.views import login_view, logout_view, dealers_view, dealers_by_state_view, dealer_details_view, post_review_view, submit_review_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='About.html')),
    path('contact/', TemplateView.as_view(template_name='Contact.html')),
    path('djangoapp/login/', login_view, name='login'),
    path('djangoapp/logout/', logout_view, name='logout'),
    path('djangoapp/dealers/', dealers_view, name='dealers'),
    path('djangoapp/dealers/state/<str:state>/', dealers_by_state_view, name='dealers_by_state'),
    path('djangoapp/dealer/<int:dealer_id>/', dealer_details_view, name='dealer_details'),
    path('djangoapp/review/<int:dealer_id>/', post_review_view, name='post_review'),
    path('djangoapp/submit_review/', submit_review_view, name='submit_review'),
]
