# Antes de rodar o codigo, certifique-se que instalou o "pip install ccxt"
import ccxt

exchanges = ['latoken', 'probit']

pares_comuns = []
print(f"\n\nIniciando a verificação entre as exchanges {exchanges[0]} e {exchanges[1]} ... \n\n")
for exchange in exchanges:
    try:
        exchange_instance = getattr(ccxt, exchange)()

        markets = exchange_instance.load_markets()

        symbols = list(markets.keys())

        if len(pares_comuns) == 0:
            pares_comuns = symbols
        else:
            pares_comuns = list(set(pares_comuns) & set(symbols))

    except Exception as e:
        print(f"Erro ao obter pares de moedas da exchange {exchange}: {e}")

for pair in sorted(pares_comuns):
    if pair.split('/')[1] == 'USDT':
        prices = {}
        links = {}
        for exchange in exchanges:
            try:
                exchange_instance = getattr(ccxt, exchange)()

                price = exchange_instance.fetch_ticker(pair)['last']

                prices[exchange] = "{:.11f}".format(price)
                
                if exchange == 'latoken':
                    links[exchange] = f"https://{exchange}.com/exchange/{pair.replace('/', '_')}"
                elif exchange == 'probit':
                    links[exchange] = f"https://{exchange}.com/app/exchange/{pair.replace('/', '-')}"
                    
            except Exception as e:
                print(f"Erro ao obter preço do par de moedas {pair} na exchange {exchange}: {e}")

        diff_percentage = (float(prices[exchanges[0]]) - float(prices[exchanges[1]])) / float(prices[exchanges[1]]) * 100

        # AQUI VOCE PODE FILTRAR O VALOR DA DIFERENÇA, POR PADRÃO ESTÁ EM MAIS DE 11% 
        if abs(diff_percentage) > 11:
            print(f"\nPar de moedas: {pair}")
            for exchange in exchanges:
                print(f"{exchange.upper()}: {prices[exchange]} - {links[exchange]}")
            print(f"Diferença percentual: {diff_percentage:.2f}%")




print("\n")
print("fim da lista de pares, obrigado por utilizar nosso programa!")
print("\n\n\n\nCreated by Magno Barbosa")
print("\n\n\n")
