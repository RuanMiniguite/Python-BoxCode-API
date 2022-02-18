import requests
from pprint import pprint
from time import sleep
import os

url = "http://127.0.0.1:8080"

def menu():
    print("-------------------:-------------------")
    print("| 1 |  Cadastrar Usuario              |")
    print("| 2 |  Exibir    Usuario              |")
    print("| 3 |  Alterar   Usuario              |")
    print("| 4 |  Excluir   Usuario              |")
    print("-------------------:-------------------")
    print("| 6 |  Cadastrar Projeto              |")
    print("| 5 |  Exibir    Projeto              |")
    print("| 8 |  Alterar   Projeto              |")
    print("| 7 |  Excluir   Projeto              |")
    print("-------------------:-------------------")


def main():
    os.system('clear') or None
    menu()
    opc = input("Informe uma opcao: \n")

    if opc == "1":      
      pass

    elif opc == "2":    
      pass
    
    elif opc == "3":    
      pass

    elif opc == "4":    
      pass
    
    elif opc == "5":    
      pass

    elif opc == "6":    
      pass

    elif opc == "7":    
      pass

    elif opc == "8":    
      pass
    
    sleep(1)
    input("Pressione ENTER para continuar!\n")


# cliente = {"nome": "Joao Pedro", "endereco": "Rua XYZ"}
# requests.post(f"{url}/cliente", json=cliente)

# cliente = {"id": "01", "nome": "Ruan", "endereco": "Rua XYZ"}
# requests.put(f"{url}/cliente", json=cliente)

# r = requests.get(f"{url}/cliente")
# pprint(r.json())

if __name__ == "__main__":
    main()