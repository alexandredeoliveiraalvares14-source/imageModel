# Análise Técnica do Código - Função `eh_primo()` (Refatorado v2)

## **Estrutura Geral**

O arquivo implementa um verificador de números primos com **otimizações matemáticas** seguindo princípios de **Clean Code**: type hints, documentação clara, tratamento de exceções e separação de responsabilidades. Agora inclui **interatividade com o usuário**.

---

## **Melhorias Implementadas**

### ✅ **Type Hints**
```python
def eh_primo(numero: int) -> bool:
```
- **Benefício:** Melhora legibilidade e permite validação de tipos
- `numero: int` → parâmetro deve ser inteiro
- `-> bool` → função retorna booleano

### ✅ **Tratamento de Exceções**
```python
if not isinstance(numero, int):
    raise TypeError(f"Esperado int, recebido {type(numero).__name__}")
```
- Valida entrada antes de processar
- Gera erro descriptivo se tipo incorreto
- Evita comportamentos inesperados

### ✅ **Nomes Descritivos**
```python
raiz_quadrada = int(numero ** 0.5)  # antes: direto no range
for divisor in range(...):           # antes: variável 'i'
```
- Código auto-documentado e fácil de entender

### ✅ **Interatividade com Usuário** (NOVO!)
```python
def solicitar_numero_usuario() -> int:
def verificar_numero_usuario(numero: int) -> None:
```
- Solicita entrada do usuário
- Valida e trata erros de entrada
- Exibe resultado formatado

---

## **Função Principal: `eh_primo(numero)`**

### **Linha 1: Assinatura com Type Hints**
```python
def eh_primo(numero: int) -> bool:
```
Define entrada (inteiro) e saída (booleano) esperadas.

---

### **Linha 2-11: Docstring Expandida**
```python
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
```
Documenta **comportamento, otimizações e exceções** geradas.

---

### **Linha 12-14: Validação de Tipo**
```python
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, recebido {type(numero).__name__}")
```
**Por quê?** Falha rápido com mensagem clara se entrada inválida.
- `isinstance()` verifica se é inteiro
- f-string com `type().__name__` mostra tipo recebido

---

### **Linha 16-18: Primeiro Filtro - Números Menores que 2**
```python
    # Números menores que 2 não são primos
    if numero < 2:
        return False
```
Comentário explica **por quê** do filtro (clean code).

---

### **Linha 20-22: Segundo Filtro - Número 2**
```python
    # 2 é o único número primo par
    if numero == 2:
        return True
```
Tratamento do caso especial com comentário justificativo.

---

### **Linha 24-26: Terceiro Filtro - Números Pares**
```python
    # Números pares maiores que 2 não são primos
    if numero % 2 == 0:
        return False
```
Elimina ~50% dos candidatos restantes.

---

### **Linha 28-33: Loop Principal - Otimizado**
```python
    # Verifica divisibilidade por números ímpares até √numero
    raiz_quadrada = int(numero ** 0.5)
    for divisor in range(3, raiz_quadrada + 1, 2):
        if numero % divisor == 0:
            return False
    
    return True
```

**Melhorias:**
- `raiz_quadrada` como variável nomeada (legibilidade)
- `divisor` em vez de `i` (clareza semântica)
- Comentário explica limite matemático

| Componente | Explicação |
|-----------|-----------|
| `raiz_quadrada = int(numero ** 0.5)` | Extrai limite em variável nomeada |
| `range(3, raiz_quadrada + 1, 2)` | Testa apenas ímpares até √numero |
| `if numero % divisor == 0` | Encontrou divisor → não é primo |
| `return True` | Nenhum divisor encontrado → é primo |

---

## **Novas Funções Auxiliares**

### **Função: `listar_primos(limite)`**
```python
def listar_primos(limite: int) -> list[int]:
    """
    Retorna lista de todos os números primos até um limite.
    
    Args:
        limite: Valor máximo (inclusive) a verificar.
        
    Returns:
        Lista com todos os números primos encontrados.
    """
    return [num for num in range(2, limite + 1) if eh_primo(num)]
```

**Benefícios:**
- **Single Responsibility:** função dedicada a listar primos
- **List Comprehension:** código conciso e Pythônico
- Reutiliza `eh_primo()` (DRY - Don't Repeat Yourself)

---

### **Função: `exibir_testes(numeros)`**
```python
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
```

**Benefícios:**
- **Separação de Responsabilidades:** lógica de testes separada da exibição
- Facilita testes unitários
- Código mais testável e reutilizável

---

### **Função: `solicitar_numero_usuario()` (NOVO!)**
```python
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
```

**O que faz:**
- **Loop infinito** (`while True`) garante entrada válida
- `int(input())` converte entrada do usuário em inteiro
- **Try/Except** captura `ValueError` se entrada não for numérica
- **Mensagem de erro** amigável ao usuário
- Emoji 📝 para melhor UX (User Experience)

**Fluxo:**
1. Solicita número ao usuário
2. Tenta converter para inteiro
3. Se sucesso → retorna o número
4. Se erro → mostra mensagem e pede novamente

---

### **Função: `verificar_numero_usuario(numero)` (NOVO!)**
```python
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
```

**O que faz:**
- Chama `eh_primo()` com número do usuário
- **Operador ternário** (`if resultado else`) para determinar status
- Exibe resultado em **caixa formatada** com emojis
- **Tratamento de exceção** para erros de tipo

---

## **Ponto de Entrada (Main)**

```python
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
```

**Estrutura do programa:**

| Fase | O que faz |
|------|-----------|
| **Cabeçalho** | Exibe título formatado |
| **Fase 1** | Testa números pré-definidos em tabela |
| **Fase 2** | Lista todos os primos até 50 |
| **Fase 3** | Solicita número ao usuário e verifica |

---

## **Fluxo de Execução com Exemplo**

### Entrada do usuário: `17`

```
========================================
🔢 VERIFICADOR DE NÚMEROS PRIMOS 🔢
========================================

📊 Executando testes com números pré-definidos:

Número     É Primo?       
-------------------------
1          False          
2          True           
... (continua)

📋 Números primos até 50:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

📝 Digite um número inteiro para verificar se é primo: 17

========================================
Número informado: 17
Status: ✅ É PRIMO
========================================
```

---

## **Princípios de Clean Code Aplicados**

| Princípio | Implementação |
|-----------|--------------|
| **KISS** (Keep It Simple, Stupid) | Lógica clara, sem complexidade desnecessária |
| **DRY** (Don't Repeat Yourself) | Funções reutilizáveis, sem duplicação |
| **SOLID** | Single Responsibility em cada função |
| **Type Safety** | Type hints em todas as funções |
| **Documentação** | Docstrings completas (Args, Returns, Raises) |
| **Nomes Descritivos** | Variáveis e funções auto-explicativas |
| **Tratamento de Erros** | Validação com mensagens claras |
| **UX** | Emojis e formatação para melhor experiência |
| **Validação de Entrada** | Loop até entrada válida |

---

## **Complexidade Computacional**

- **Melhor caso:** O(1) - número é 2 ou < 2
- **Pior caso:** O(√n) - testa até raiz quadrada
- **Espaço:** O(1) - usa apenas variáveis locais
- **`listar_primos(n)`:** O(n√n) no pior caso

---

## **Como Executar**

1. Abra o terminal no VS Code
2. Execute: `python num_primo.py`
3. Observe os testes automatizados
4. Digite um número quando solicitado
5. Veja o resultado formatado

Esta é uma implementação **robusta, interativa e mantível**! 🚀