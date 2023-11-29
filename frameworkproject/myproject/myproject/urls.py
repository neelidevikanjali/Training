"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drfcrud/', include('webapp.urls')),
    path('drflogin/', include('restloginapp.urls')),
    path('session/', include('loginsessionapp.urls')),
    path('orm/', include('studentormapp.urls')),
    path('multi/', include('multilevelsession.urls')),
    path('auth/', include('authapp.urls')),
    path('encrypt/', include('encryptapp.urls')),
    path('valid/', include('validationapp.urls')),
  #  path('logging/', include('loggingapp.urls')),
    path('currency/', include('currencyapp.urls')),
    path('age/', include('calculateageapp.urls')),
    path('year/', include('calculateDobapp.urls')),
    path('twodates/', include('twodatesapp.urls')),
    path('qrcode/', include('QRcodeapp.urls')),
    path('barcode/', include('barcodeapp.urls')),
    path('decimal/', include('decimalapp.urls')),
    path('country/', include('countrycurrencyapp.urls')),
    path('bmi/', include('bmiapp.urls')),
    path('timezone/', include('timezoneapp.urls')),
    path('filepath/', include('filepathapp.urls')),
    path('timestamp/', include('timestampapp.urls')),
    path('numto/', include('numberwordsapp.urls')),
    path('otom/', include('otomapp.urls')),
    path('forget/', include('forgetpasswordapp.urls')),

]

