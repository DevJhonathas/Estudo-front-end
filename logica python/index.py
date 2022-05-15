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




from fileinput import close
from traceback import print_tb


print('\n Ola, vamos fazer um teste de covid?\n Vamos tomar essa vacina po!\n')
recomendacao = '''Vamos tomar cuidado ao sair na rua, tem um trem la que mata sua familia toda!'''  #Variavel para recomendacoes gerais
recomendacaoGravida = '''Evite sair de casa e use mascara, cuidado com algumas vacinas ai''' #Variavel para recomendacao para gravidas
        

#INFORMACOES SOBRE A SEXUALIDADE DA PESSOA
sexo = input("Primeiramente você é homem ou mulher?\nDigite H para homem ou M para mulher\n\n")
if sexo.upper() == 'M':
    gravidez = input('Voce esta gravida? Sim(S) / Nao(N)\n\n')  # Analisando se a mulher esta gravida ou nao
    if gravidez.upper() == 'S':
        print(recomendacaoGravida) # Informacao gravida
        print('Anotando dados\n 30%...')
    elif gravidez.upper() == 'N':
        print(recomendacao)
        print('Anotando dados\n 30%...') # Informacao nao gravida
elif sexo.upper() == 'H':
    print('Anotando dados\n 30%...')  # Informacao homem
else:
    print('Letra incorreta!')

#INFORMACOES SOBRE IDADES E DOENCAS
idade = input("Digite sua idade por gentileza\n\n")    
if idade > str('18') or idade < str('60'):
    print(recomendacao)  # Informacao para pessoas que nao prioridade
    print('Anotando dados\n 50%...') 
    identificacaoDoenca = input("Você possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?\n Sim ou não?\n\n")
    if identificacaoDoenca.upper() == 'S':
        print('Va ao medico')  # Informacao para pessoas com doencas
    elif identificacaoDoenca.upper() == 'N':
        print(recomendacao)  # Informacao para pessoas que nao tenham doencas
    else:
        print('Letra incorreta!')
elif idade < str('18'):
    print('Tome cuidado para n ser infectado e matar sua familia')
    print(recomendacao)
    identificacaoDoenca = input("Você possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?\n Sim ou não?\n\n")
    if identificacaoDoenca.upper() == 'S':
        print('Va ao medico')# Informacao para pessoas com doencas
        print('\nConsulta Finalizada\n dados: 100%...')
    elif identificacaoDoenca.upper() == 'N':
        print(recomendacao)# Informacao para pessoas que nao tenham doencas
        print('\nConsulta Finalizada\n dados: 100%...')
    else:
        print('Comando errado')
elif idade > str('60'):
    print('Tome cuidado ao sair de casa!\n')
    identificacaoDoenca = input("Você possui alguma doença pré-existente, tipo asma, diabetes, hipertensão, ou câncer?\n Sim ou não?\n\n")
    if identificacaoDoenca.upper() == 'S':
        print('Va ao medico')# Informacao para pessoas com doencas
        print('\nConsulta Finalizada\n dados: 100%...')
    elif identificacaoDoenca.upper() == 'N':
        print(recomendacao)# Informacao para pessoas que nao tenham doencas
        print('\nConsulta Finalizada\n dados: 100%...')
    else:
        print('Comando errado')
else: 
    print('\nConsulta Finalizada\n dados: 100%...') #FINALIZANDO PROGRAMA...
    
