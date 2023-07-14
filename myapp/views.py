from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def get_stock_info(request):
    ticker = request.POST.get('ticker')
    stock = yf.Ticker(ticker)
    info = stock.info
    data = {
        'ticker': ticker,
        'info': stock.info,
       
    }
    return JsonResponse(data)
