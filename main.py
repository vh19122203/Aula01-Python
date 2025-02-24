# Função para obter dados do usuário
def obter_dados_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome, idade

# Função para verificar a maioridade
def verificar_maioridade(idade):
    if idade >= 18:
        return "maior de idade"
    elif 12 <= idade < 18:
        return "adolescente"
    else:
        return "criança"

# Função para calcular a soma dos números de uma lista
def calcular_soma(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Função para exibir uma contagem regressiva
def contagem_regressiva(inicio):
    while inicio > 0:
        print(f"Contagem Regressiva: {inicio}")
        inicio -= 1
    print("Contagem finalizada!")

# Função principal
def main():
    # Variáveis
    nome, idade = obter_dados_usuario()
    status = verificar_maioridade(idade)
    
    # Estrutura de decisão
    print(f"Olá {nome}, você é {status}.")
    
    # Solicitar uma lista de números ao usuário
    numeros = []
    quantidade = int(input("Quantos números você deseja adicionar à lista? "))
    for _ in range(quantidade):
        numero = int(input("Digite um número: "))
        numeros.append(numero)
    
    # Calcular e exibir a soma dos números
    soma = calcular_soma(numeros)
    print(f"A soma dos números digitados é: {soma}")
    
    # Exibir contagem regressiva
    inicio_contagem = int(input("Digite o número inicial para a contagem regressiva: "))
    contagem_regressiva(inicio_contagem)
    
    print("Fim do programa.")

# Execução do programa
if __name__ == "__main__":
    main()