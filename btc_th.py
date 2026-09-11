import requests 
def get_ticker()-> dict :
    response = requests.get('https://api.india.delta.exchange/v2/tickers?symbols=BTC-USD')
    print(response.text)
    print(response.status_code)
    return response.json()
result=get_ticker()
print(result)    

    
    