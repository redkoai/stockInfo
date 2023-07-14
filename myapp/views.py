from django.shortcuts import render
from django.http import JsonResponse
import yfinance as yf

def get_stock_info(request):
    ticker = request.GET.get('ticker')
    stock = yf.Ticker(ticker)
    info = stock.info
    data = {
        'ticker': ticker,
        'name': info['name'],
        'price': info['current'],
        'change': info['change'],
        'percent_change': info['percent_change'],
    }
    return JsonResponse(data, safe=False)
