"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.views.generic import TemplateView
# from rest_framework.schemas import get_schema_view

# api_v1_docs = [
#     path('openapi', get_schema_view(
#         title="Library store",
#         description="Library APIs",
#         version="1.0.0"
#     ), name='openapi-schema'),
#     path('docs/',TemplateView.as_view(
#         template_name='swagger-docs.html',
#         extra_context={'schema_url':'openapi-schema'}
#     ), name='swagger-ui')
# ]
urlpatterns = [
    # path('api/v1/', include(api_v1_docs)),
    path('admin/', admin.site.urls),
    # path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('library.urls')),
  

]