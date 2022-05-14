#Pois bem, desafio você agora a colocar suas habilidades em prática e seu poder de pesquisa. Vamos lá? Que tal abrimos nosso Colab
# ou se preferir, seu jupyter notebook e começar a “escrever”? Afinal, somente colocando em prática iremos fixar o que aprendemos e 
# iremos também errar. É, é isso mesmo, errar. Errar faz parte do aprendizado e estamos aqui para te ajudar a corrigir os erros e abrir novos horizontes.
#Quero que você crie um programa que dirá se um entrevistado um usuário é do grupo de risco da COVID-19, ou não. Para isso, seguem as 
# informações que você precisa coletar do usuário e as condições para determinar se o mesmo pertence ao grupo de risco, ou não;
#->	O entrevistado possui mais de 60 anos?
#->	O entrevistado possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?
#->	Se mulher, está grávida?
#Após exibir o resultado se faz parte, ou não do grupo de risco, o programa deve exibir a mensagem de recomendações de prevenção: 
# “Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos”




print('\n Ola, vamos fazer um teste de covid?\nToma essa vacina po!\n')
recomendacao = '''Vamos tomar cuidado ao sair no caralho da rua, tem um trem la que mata sua familia toda!'''
recomendacaoGravida = '''Evite sair de casa e use mascara, cuidado com algumas vacinas ai'''
        


sexo = input("Você é homem ou mulher?\nDigite H para homem ou M para mulher\n\n")
if sexo.upper() == 'M':
    gravidez = input('Voce esta gravida? Sim(S) / Nao(N)\n\n')
if gravidez.upper() == 'S':
    print(recomendacaoGravida)
elif gravidez.upper() == 'N':
    print(recomendacao)
else:
    print('Letra incorreta!')
    
idade = input("Digite sua idade por gentileza\n\n")    
if idade < str('18') or idade > str('18') and idade < str('60'):
    print(recomendacao)
elif idade > str('60'):
    print('Tome cuidado ao sair de casa!\n')
    identificacaoDoenca = input("Você possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?\n Sim ou não?\n\n")
    if identificacaoDoenca.upper() == 'S':
        print('Va ao medico')
    elif identificacaoDoenca.upper() == 'N':
        print(recomendacao)
    else:
        print('Comando errado')
else:
    print('Comando errado')
    
