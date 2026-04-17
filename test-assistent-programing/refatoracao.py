def calculate_statistics(numbers):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numbers: Lista de números para análise
        
    Returns:
        Tupla contendo (soma, média, máximo, mínimo)
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


# Lista de números para análise
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Calcular estatísticas
total, average, maximum, minimum = calculate_statistics(data)

# Exibir resultados
print("total:", total)
print("media:", average)
print("maior:", maximum)
print("menor:", minimum)