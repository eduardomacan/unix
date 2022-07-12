## tr

Substitui caracteres de entrada presentes em str1 por seus
correspondentes em str2.

Sintaxe: 

	tr [-cds] [strf [str2]]

Parâmetro Descrição
--------- ---------
-c        Efetua a troca em todos os caracteres que não
          estejam especificados em str1 (complemento).
-d        Elimina ocorrências de caracteres de str1 na
          entrada.
-s        Elimina repetições de caracteres de str2 na
          saída.

Exemplo:

	# Mostra o nome de todos os arquivos do diretório corrente em maiúsculas.

	ls | tr 'a-z' 'A-Z'


