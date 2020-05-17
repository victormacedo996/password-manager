import json
import time
from random import choice
import string


## Primeiro uso
valid_master_pw = False
while valid_master_pw == False:
    master_pw = input('Definir senha mestre? ').lower
    if master_pw != 's' and master_pw != 'n':
        print('Use somente S para sim e N para não')
    else:
        valid_first_use = True



## (Criptografar e salvar master_pw em algum canto)


## Login no programa
login = input('Digite a senha mestre: ')

## (Abrir master_pw para realizar o login)


if  login != master_pw:
    print('Rala mandado!!')
    exit()

dic_password = {}
dic_instructions = {'Sair do programa': 'Q', 'Criar nova senha':'C', 'Excluir senha':'E', 'Consultar senha':'CS'}


## Inicio do loop infinito
infinite_loop = True
while infinite_loop == True:

    ## Menu
    print('O que deseja fazer?')
    print(json.dumps(dic_instructions, indent=1))
    print('\n')

    valid_choose = False
    while valid_choose == False:
        choose = input('')
        if choose != 'q' and choose != 'c' and choose != 'e' and choose != 'cs':
            print('Use somente os comandos acima')
        else:
            valid_choose = True

    ## Comando Q - fim do loop infinito
    if choose == 'q':
        infinite_loop = False
        print('Obrigado por usar o programa!')
        time.sleep(2)

    ## Comando C
    elif choose == 'c':

        ## Validações
        valid_special_character = False
        while valid_special_character == False:
            special_character = input('Usar caracteres especiais? Use S para sim e N para não ').lower()
            if special_character != 's' and special_character != 'n':
                print ('Use apenas S para sim e N para não')
            else:
                valid_special_character = True


        valid_numbers = False
        while valid_numbers == False:
            numbers = input('Usar numeros? Use S para sim e N para não ').lower()
            if numbers!= 's' and numbers != 'n':
                print ('Use apenas S para sim e N para não')
            else:
                valid_numbers = True


        valid_caps_letter = False
        while valid_caps_letter == False:
            caps_letter = input('Usar letras maiusculas? Use S para sim e N para não ').lower()
            if caps_letter != 's' and caps_letter != 'n':
                print ('Use apenas S para sim e N para não')
            else:
                valid_caps_letter = True


        valid_size = False
        while valid_size == False:
            size = input('Com quantos caracteres quer a senha? ')
            try:
                size = int(size)
                if size <= 0:
                    print('O tamanho da senha não pode ser 0, nem negativo')
                else:
                    valid_size = True
            except:
                print ('Use apenas numeros')
                
        ## Serviço sem validação pra poder utilizar qlqr caractere que quiser
        service = input('De qual serviço é a senha? ')

        ## Condicionais para a criação da senha
        if special_character == 's' and numbers == 's' and caps_letter =='s':
            password = ''.join([choice(string.punctuation + string.digits + string.ascii_letters) for i in range(size)])
        elif special_character == 's' and numbers == 's' and caps_letter =='n':
            password = ''.join([choice(string.punctuation  + string.digits + string.ascii_lowercase) for i in range(size)])
        elif special_character == 's' and numbers == 'n' and caps_letter =='s':
            password = ''.join([choice(string.punctuation + string.letters) for i in range(size)])
        elif special_character == 'n' and numbers == 's' and caps_letter == 's':
            password = ''.join([choice(string.digits + string.ascii_letters) for i in range(size)])
        elif special_character == 'n' and numbers == 'n' and caps_letter == 's':
            password = ''.join([choice(string.ascii_letters) for i in range(size)])
        elif special_character == 's' and numbers == 'n' and caps_letter == 'n':
            password = ''.join([choice(string.punctuation) for i in range(size)])
        elif special_character == 'n' and numbers == 's' and caps_letter == 'n':
            password = ''.join([choice(string.digits) for i in range(size)])
        elif special_character =='n' and numbers == 'n' and caps_letter =='n':
            password = ''.join([choice(string.ascii_lowercase) for i in range(size)])

        ## (Arrumar forma de criptografar serviço e senha)

        dic_password[service] = password
        

        ## (Salvar o dic_password em algum canto e conseguir fazer append)

        print(dic_password)
        print('Senha criada com sucesso!')
        print('\n')

    ## Comando E
    elif choose =='e':
        service_del = input('Qual o serviço que quer excluir a senha? ')

        ## (Carregar o dic_password de algum canto e fazer o delete)
        
        del dic_password[service_del]
        print('Senha excluida com sucesso!')

    ## Comando CS
    elif choose == 'cs':
        option = input('Ver senhas salvas = S, ver uma senha especifica = E')
        if option == 's':
            
            ## (Carregar o dic_password de algum canto)
            
            print(json.dumps(dic_password, indent=1))
        else:
            specific_password = input('Qual o serviço buscado? ')

            ## (Carregar o dic_password de algum canto e fazer a busca)

            
            print(dic_password.get(specific_password))
print('\n')
