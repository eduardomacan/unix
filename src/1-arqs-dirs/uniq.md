## uniq

Notifica ou filtra a ocorréncia de linhas repetidas adjacentes em um
arquivo texto.

Sintaxe: 

	uniq [-cdu] [-f n] [-s n] [argent [arqsai] ]

Parâmetro Descrição
--------- ---------
-c        Precede cada linha de saída com o número de
          vezes que a mesma ocorreu na entrada.
-d        Mostra apenas as linhas que aparecem repetidas
          na entrada.
-f n      Ignora os n primeiros campos (palavras
          separadas por espaços, tabs ou newlines) na
          comparação entre linhas.
-s n      Ignora os n primeiros caracteres em cada linha
          de entrada. Se usado com -f, os n primeiros
          caracteres após os campos ignorados também
          serão ignorados.
-u        Não mostra as linhas que se repetem na entrada.

Obs: Serão usados argumentos adicionais como, por exemplo, o
nome de um arquivo de entrada e um de saída,
respectivamente.

