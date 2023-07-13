from django.shortcuts import render

from django.http import JsonResponse

def get_stock_info(request):
    ticker = request.POST.get('ticker')
    # Add your code to fetch stock information using yfinance
    # and return the desired JSON response
    data = {
        'ticker': ticker,
    }
    return JsonResponse(data)

