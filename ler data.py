from datetime import datetime


# Função para converter números em texto
def numero_por_extenso(num):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas_maiores = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    if 0 <= num < 10:
        return unidades[num]
    elif 10 <= num < 20:
        return dezenas[num - 10]
    elif 20 <= num < 100:
        d, u = divmod(num, 10)
        return dezenas_maiores[d - 2] + ('' if u == 0 else ' e ' + unidades[u])
    elif 100 <= num < 1000:
        c, rem = divmod(num, 100)
        if rem == 0:
            return unidades[c] + ' cento' if c > 1 else 'cem'
        else:
            return (unidades[c] if c > 1 else '') + ' cento e ' + numero_por_extenso(rem)
    elif 1000 <= num < 1000000:
        milhar, rem = divmod(num, 1000)
        if rem == 0:
            return (numero_por_extenso(milhar) if milhar > 1 else '') + ' mil'
        else:
            return (numero_por_extenso(milhar) if milhar > 1 else '') + ' mil e ' + numero_por_extenso(rem)
    else:
        return 'Número fora do intervalo'


# Função para converter a data em formato extenso
def data_por_extenso(data_str):
    try:
        # Converte a string para um objeto datetime
        data = datetime.strptime(data_str, '%d/%m/%Y')

        # Dicionário para os meses
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

        # Obtendo o dia, mês e ano
        dia = int(data.strftime('%d'))
        mes = int(data.strftime('%m'))
        ano = int(data.strftime('%Y'))

        # Convertendo o dia e ano para texto
        dia_extenso = numero_por_extenso(dia)
        mes_extenso = meses[mes - 1]
        ano_extenso = numero_por_extenso(ano)

        return f'{dia_extenso} de {mes_extenso} de {ano_extenso}'
    except ValueError:
        return 'Data inválida. Por favor, insira a data no formato DD/MM/AAAA.'

def Converter_data():
    data_str = input('Digite uma data no formato DD/MM/AAAA: ')
    resultado = data_por_extenso(data_str)
    print(resultado)

def Listar_datas():
        print("""janeiro
        fevereiro
        março
        abril
        maio
        junho
        julho
        agosto
        setembro
        outubro
        novembro
        dezembro""")

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


def menu():
    print("""
1 - Converter_data
2 - Listar_datas
3 - Sair
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 1, 3)
while True:
    opção = menu()
    if opção == 3:
        break
    elif opção == 1:
        Converter_data()
    elif opção == 2:
        Listar_datas()

