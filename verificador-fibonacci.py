while True:
    print("""
Verificador de números da sequência de Fibonacci
          
          """)
    numero = int(input("Digite um número: "))
    a = 0
    b = 1
    encontrado = False

    while a <= numero:
        if a == numero:
            encontrado = True
            break
        a, b = b, a + b
    
    if encontrado:
        print(f"O número {numero} faz parte da sequência de Fibonacci!!")
    else:
        print(f"O número {numero} não faz parte da sequência de Fibonacci!!")