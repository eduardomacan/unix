## sort

Ordena linhas de arquivos.
Sintaxe: sort [+p1 [-p2]] [-k p1[,p2]] [-bedfimMnru]
[-o arq] [-te] [Tdir] [arquivo ...]
Parâmetro Descrição

+p1 [-p2] Especifica a posição da chave de ordenação nas
linhas do arquivo, entre p1 e p2. Conta a partirde

0.

-b Ignora brancos (espaços e newlines) antes das
chaves de ordenação.

a -c Verifica se os arquivos ja estao ordenados; nao

ordena.

-d Considera apenas letras e digitos como parte
das chaves de ordenacao.

-f Converte letras minúsculas em maiúsculas antes

de efetuar as comparações.

-i Considera parte das chaves apenas os
caracteres visíveis num terminal.

-k p1[,p2] Similar a +p1 [-p2], porém campos e caracteres
contam a partir de 1.

-m Mescla (merge) arquivos já ordenados; não
efetua ordenação.

-M Ordena usando uma string como, por exemplo,
nome de mês; implica -b.

-n Ordena usando o valor numérico da string; implica
-b.

-o arg Escreve sua saída no arquivo arq em vez de
stdout.

Tr Reverte a ordenação.

«tc Use c como separador de campos.
Default=espaços e newlines.

-T dir Armazena arquivos temporários no diretório dir.

-u Elimina linhas com campos repetidos. Em
conjunto com -m.

Obs: pfep2têmasintaxef.c, ondefrepresenta um campo e cum

caractere contado a partir do início do campo (para +p) ou do
fim do campo (para -p).
Exemplos:
sort -k 2,2 arquivo
Ordena o conteúdo de arquivo, usando o segundo campo (palavra,
no sentido de texto) como chave de ordenação.

sort arq -ro arq. brd
Ordena o arquivo arq e armazena a saida em arg.ord.

cat /etc/passwd|sort -nt: -k 3,3
Mostra o arquivo local de senhas ordenado por user id (o terceiro
ç campo separado por dois pontos).


