# Sobre o Comparador de moedas

O Comparador de moedas é um programa que otimiza a pesquisa de preços de criptoativos. Sua principal função é fornecer dados de possíveis ativos para fazer arbitragem ou até mesmo - para auxiliar em uma melhor oportunidade de preços de compra e venda.


## Pré-requisitos
Python 3.11.4

## Instalação
Instale a biblioteca CCXT

```bash
pip install ccxt
```

## Como usar?
O Comparador de moedas está na sua primeira fase, por enquanto, você simplesmente vai executar o código que está em célula única. Ele está configurado para fazer a pesquisa entre a Latoken Exchange e a Probit Exchange. Mas em breve, adicionaremos outras (outras +50)!.
O Comparador de moedas vai listar todos os pares de moedas em "/USDT" que estão em negociação nas exchanges selecionadas. 
<br>

<img width="795" alt="selecaoDeMoedas" src="https://github.com/MgnMagno/comparador_de_moedas/assets/140118389/0eb4626c-e426-4be1-8282-1d88d076b586">
<br><br>

Detalhe: para facilitar sua vida, o Comparador de moedas imprimirá os pares comuns já com o link personalizado de cada corretora indicando a diferença percentual entre elas.
neste exemplo, verificamos o spread da criptomoeda Algorand
<img width="444" alt="selecaoDeMoedasAlgorand" src="https://github.com/MgnMagno/comparador_de_moedas/assets/140118389/c3bc2d63-1579-4bf4-9578-8f253ac74d65">
<br><br>

Agora você pode abrir a negociação diretamente na corretora correspondente. A exemplo, abrimos esses links do Comparador, para analizar o ativo Algorand nas corretoras selecionadas:

Latoken

<img width="960" alt="algorandNaLatoken" src="https://github.com/MgnMagno/comparador_de_moedas/assets/140118389/e5abae11-1959-4778-8254-daf7a905eba6">

<br><br>

Probit

<img width="960" alt="algorandNaProbit" src="https://github.com/MgnMagno/comparador_de_moedas/assets/140118389/73e79a36-45d4-4818-b834-2669c9a13b58">

<br><br>

Você também pode modfificar a diferença percentual de acordo com a sua estratégia de trade.
<br>

<img width="710" alt="Captura de tela 2023-09-16 204037" src="https://github.com/MgnMagno/comparador_de_moedas/assets/140118389/6ea9137e-b1fb-4149-98df-9df9372fe503">

<br><br>


## Contribuições

Solicitações pull requests são bem-vindas!

## License

[MIT](https://choosealicense.com/licenses/mit/)
