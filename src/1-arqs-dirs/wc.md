## wc

Conta o número de palavras, linhas ou bytes (caracteres) de um arquivo.

Sintaxe:

	wc [-clw] [arquivo ...]

Parâmetro Descrição
--------- ---------
-c        Mostra onúmero de caracteres (bytes) do arquivo.
-l        Mostra o número de linhas de um arquivo.
-w        Mostra o numero de palavras de um arquivo.

Obs: Por default wc irá imprimir todas as contagens. Palavras são
strings separadas por espaços, TABs ou newlines e linhas
são strings terminadas por newline.

Exemplos:

	wc -l /etc/passwd

	wc -c ./*

