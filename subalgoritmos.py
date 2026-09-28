import csv
import json


def limpar_tela() -> None:
    print("\n" * 30)


def continuar() -> None:
    input("\nPressione ENTER para continuar...")


def menu() -> None:
    print("\nMENU")
    print("0 - SAIR")
    print("1 - Cadastrar dados")
    print("2 - Listar dados")


def pedir_cpf() -> str:
    while True:
        cpf: str = input("CPF: ").strip()

        if cpf != "":
            return cpf

        print("O CPF não pode ficar em branco.")


def escolher_cadastro() -> str:
    while True:
        print("\nCadastrar dados:")
        print("1 - Arquivo Texto")
        print("2 - Arquivo CSV")
        print("3 - Arquivo Json")
        print("4 - Voltando ao menu anterior")

        escolha: str = input("Escolha: ").strip()

        match escolha:
            case "1":
                return "txt"
            case "2":
                return "csv"
            case "3":
                return "json"
            case "4":
                return ""
            case _:
                print("Opção inválida.")


def escolher_lista() -> str:
    while True:
        print("\nListar dados")
        print("1 - Do arquivo Texto")
        print("2 - Do arquivo CSV")
        print("3 - Do arquivo Json")
        print("4 - Voltar ao menu anterior")

        escolha: str = input("Escolha: ").strip()

        match escolha:
            case "1":
                return "txt"
            case "2":
                return "csv"
            case "3":
                return "json"
            case "4":
                return ""
            case _:
                print("Opção inválida.")


def pedir_dados() -> tuple[str, str, str]:
    nome: str = input("Nome: ").strip()
    endereco: str = input("Endereço: ").strip()
    celular: str = input("Celular: ").strip()

    return nome, endereco, celular


def verificar_existe(tipo_arquivo: str) -> bool:
    nome_arquivo: str = f"pessoa.{tipo_arquivo}"

    try:
        with open(nome_arquivo, "r", encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def verificar_cpf(tipo_arquivo: str, cpf: str) -> bool:
    nome_arquivo: str = f"pessoa.{tipo_arquivo}"

    try:
        if tipo_arquivo == "txt":
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                linha: str

                for linha in arquivo:
                    if linha.strip() == f"CPF: {cpf}":
                        return True

        elif tipo_arquivo == "csv":
            with open(
                nome_arquivo,
                "r",
                newline="",
                encoding="utf-8"
            ) as arquivo:
                leitor = csv.reader(arquivo)
                linha: list[str]

                for linha in leitor:
                    if len(linha) > 0 and linha[0] == cpf:
                        return True

        elif tipo_arquivo == "json":
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo: str = arquivo.read()

            if conteudo.strip() == "":
                return False

            dados: dict[str, dict[str, str]] = json.loads(conteudo)
            return cpf in dados

    except FileNotFoundError:
        return False

    return False


def gravar_dados(
    tipo_arquivo: str,
    pessoa: dict[str, dict[str, str]],
    cpf: str
) -> None:
    if tipo_arquivo == "txt":
        with open("pessoa.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"CPF: {cpf}\n")
            arquivo.write(f"Nome: {pessoa[cpf]['nome']}\n")
            arquivo.write(f"Endereço: {pessoa[cpf]['endereco']}\n")
            arquivo.write(f"Celular: {pessoa[cpf]['celular']}\n")
            arquivo.write("-" * 30 + "\n")

    elif tipo_arquivo == "csv":
        arquivo_vazio: bool = True

        try:
            with open("pessoa.csv", "r", encoding="utf-8") as arquivo:
                arquivo_vazio = arquivo.read(1) == ""
        except FileNotFoundError:
            arquivo_vazio = True

        with open(
            "pessoa.csv",
            "a",
            newline="",
            encoding="utf-8"
        ) as arquivo:
            escritor = csv.writer(arquivo)

            if arquivo_vazio:
                escritor.writerow(
                    ["CPF", "NOME", "ENDERECO", "CELULAR"]
                )

            escritor.writerow([
                cpf,
                pessoa[cpf]["nome"],
                pessoa[cpf]["endereco"],
                pessoa[cpf]["celular"]
            ])

    elif tipo_arquivo == "json":
        dados: dict[str, dict[str, str]] = {}

        try:
            with open("pessoa.json", "r", encoding="utf-8") as arquivo:
                conteudo: str = arquivo.read()

            if conteudo.strip() != "":
                dados = json.loads(conteudo)

        except FileNotFoundError:
            dados = {}

        dados[cpf] = pessoa[cpf]

        with open("pessoa.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )


def listar_dados(tipo_arquivo: str) -> None:
    if tipo_arquivo == "txt":
        with open("pessoa.txt", "r", encoding="utf-8") as arquivo:
            print("\nDADOS DO ARQUIVO TEXTO")
            print(arquivo.read())

    elif tipo_arquivo == "csv":
        with open(
            "pessoa.csv",
            "r",
            newline="",
            encoding="utf-8"
        ) as arquivo:
            leitor = csv.reader(arquivo)

            print("\nDADOS DO ARQUIVO CSV")

            linha: list[str]
            for linha in leitor:
                print(" | ".join(linha))

    elif tipo_arquivo == "json":
        with open("pessoa.json", "r", encoding="utf-8") as arquivo:
            conteudo: str = arquivo.read()

        print("\nDADOS DO ARQUIVO JSON")

        if conteudo.strip() == "":
            print("O arquivo está vazio.")
            return

        dados: dict[str, dict[str, str]] = json.loads(conteudo)

        cpf: str
        dados_pessoa: dict[str, str]

        for cpf, dados_pessoa in dados.items():
            print(f"\nCPF: {cpf}")
            print(f"Nome: {dados_pessoa['nome']}")
            print(f"Endereço: {dados_pessoa['endereco']}")
            print(f"Celular: {dados_pessoa['celular']}")
