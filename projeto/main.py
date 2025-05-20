import sqlite3

# Caminho do banco de dados
DB_PATH = 'banco_healthy_connection.db'

# Funções chamadas no menu (apenas esqueleto)
def cadastrar_usuario():
    print("\n[🔧] Função de cadastro de usuário ainda será implementada.")

def listar_usuarios():
    print("\n[🔧] Função de listagem de usuários ainda será implementada.")

def buscar_usuario_por_email():
    print("\n[🔧] Função de busca de usuário por email ainda será implementada.")

def atualizar_usuario():
    print("\n[🔧] Função de atualização de dados ainda será implementada.")

def deletar_usuario():
    print("\n[🔧] Função de remoção de usuário ainda será implementada.")

# Função principal do menu
def menu():
    print("===========================================")
    print("💪 Bem-vindo ao Healthy Connection Terminal")
    print("===========================================\n")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar usuário")
        print("2 - Listar todos os usuários")
        print("3 - Buscar usuário por email")
        print("4 - Atualizar dados do usuário")
        print("5 - Remover usuário")
        print("0 - Sair")

        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario_por_email()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "0":
            print("\n[👋] Encerrando o programa. Até logo!")
            break
        else:
            print("\n[⚠️] Opção inválida. Tente novamente.")

# Executar o menu se rodar diretamente
if __name__ == "__main__":
    menu()
