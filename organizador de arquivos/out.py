import os 

cwd = os.getcwd()  # Obtém o diretório de trabalho atual

folder_List = []
for i in os.listdir(cwd):  # Itera sobre todos os itens no diretório atual
     if os.path.isdir(i):  # Verifica se o item é um diretório
         folder_List.append(i)  # Adiciona o diretório à lista de pastas
         
for folder in folder_List:  # Itera sobre cada pasta encontrada
    path = os.path.join(cwd, folder)  # Cria o caminho completo para a pasta
    
    files = os.listdir(path)  # Lista todos os arquivos dentro da pasta
    for file in files:  # Itera sobre cada arquivo na pasta
        from_path = os.path.join(path, file)  # Caminho completo do arquivo na pasta
        to_path = os.path.join(cwd, file)  # Caminho para onde o arquivo será movido (diretório principal)
        os.replace(from_path, to_path)  # Move o arquivo para o diretório principal
    os.rmdir(path)  # Remove a pasta vazia após mover todos os arquivos