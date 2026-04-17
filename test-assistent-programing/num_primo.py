def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.
    
    Utiliza otimizações matemáticas para melhorar performance:
    - Testa apenas números ímpares até √numero
    - Retorna imediatamente ao encontrar divisor
    
    Args:
        numero: Um inteiro a ser verificado.
        
    Returns:
        True se o número é primo, False caso contrário.
        
    Raises:
        TypeError: Se o argumento não for um inteiro.
    """
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, recebido {type(numero).__name__}")
    
    # Números menores que 2 não são primos
    if numero < 2:
        return False
    
    # 2 é o único número primo par
    if numero == 2:
        return True
    
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False
    
    # Verifica divisibilidade por números ímpares até √numero
    raiz_quadrada = int(numero ** 0.5)
    for divisor in range(3, raiz_quadrada + 1, 2):
        if numero % divisor == 0:
            return False
    
    return True


def listar_primos(limite: int) -> list[int]:
    """
    Retorna lista de todos os números primos até um limite.
    
    Args:
        limite: Valor máximo (inclusive) a verificar.
        
    Returns:
        Lista com todos os números primos encontrados.
    """
    return [num for num in range(2, limite + 1) if eh_primo(num)]


def exibir_testes(numeros: list[int]) -> None:
    """
    Exibe resultado dos testes em formato de tabela.
    
    Args:
        numeros: Lista de números a testar.
    """
    print("Testando a função eh_primo():\n")
    print(f"{'Número':<10} {'É Primo?':<15}")
    print("-" * 25)
    
    for numero in numeros:
        resultado = eh_primo(numero)
        print(f"{numero:<10} {str(resultado):<15}")


def solicitar_numero_usuario() -> int:
    """
    Solicita ao usuário que digite um número inteiro.
    
    Valida a entrada e garante que um inteiro válido seja retornado.
    
    Returns:
        Um número inteiro fornecido pelo usuário.
        
    Raises:
        ValueError: Se a entrada não for um inteiro válido.
    """
    while True:
        try:
            numero = int(input("\n📝 Digite um número inteiro para verificar se é primo: "))
            return numero
        except ValueError:
            print("❌ Erro: Por favor, digite um número inteiro válido!")


def verificar_numero_usuario(numero: int) -> None:
    """
    Verifica se um número fornecido pelo usuário é primo e exibe resultado.
    
    Args:
        numero: Um número inteiro a ser verificado.
    """
    try:
        resultado = eh_primo(numero)
        status = "✅ É PRIMO" if resultado else "❌ NÃO É PRIMO"
        
        print("\n" + "=" * 40)
        print(f"Número informado: {numero}")
        print(f"Status: {status}")
        print("=" * 40)
        
    except TypeError as erro:
        print(f"Erro de tipo: {erro}")


# Ponto de entrada do programa
if __name__ == "__main__":
    print("=" * 40)
    print("🔢 VERIFICADOR DE NÚMEROS PRIMOS 🔢")
    print("=" * 40)
    
    # Opção 1: Testar números pré-definidos
    print("\n📊 Executando testes com números pré-definidos:")
    numeros_teste = [1, 2, 3, 4, 5, 10, 11, 13, 17, 20, 23, 29, 30, 97, 100]
    exibir_testes(numeros_teste)
    
    # Opção 2: Listar primos até 50
    print("\n\n📋 Números primos até 50:")
    primos = listar_primos(50)
    print(primos)
    
    # Opção 3: Solicitar número do usuário
    numero_usuario = solicitar_numero_usuario()
    verificar_numero_usuario(numero_usuario)
