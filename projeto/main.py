import sqlite3

# Caminho do banco de dados já existente
DB_PATH = 'banco_healthy_connection.db'

# Cadastro de novo usuário
def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Nome completo: ")
    email = input("Email: ")
    senha = input("Crie uma senha: ")

    lgpd = input("Você aceita os termos da LGPD? (s/n): ").lower()
    if lgpd != "s":
        print("[❌] Cadastro cancelado. É necessário aceitar a LGPD.")
        return
    aceitou_lgpd = True

    idade = input("Idade: ")
    genero = input("Gênero (M/F/Outro): ")

    print("\nQual o seu objetivo?")
    print("1 - Perder peso")
    print("2 - Ganhar massa")
    print("3 - Manter a saúde")
    opcao = input("Digite o número correspondente: ")

    objetivos = {"1": "Perder peso", "2": "Ganhar massa", "3": "Manter saúde"}
    objetivo = objetivos.get(opcao, "Outro")

    try:
        conexao = sqlite3.connect(DB_PATH)
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO Usuario (nome, email, senha, aceitou_lgpd, idade, genero, objetivo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nome, email, senha, aceitou_lgpd, idade, genero, objetivo))
        conexao.commit()
        conexao.close()
        print("[✅] Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("[⚠️] Já existe um usuário com este email.")
    except Exception as e:
        print(f"[❌] Erro ao cadastrar: {e}")

# Login de usuário
def login():
    print("\n=== Login de Usuário ===")
    email = input("Email: ")
    senha = input("Senha: ")

    try:
        conexao = sqlite3.connect(DB_PATH)
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT nome FROM Usuario WHERE email = ? AND senha = ?
        ''', (email, senha))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            print(f"[✅] Login bem-sucedido! Bem-vindo, {resultado[0]}.")
        else:
            print("[❌] Email ou senha incorretos.")
    except Exception as e:
        print(f"[❌] Erro no login: {e}")

# Funções extras (em desenvolvimento)
def listar_usuarios():
    print("\n[🔧] Função de listagem de usuários ainda será implementada.")

def buscar_usuario_por_email():
    print("\n[🔧] Função de busca de usuário por email ainda será implementada.")

def atualizar_usuario():
    print("\n[🔧] Função de atualização de dados ainda será implementada.")

def deletar_usuario():
    print("\n[🔧] Função de remoção de usuário ainda será implementada.")

# Menu principal
def menu():
    print("===========================================")
    print("💪 Bem-vindo ao Healthy Connection Terminal")
    print("===========================================\n")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar novo usuário")
        print("2 - Login")
        print("3 - Listar todos os usuários")
        print("4 - Buscar usuário por email")
        print("5 - Atualizar dados do usuário")
        print("6 - Remover usuário")
        print("0 - Sair")

        opcao = input("\nDigite sua opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login()
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            buscar_usuario_por_email()
        elif opcao == "5":
            atualizar_usuario()
        elif opcao == "6":
            deletar_usuario()
        elif opcao == "0":
            print("\n[👋] Encerrando o programa. Até logo!")
            break
        else:
            print("\n[⚠️] Opção inválida. Tente novamente.")

# Executar o menu se rodar diretamente
if __name__ == "__main__":
    menu()
