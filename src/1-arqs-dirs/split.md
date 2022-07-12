## split

Divide um arquivo em várias partes.

Sintaxe: 

	split [-I nl] [-a suf] [arquivo [prefixo]]
	split -b n[k|m] [-a suf] [arquivo [prefixo]

Parâmetro Descrição
--------- ---------
-a suf    Especifica o numero de letras a serem usadas
          para compor o sufixo; default=2.
-b n[k|m] Especifica o número de bytes de cada parte a ser
          quebrada; os modificadores k (Kilobytes) e 
          m (Megabytes) são válidos.
-l nl     Especifica o número de linhas a serem usadas
          para quebrar um arquivo. Só faz sentido com
          arquivos texto; default= 1000.
prefixo   Especifica o prefixo a ser usado no nome de
          cada parte do arquivo original; default=x.

Obs: As opções -b e -| são mutuamente exclusivas.

Exemplo:

	# Quebra o arquivo browser.tgz em vários blocos de aprox. 1.4Mb.
	split -b1400k browser.tgz brow


