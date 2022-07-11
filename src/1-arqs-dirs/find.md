## find

Percorre os diretórios (e seus subdiretórios) especificados mostrando
os arquivos com as características desejadas.

Sintaxe: 

	find <diretório> [diretório ...] [expressão]

Parâmetro     Descrição
---------     ---------
expressão     As seguintes primitivas podem ser
              combinadas para definir expressão.
-atime n      Verdadeiro se o arquivo tiver sido
              acessado há n dias.
-ctime n      Verdadeiro se o arquivo tiver sido mudado
              há n dias.
-exec c;      Verdadeiro se o comando c retornar zero
              após sua execução.
-fstype x     Verdadeiro se o arquivo residir em um
              sistema de arquivos do tipo x.
-group x      Verdadeiro se o arquivo pertencer ao
              grupo x.
-inum n       Verdadeiro se o número do i-node do
              arquivo for igual a n.
-links n      Verdadeiro se houver n links para o arquivo.
-mtime n      Verdadeiro se o arquivo tiver sido
              modificado há n dias.
-ok c;        Similar a -exec, porém pedindo
              confirmação prévia.
-name x       Verdadeiro se x coincidir com o nome do
              arquivo corrente.
-newer x      Verdadeiro se o arquivo tiver sido
              modificado mais recentemente do que o
              arquivo x.
-nouser       Verdadeiro se o arquivo corrente não
              pertencer a nenhum usuário listado no
              arquivo /etc/passwd.
-nogroup      Verdadeiro se o arquivo corrente não
              pertencer a nenhum grupo listado no
              arquivo/etc/group.
-perm [-]modo Verdadeiro se coincidirem as permissões
              do arquivo e modo. Se precedido por -,
              apenas os bits ligados de modo serão
              comparados.
-print        Sempre verdadeiro. Imprime o nome do
              arquivo corrente.
-prune        Não entra em subdiretórios.
-size n[c]    Verdadeiro se o tamanho do arquivo for
              de n blocos. Se seguido pela letra c, o
              tamanho será interpretado em bytes.
-type t       Verdadeiro se o tipo do arquivo
              corresponder a t, onde t é um entre:
              **b** Block device.
              **c** Character device.
              **d** Diretório.
              **l** Link.
              **p** Arquivos comuns (plain files).
              **f** FIFO.
              **s** Socket.
-user x       Verdadeiro se o arquivo pertencer ao
              usuário x.
(exp)         Verdadeiro se a expressão entre
              parênteses for verdadeira. Os parênteses
              serão interpretados pela shell se não
              forem precedidos por.
operadores    Pode-se combinar diversas expressões
              usando os seguintes operadores (emordem
              decrescente de precedéncia)
!exp          Operador de negação (o caractere. ! é
              interpretado pela shell e deve ser
              precedido por).
exp -and exp  Operador 'E' lógico. Retorna verdadeiro
              se ambas as expressões forem
              verdadeiras.
exp -a exp    Algumas versões de find usam -a no
              lugar de -and.
exp -or exp   Operador 'OU' lógico. Retorna verdadeiro
              se pelo menos uma das duas expressões
              for verdadeira.
exp -o exp    Algumas versões de find usam -o no
              lugar de -or.

Exemplos:


	# Lista todos os arquivos no diretório HOME do usuário macan que
	# não têm extensão .c.
	find ~macan \! -name “*.c" -print

	# Lista todos os arquivos no diretório HOME que têm permissão de
	# execução pelo proprietário.
	find ~ -perm -100 -print


