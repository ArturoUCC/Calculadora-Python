from zeep import Client

wsdl_url = 'http://127.0.0.1:8000/?wsdl'

try:
    client = Client(wsdl_url)

    print('Cliente conectado al WSDL en', wsdl_url)

    resultado_suma = client.service.sumar(4, 3)
    print('Resultado de la suma:', resultado_suma)

    resultado_resta = client.service.restar(4, 3)
    print('Resultado de la resta:', resultado_resta)

    resultado_multiplicar = client.service.multiplicar(4, 3)
    print('Resultado de la multiplicación:', resultado_multiplicar)

    resultado_dividir = client.service.dividir(4, 3)
    print('Resultado de la división:', resultado_dividir)

except Exception as e:
    print('Error al conectar con el WSDL:', e)
    exit(1)