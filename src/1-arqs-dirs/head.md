## head
Mostra as primeiras linhas de arquivos.
Sintaxe: head [-cn|-nn|-b 1] [-f] [arquivo ...]

Parâmetro Descrição

 

-bn Mostra os últimos n blocos do arquivo.
-cn Mostra os últimos n caracteres do arquivo.
-f Faz com quehead não pare detentar ler, mesmo

encontrando o fim do arquivo, assumindo que o
mesmo está crescendo.

-nn Mostra as últimas n linhas do arquivo.

-#[b|c|l] | Onde#éonumerodelinhas (default), caracteres
ou blocos a serem mostrados. Disponivel em
algumas versões.

Exemplo:

head mydecls.h
Mostra as primeiras linhas do arquivo mydecls.h..

11


