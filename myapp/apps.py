from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def get_stock_info(request):
    ticker = request.POST.get('ticker')
    # Add your code to fetch stock information using yfinance
    # and return the desired JSON response
    data = {
        'ticker': ticker,
    }
    return JsonResponse(data)

@require_POST
def index(request):
    if request.method == 'POST':
        return get_stock_info(request)
    else:
        return render(request, 'index.html')