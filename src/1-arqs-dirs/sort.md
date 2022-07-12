## sort

Ordena linhas de arquivos.

Sintaxe: 

	sort [+p1 [-p2]] [-k p1[,p2]] [-bedfimMnru]
		[-o arq] [-te] [Tdir] [arquivo ...]

Parâmetro  Descrição
---------  ---------
+p1 [-p2]  Especifica a posição da chave de ordenação nas
           linhas do arquivo, entre p1 e p2. Conta a partir de
           0.
-b         Ignora brancos (espaços e newlines) antes das
           chaves de ordenação.
-c         Verifica se os arquivos ja estao ordenados; nao
           ordena.
-d         Considera apenas letras e digitos como parte
           das chaves de ordenacao.
-f         Converte letras minúsculas em maiúsculas antes
           de efetuar as comparações.
-i         Considera parte das chaves apenas os
           caracteres visíveis num terminal.
-k p1[,p2] Similar a +p1 [-p2], porém campos e caracteres
           contam a partir de 1.
-m         Mescla (merge) arquivos já ordenados; não
           efetua ordenação.
-M         Ordena usando uma string como, por exemplo,
           nome de mês; implica -b.
-n         Ordena usando o valor numérico da string; implica
           -b.
-o arg     Escreve sua saída no arquivo arq em vez de
           stdout.
-r         Reverte a ordenação.
-tc        Use c como separador de campos.
           Default=espaços e newlines.
-T *dir*   Armazena arquivos temporários no diretório dir.
-u         Elimina linhas com campos repetidos. Em
           conjunto com -m.

Obs: p1 e p2 têm a sintaxe f.c, onde f representa um campo e c um
caractere contado a partir do início do campo (para +p) ou do
fim do campo (para -p).

Exemplos:

	# Ordena o conteúdo de arquivo, usando o segundo campo (palavra,
	# no sentido de texto) como chave de ordenação.
	sort -k 2,2 arquivo

	# Ordena o arquivo arq e armazena a saida em arg.ord.
	sort arq -ro arq.ord

	# Mostra o arquivo local de senhas ordenado por user id (o terceiro
	# campo separado por dois pontos).
	cat /etc/passwd|sort -nt: -k 3,3



