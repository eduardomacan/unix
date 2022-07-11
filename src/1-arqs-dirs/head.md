## head

Mostra as primeiras linhas de arquivos.

Sintaxe: 

	head [-c n | -n n |-b 1 ] [-f] [arquivo ...]

Parâmetro Descrição
--------- ---------
-b n      Mostra os últimos n blocos do arquivo.
-c n      Mostra os últimos n caracteres do arquivo.
-f        Faz com quehead não pare detentar ler, mesmo
          encontrando o fim do arquivo, assumindo que o
          mesmo está crescendo.
-n n      Mostra as últimas n linhas do arquivo.
-#[b|c|l] Onde # é o numero de linhas (default), caracteres
          ou blocos a serem mostrados. Disponivel em
          algumas versões.

Exemplo:

	# Mostra as primeiras linhas do arquivo mydecls.h..
	head mydecls.h

