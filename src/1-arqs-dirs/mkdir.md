## mkdir

Cria diretórios.

Sintaxe: 

	mkdir [-p] <diretório> [diretório ...]

Parâmetro Descrição
--------- ---------
-p        Cria os diretórios intemediários do path se
          necessário.

Exemplos:

	# Cria o diretório livro e componentes 
	# intermediários do path se necessário.
	mkdir -p ./pub/docs/livro

	# Cria vários diretórios.
	mkdir dirl ../dir2 /usr/local/src/dir3

