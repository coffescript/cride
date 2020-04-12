"""Circles views."""

# Django REST Framework
from rest_framework.decorators import api_view

# Models
from cride.circles.models import Circle

def list_circles(request):
    """List Circles"""
    circles = Circle.object
