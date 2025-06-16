from django.shortcuts import render, redirect

def select_language(request):
    if request.method == 'POST':
        selected_language = request.POST.get('language')
        if selected_language in ['uz', 'ru', 'en']:
            return redirect(f'/{selected_language}/')
    return render(request, 'language_selector/select_language.html')
