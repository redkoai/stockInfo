from django.shortcuts import render
from django.http import JsonResponse

def get_stock_info(request):
    ticker = request.GET.get('ticker')
    stock = yf.Ticker(ticker)
    info = stock.info
    data = {
        'ticker': ticker,
        'name': info,
    }
    return JsonResponse(info)
