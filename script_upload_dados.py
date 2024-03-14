from manipula_repos import ManipulaRpositorios

# Instanciando um objeto
novo_repo = ManipulaRpositorios('MathGatto')


# Criando um repositório
nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)


# Adicionando arquivos salvos no repositório criado
novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv', 'Adicionando os dados da empresa Amazon')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv', 'Adicionando os dados da empresa Netflix')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv', 'Adicionando os dados da empresa Spotify')
novo_repo.add_arquivo(nome_repo, 'linguagens_apple.csv', 'dados/linguagens_apple.csv', 'Adicionando os dados da empresa Apple')