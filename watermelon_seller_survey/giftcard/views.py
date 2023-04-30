from django.shortcuts import render


def seller_intake_survey(request):
    return render(request, 'form.html')


def seller_intake_survey_list(request):
    return render(request, 'results.html')