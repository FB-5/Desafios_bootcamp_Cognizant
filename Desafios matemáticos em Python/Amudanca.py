# A Mudança

# Hermione está criando um novo Vira Tempo especialmente para programadores. 
# É impressionante as vantagens que ele oferece e o conforto pra codar que ele tem. 
# O artefato ainda está em desenvolvimento e ele prometeu consertar os bugs e colocar uns apetrechos melhores e, em troca, pediu um sistema simples para o modo Standy Bay. 
# O problema é que o artefato por si só sempre tem o ângulo de inclinação do Sol/Lua(de 0 a 360). Valendo um Vira Tempo, caso deseja aceitar: dada em grau da inclinação do Sol/Lua, informe em qual período do dia ele se encontra.

# Entrada
# A entrada contém um número inteiro M (0 ≤ M ≤ 360) representando o grau do Sol/Lua. Como a posição muda constantemente seu programa receberá diversos casos a cada segundo(EOF).

# Saída
# Imprima uma saudação referente ao período do dia que ele se encontra: "Boa Tarde!!", "Boa Noite!!", "Bom Dia!!" e "De Madrugada!!".

# Exemplo de Entrada
# 0 45 360 90 180

# Exemplo de Saída
# Bom Dia!! Bom Dia!! Bom Dia!! Boa Tarde!! Boa Noite!!

while True:
    try:
        n = int(input())
        if n >= 0 and n < 90 or n == 360:
            print('Bom Dia!!')
        elif n < 180:
            print('Boa Tarde!!')
        elif n < 270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')

    except EOFError:
        break
