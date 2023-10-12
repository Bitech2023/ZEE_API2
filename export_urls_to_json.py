import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")
from django.conf import settings
from django.urls import URLPattern, URLResolver
from django.urls import get_resolver
import json
import django
django.setup()

# Import your views
from location.views import GeocodeView, LocationListCreateView, LocationDetailView


def get_supported_methods(view):
    # Retrieve the supported HTTP methods for a view
    supported_methods = []
    if hasattr(view, 'http_method_names'):
        supported_methods = [method.lower() for method in view.http_method_names]
    return supported_methods

def serialize_url_patterns(url_patterns, urlpatterns_data):

    serialized_patterns = []

    def process_patterns(patterns, data):
        for pattern, pattern_data in zip(patterns, data):
            if isinstance(pattern, URLPattern):
                url_data = {
                    'name': pattern.name,
                    'pattern': str(pattern.pattern),
                    'view_name': pattern_data['name'] ,
                    'methods': get_supported_methods(data),
                    'permissions': pattern_data.get('permissions', []),
                    
                }
                serialized_patterns.append(url_data)
                print(f"Added URL: {url_data['name']} - {url_data['pattern']}")
            elif isinstance(pattern, URLResolver):
                print(f"Processing URLResolver: {pattern.url_patterns}")
                process_patterns(pattern.url_patterns, data)

    process_patterns(url_patterns, urlpatterns_data)
    return serialized_patterns

# Define the data associated with each URL pattern
urlpatterns_data = [
    {'view': GeocodeView.as_view(), 'name': 'geocode'},
    {'view': LocationListCreateView.as_view(), 'name': 'location-list-create'},
    {'view': LocationDetailView.as_view(), 'name': 'location-detail'},
]

url_resolver = get_resolver()
url_patterns = url_resolver.url_patterns
url_list = serialize_url_patterns(url_patterns, urlpatterns_data)

json_data = json.dumps(url_list, indent=4)
with open('conb.json', 'w') as json_file:
    json_file.write(json_data)

print(f"Total URLs exported: {len(url_list)}")
