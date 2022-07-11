## find
Percorre os diretórios (e seus subdiretórios) especificados mostrando

os arquivos com as características desejadas.

Sintaxe: find <diretório> [diretório ...] [expressão]

 

Parâmetro Descrição
expressão As seguintes primitivas podem ser

combinadas para definirexpressão.

-atimen Verdadeiro se o arquivo tiver sido
acessado há n dias.

-ctime n Verdadeiro se o arquivo tiver sido mudado
há n dias.

-execc; Verdadeiro se o comando c retornar zero
após sua execução.

-fstypex Verdadeiro se o arquivo residir em um
sistema de arquivos do tipo x.

-group x Verdadeiro se o arquivo pertencer ao
grupo x.

-inumn Verdadeiro se o número do i-node do
arquivo for igual a n.

-linksn Verdadeiro se houvern links parao arquivo.

-mtimen Verdadeiro se o arquivo tiver sido
modificado há n dias.

-okc; Similar a -exec, porém pedindo
confirmação prévia.

-name x Verdadeiro se x coincidir com o nome do
arquivo corrente.

-newer x Verdadeiro se o arquivo tiver sido
modificado mais recentemente do que o
arquivo x.

-nouser Verdadeiro se o arquivo corrente não

pertencer a nenhum usuário listado no
arquivo/etc/passwd.

-nogroup Verdadeiro se o arquivo corrente nao
pertencer a nenhum grupo listado no
arquivo/etc/group.

-perm [-|modo Verdadeiro se coincidirem as permissões
do arquivo e modo. Se precedido por -,
apenas os bits ligados de modo serão

comparados.

-print Sempre verdadeiro. Imprime o nome do
arquivo corrente.

-prune Não entra em subdiretórios.

-size n[c] Verdadeiro se o tamanho do arquivo for

de n blocos. Se seguido pela letra c, o
tamanho será interpretado em bytes.
-typet Verdadeiro se o tipo do arquivo
corresponder a t, onde t é um entre:
b Block device.
Character device.
Diretório.
Link.
Arquivos comuns (plain files).
FIFO.
Socket.

-user x Verdadeiro se o arquivo pertencer ao
usuário x.

(exp) Verdadeiro se a expressão entre
parênteses for verdadeira. Os parênteses
serão interpretados pela shell se não
forem precedidos por.

operadores Pode-se combinar diversas expressões
usando os seguintes operadores (emordem
decrescente de precedéncia)

!exp Operador de negação (o caractere. ! é
interpretado pela shell e deve ser
precedido por).

exp-andexp Operador 'E' lógico. Retorna verdadeiro
se ambas as expressões forem
verdadeiras.

Us DT O

10
exp -a exp Algumas versões de find usam -a no
lugar de -and.
exp-orexp  Operador'OU'lógico. Retorna verdadeiro
se pelo menos uma das duas expressões
for verdadeira.
exp -0 exp Algumas versões de find usam -o no
lugar de -or.
Exemplos:
find -macan 1! -name “*.c" -print
Lista todos os arquivos no diretório HOME do usuário macan que
não têm extensão .c.
find - -perm -100 -print
Lista todos os arquivos no diretório HOME que têm permissão de
execução pelo proprietário.



