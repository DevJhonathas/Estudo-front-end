'''Quero que você crie um programa que dirá se um entrevistado (um usuário) é do grupo de risco da COVID-19, ou não.
Para isso, seguem as informações que você precisa coletar do usuário e as condições para determinar se o mesmo pertence ao grupo de risco, ou não;

->	O entrevistado possui mais de 60 anos?

->	O entrevistado possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?

->	Se mulher, está grávida?

Após exibir o resultado se faz parte, ou não do grupo de risco, o programa deve exibir a mensagem de recomendações de prevenção:
“Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos”'''



print('''
      *** PRETENCAO AO COVID-19 ***
      \n''')
idade = int(input("Gentileza me informe sua idade: "))

if idade >= 60:
    print("\nPor favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos")
else:
    doenca = input('''\nVoce por acaso possui alguma doenca, como: asma, diabetes, hipertensão, ou câncer?
Escrever: Sim ou nao!
      \n''')
    if doenca.upper == 'S' or doenca.upper == 'Sim' or doenca.upper == 'SIM':
        print("\nPor favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos")
    else:
        genero = input('Qual seu sexo? H = homem, M = mulher')
        if genero.upper == 'M' or genero.upper == 'Mulher' or genero.upper == 'MULHER':
            generoFeminino = input('Voce por acaso esta gravida?')
            if generoFeminino.upper == 'S' or generoFeminino.upper == 'Sim' or generoFeminino.upper == 'SIM':
                print("\nPor favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos")
        else:
            print('''\nVoce nao possui riscos, mas tome medidas preventivas para que pessoas que possuem nao sofram as cosequencias por suas escolhas!
Utilize mascaras ao sair e utilize alcool nas maos
''')
print('''\n\n
        *** FIM DO TESTE DE PRETENCAO AO COVID-19 ***''')
        
        
        
        
        #Apresenta erros que devem ser corrigidos eventualmente
        #Erros: nao esta lendo as funcoes abaixo de doencas, apenas pula para linha final