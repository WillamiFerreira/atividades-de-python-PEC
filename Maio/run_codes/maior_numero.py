def melhor_de(n):
    nota_melhor = 0
    nome_melhor = ''

    for k in range(n):
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Nota do aluno: '))
        if nota > nota_melhor:
            nome_melhor = nome
            nota_melhor = nota
        return nome_melhor, nota_melhor

def main():
    nome, nota = melhor_de(10)
    print(f'Melhor aluno {nome}')
    print(f'Nota: {nota:.2f}')

    if __name__ == '__main__':
        main()