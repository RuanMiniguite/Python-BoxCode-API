import requests
from pprint import pprint
from time import sleep
import os

url = "http://0.0.0.0:8080"


def menu():
    os.system('clear') or None
    print("-------------------:-------------------")
    print("| 1 |  Cadastrar Usuario              |")
    print("| 2 |  Exibir    Usuario              |")
    print("| 3 |  Alterar   Usuario              |")
    print("| 4 |  Excluir   Usuario              |")
    print("-------------------:-------------------")
    print("| 5 |  Cadastrar Projeto              |")
    print("| 6 |  Exibir    Projeto              |")
    print("| 7 |  Alterar   Projeto              |")
    print("| 8 |  Excluir   Projeto              |")
    print("-------------------:-------------------")
    print("| 9 |  SAIR                           |")
    print("-------------------:-------------------")

def menu1():
    os.system('clear') or None
    print("-------------------:-------------------")
    print("| 1 |  Pessoa Física                  |")
    print("| 2 |  Pessoa Jurídica        Sair[0] |")
    print("-------------------:-------------------")

def menu2():
    print("-------------------:-------------------")
    print("|        Deseja alterar usuario       |")
    print("|         [1] Sim      [2] Não        |")
    print("-------------------:-------------------")

def main():
    opc = None
    while opc != "9":
        menu()
        opc = input("Informe uma opcao: ")

        if opc == "1":        #Cadastrar Usuario   
            cadastroUser()

        elif opc == "2":      #Exibir Usuario   
            exibirUser()
        
        elif opc == "3":      #Alterar Usuario
            alterarUser()

        elif opc == "4":      #Excluir Usuario
            excluirUser()
        
        elif opc == "5":      #Cadastrar Projeto  
            cadastroProj()

        elif opc == "6":      #Exibir Projeto
            exibirProj()

        elif opc == "7":      #Alterar Projeto
            alterarProj()

        elif opc == "8":      #Excluir Projeto
            excluirProj()

        elif opc == "9":    
            exit()
        
        input("Pressione ENTER para continuar!\n")


# ------------------------ USER ------------------------
def cadastroUser():
    opc = None
    while opc != 1 and opc != 2 and opc != 0:
        
        menu1()
        opc = input("Informe uma opcao: \n")

        if opc == "1":        #Fisica
            nome =  input("Informe nome: ")
            idade = input("Informe idade: ")
            cpf = input("Informe cpf: ")
            instEnsino = input("Informe Instuicao de ensino: ")
            
            data = {"nome": nome, "idade": idade, "cpf": cpf, "instEnsino": instEnsino}
            requests.post(f"{url}/fisica", json=data)
        
        elif opc == "2":      #Juridica
            nome =  input("Informe nome: ")
            segmento = input("Informe segmento: ")
            cnpj = input("Informe cnpj: ")      

            data = {"nome": nome, "segmento": segmento, "cnpj": cnpj}
            requests.post(f"{url}/juridica", json=data)

        elif opc == "0":
            break

        else:
            print("Opção invalida!")
            input("Pressione ENTER para continuar!\n")

def exibirUser():
    opc = None
    while opc != 1 and opc != 2 and opc != 0:
       
        menu1()
        opc = input("Informe uma opcao: \n")

        if opc == "1":           #Fisica
            cpf = input("Informe o cpf: ")
            resp = requests.get(f"{url}/fisica/" + cpf)
            pprint(resp.json())
            input("Pressione ENTER para continuar!\n")
        
        elif opc == "2":         #Juridica
            cnpj = input("Informe o cnpj: ")
            resp = requests.get(f"{url}/juridica/" + cnpj)
            pprint(resp.json())
            input("Pressione ENTER para continuar!\n")

        elif opc == "0":
            break

        else:
            print("Opção invalida!")
            input("Pressione ENTER para continuar!\n")

def alterarUser():
    opc = None
    while opc != 1 and opc != 2 and opc != 0:
        
        menu1()
        opc = input("Informe uma opcao: \n")

        if opc == "1":           #Fisica
            cpf = input("Informe o cpf: ")
            resp = requests.get(f"{url}/fisica/" + cpf)
            pprint(resp.json())
            
            menu2()
            opc1 = input("Informe uma opcao: ")
            
            if opc1 == "1":
                nome =  input("Informe nome: ")
                idade = input("Informe idade: ")
                instEnsino = input("Informe Instuicao de ensino: ")

                data = {"nome": nome, "idade": idade, "cpf": cpf, "instEnsino": instEnsino}
                requests.put(f"{url}/fisica/" + cpf, json=data)
            else:
                break

            input("Pressione ENTER para continuar!\n")
        
        elif opc == "2":         #Juridica
            cnpj = input("Informe o cnpj: ")
            resp = requests.get(f"{url}/juridica/" + cnpj)
            pprint(resp.json())

            menu2()
            opc1 = input("Informe uma opcao: ")
            if opc1 == "1":
                nome =  input("Informe nome: ")
                segmento = input("Informe segmento: ")

                data = {"nome": nome, "segmento": segmento, "cnpj": cnpj}
                requests.put(f"{url}/juridica/" + cnpj, json=data)
           
            else:
                break
              
        elif opc == "0":
            break

        else:
            print("Opção invalida!")
            input("Pressione ENTER para continuar!\n")

def excluirUser():
    opc = None
    while opc != 1 and opc != 2 and opc != 0:
       
        menu1()
        opc = input("Informe uma opcao: \n")

        if opc == "1":
            cpf = input("Informe o cpf: ")
            resp = requests.delete(f"{url}/fisica/" + cpf)
            print(resp)

        elif opc == "2":
            cnpj = input("Informe o cnpj: ")
            resp = requests.delete(f"{url}/juridica/" + cnpj)
            print(resp)
        
        elif opc == "0":
            break

        else:
            print("Opção invalida!")
            input("Pressione ENTER para continuar!\n")

# ------------------------ PROJETO ------------------------
def cadastroProj():
    nome =  input("Informe nome: ")
    segmento = input("Informe o segmento: ")

    data = {"nome": nome, "segmento": segmento}
    requests.post(f"{url}/projeto", json=data)

def exibirProj():
    id = input("Informe o ID: ")
    resp = requests.get(f"{url}/projeto/" + id)
    pprint(resp.json())

def alterarProj():
    pass

def excluirProj():
    id = input("Informe o ID: ")
    resp = requests.delete(f"{url}/projeto/" + id)
    pprint(resp.json())


if __name__ == "__main__":
    main()