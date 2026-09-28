import subalgoritmos as sub

pessoa: dict[str, dict[str, str]] = {}

while True:
    sub.menu()

    try:
        escolha: int = int(input("Escolha: "))
    except ValueError:
        print("Digite uma opção numérica.")
        sub.continuar()
        continue

    match escolha:
        case 0:
            print("Programa encerrado.")
            break

        case 1:
            sub.limpar_tela()

            cpf: str = sub.pedir_cpf()
            tipo_arquivo: str = sub.escolher_cadastro()

            if tipo_arquivo != "":
                if sub.verificar_cpf(tipo_arquivo, cpf):
                    print("O CPF já existe no arquivo selecionado.")
                else:
                    nome, endereco, celular = sub.pedir_dados()

                    pessoa[cpf] = {
                        "nome": nome,
                        "endereco": endereco,
                        "celular": celular
                    }

                    sub.gravar_dados(tipo_arquivo, pessoa, cpf)
                    print("Cadastro realizado com sucesso.")

            sub.continuar()

        case 2:
            sub.limpar_tela()

            tipo_arquivo = sub.escolher_lista()

            if tipo_arquivo != "":
                if sub.verificar_existe(tipo_arquivo):
                    sub.listar_dados(tipo_arquivo)
                else:
                    print("O arquivo solicitado não existe.")

            sub.continuar()

        case _:
            print("Opção inválida.")
            sub.continuar()
