import requests
from pprint import pprint
from time import sleep
import os

url = "http://127.0.0.1:8080"


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
  print("| 2 |  Pessoa Jurídica                |")
  print("-------------------:-------------------")



def main():
  opc = None
  while opc != "9":
    menu()
    opc = input("Informe uma opcao: \n")

    if opc == "1":        #Cadastrar Usuario   
      cadastroUser()

    elif opc == "2":      #Exibir Usuario   
      exibirUser()
    
    elif opc == "3":      #Alterar Usuario
      alterarUser()

    elif opc == "4":      #Excluir Usuario
      excluirUser()
    
    elif opc == "5":    
      pass

    elif opc == "6":    
      pass

    elif opc == "7":    
      pass

    elif opc == "8":    
      pass

    elif opc == "9":    
      exit()
    
    sleep(1)
    input("Pressione ENTER para continuar!\n")



# ------------------------ USER ------------------------

def cadastroUser():
  opc = None
  while opc != 1 and opc != 2:
    menu1()
    opc = input("Informe uma opcao: \n")

    if opc == "1":        #Fisica
      nome =  input("Informe nome: ")
      idade = input("Informe idade: ")
      cpf = input("Informe cpf: ")
      instEnsino = input("Informe Instuição de ensino: ")
      
      data = {"nome": nome, "idade": idade, "cpf": cpf, "instEnsino": instEnsino}
      requests.post(f"{url}/addfisica", json=data)

    elif opc == "2":      #Juridica
      nome =  input("Informe nome: ")
      segmento = input("Informe idade: ")
      cnpj = input("Informe cpf: ")      

      data = {"nome": nome, "segmento": segmento, "cnpj": cnpj}
      requests.post(f"{url}/addjuridica", json=data)

    else:
      print("Opção invalida!")
      input("Pressione ENTER para continuar!\n")

def exibirUser():
  opc = None
  while opc != 1 and opc != 2:
    menu1()
    opc = input("Informe uma opcao: \n")

    if opc == "1":
      id = input("Informe o ID: ")
      resp = requests.get(f"{url}/fisica/" + id)
      pprint(resp.json())

    elif opc == "2":
      id = input("Informe o ID: ")
      resp = requests.get(f"{url}/juridica/" + id)
      pprint(resp.json())

    else:
      print("Opção invalida!")
      input("Pressione ENTER para continuar!\n")

def alterarUser():
  pass

def excluirUser():
  opc = None
  while opc != 1 and opc != 2:
    menu1()
    opc = input("Informe uma opcao: \n")

    if opc == "1":
      id = input("Informe o ID: ")
      resp = requests.delete(f"{url}/fisica/" + id)
      pprint(resp.json())

    elif opc == "2":
      id = input("Informe o ID: ")
      resp = requests.delete(f"{url}/juridica/" + id)
      pprint(resp.json())

    else:
      print("Opção invalida!")
      input("Pressione ENTER para continuar!\n")

# ------------------------ PROJETO ------------------------







if __name__ == "__main__":
  main()



# cliente = {"nome": "Joao Pedro", "endereco": "Rua XYZ"}
# requests.post(f"{url}/cliente", json=cliente)

# cliente = {"id": "01", "nome": "Ruan", "endereco": "Rua XYZ"}
# requests.put(f"{url}/cliente", json=cliente)

# r = requests.get(f"{url}/cliente")
# pprint(r.json())