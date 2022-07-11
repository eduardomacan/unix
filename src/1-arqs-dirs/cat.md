## cat

Concatena e mostra arquivos.

Sintaxe: 
	cat [-etuv] [arquivo ...]

Parâmetro    Descrição
---------    ---------
-e           Similar a -v, mas imprime um cifrão ($) ao final
             de cada linha. Ignorado em alguns sistemas se
             não usado com -v.
-t           Similar a -v, mas imprime caracteres de tabulação
             (tabs) como ^I. Ignorado em alguns sistemas se
             não usado com -v.
-u           Processa a saída caractere a caractere, em vez
             de utilizar o buffer.
-v           Imprime caracteres especiais de forma visivel
             (tabs e newlines sao processados).

Exemplos

	# Copia stdin para o arquivo texto.txt
	cat > texto.txt

	# Cria o arquivo capitulo 1 como resultado da
	# concatenação de texto1 e texto2.
	cat texto1 texto2 > capitulo1

	# Cria o arquivo arq3, como resultado da 
	# concatenação de arq1, stdin e arq2.
	cat arq1 - arg2 > arq3

