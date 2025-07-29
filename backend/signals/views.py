from django.shortcuts import render

def file_viewer_page(request):
    """Renders the page for the client-side file viewer."""
    return render(request, 'signals/display.html')
