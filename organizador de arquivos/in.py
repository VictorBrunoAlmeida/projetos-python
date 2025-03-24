import os  # Importa o módulo os que fornece funções para interagir com o sistema operacional

cwd = os.getcwd()  # Obtém o diretório de trabalho atual (current working directory)
full_list = os.listdir(cwd)  # Lista todos os itens (arquivos e pastas) no diretório atual


# Iterar sobre a lista para passar somente arquivos para essa lista
files_list = []  # Cria uma lista vazia para armazenar apenas os arquivos
for i in full_list:  # Itera sobre cada item na lista completa
    full_path = os.path.join(cwd, i)  # Constrói o caminho completo para o item
    if os.path.isfile(full_path) and ".py" not in i:  # Verifica se é um arquivo e não é um arquivo Python
        files_list.append(i)  # Adiciona o nome do arquivo à lista de arquivos
        
# Separar arquivo da files_list para o tipo de arquivo
types = []  # Cria uma lista vazia para armazenar os tipos de arquivos (extensões)
for i in files_list:  # Itera sobre cada arquivo na lista de arquivos
    if "." in i:  # Verifica se o nome do arquivo contém um ponto (tem extensão)
        types.append(i.split(".")[1])  # Divide o nome pelo ponto e pega o segundo elemento (extensão)
        
# Remover duplicatas
tipo_unico = set(types)  # Converte a lista de tipos para um conjunto (set) para remover duplicatas

# Criando pastas com os arquivos já selecionados
for file_type in tipo_unico:  # Itera sobre cada tipo de arquivo único
    try:
        os.mkdir(file_type)  # Tenta criar uma pasta com o nome da extensão
    except FileExistsError:
        pass  # Ignora o erro se a pasta já existir (o pass serve para ignorar o erro)
    
for file in files_list:  # Itera sobre cada arquivo na lista de arquivos
    from_path = os.path.join(cwd, file)  # Cria o caminho completo de origem do arquivo
    to_path = os.path.join(cwd, file.split(".")[-1], file)  # Cria o caminho de destino: diretório atual + pasta da extensão + nome do arquivo
    
    os.replace(from_path, to_path)  # Move o arquivo do caminho de origem para o caminho de destino