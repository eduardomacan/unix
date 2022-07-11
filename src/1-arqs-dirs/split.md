## split

Divide um arquivo em várias partes.

tail

tar

16

Sintaxe: split [-I nl] [-a suf] [arquivo [prefixo]]
split -b n[k|m] [-a suf] [arquivo [prefixo]

Parâmetro

Descrição


-a suf

-b n[k|m]

-Inl

prefixo

Especifica o numero de letras a serem usadas
para compor o sufixo; default=2.

Especifica o número de bytes de cada parteaser
quebrada; os modificadores k (Kilobytes) e m
(Megabytes) são válidos.

Especifica o número de linhas a serem usadas
para quebrar um arquivo. Só faz sentido com
arquivos texto; default= 1000.

Especifica o prefixo a ser usado no nome de
cada parte do arquivo original; default=x.

Obs: As opções -b e -| são mutuamente exclusivas.

Exemplo:

split -b1400k browser. tgz brow
Quebra o arquivo browser.tgz em vários blocos de aprox. 1.4Mb.

