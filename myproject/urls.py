from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Simple Webserver</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }
            h1 { color: #2c3e50; }
            h3 { color: #34495e; margin: 5px 0; }
            hr { border: 0; border-top: 1px solid #ccc; margin: 20px 0; }
            ul { font-size: 18px; }
            li { margin-bottom: 8px; }
        </style>
    </head>
    <body>
        <h1>Ex 01 - Simple Webserver</h1>
        <hr>
        <h3><b>Student Name:</b> M.D.Pravesika</h3>
        <h3><b>Register Number:</b> 26015761</h3>
        <hr>
        <h2>List of Protocols in TCP/IP Protocol Suite:</h2>
        <ul>
            <li>101_Introduction</li>
            <li>102_FTP</li>
            <li>103_Telnet & SSH</li>
            <li>104_Email & Chat</li>
            <li>105_WWW</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]