## tar

Armazena vários arquivos e diretórios dentro de um único arquivo ou

dispositivo.

Sintaxe: tar [txcrumphvw] [f arq] [-b bIk] [-C dir] [arquivo ...]

Parâmetro
-C dir

-b blk
-c

-f arq
-h

-m

Pp

v

t
-u

Descrição

Muda o diretório de trabalho para o diretório dir.
Pode aparecer mais de uma vez entre nomes de
arquivos.

Especifica o tamanho do bloco de dados.

Cria um novo arquivo tar.

Usa o arquivo ou dispositivo arq para
armazenamento ou recuperação.

Armazena cópia dos arquivos aos quais foi feita
referência em vez de armazenar cópia dos links.
Não extrai a data de modificação dos arquivos
armazenados.

Extrai as permissões de acesso originais dos
arquivos.

Inclui arquivos ao final (append) de um arquivo tar.
Lista o conteúdo de um arquivo tar.

Inclui somente (append) arquivos que não
estejam presentes, ou que sejam mais novos do
que o arquivo tar.
V Lista arquivos processados.

-w Solicita confirmação antes de cada ação.
=X Extrai arquivos armazenados em um arquivo tar.
Obs: Os parâmetros podem ser agrupados logo após o comando,

(não necessariamente precedidos por - ). Nesse caso,
quaisquer valores associados devem ser informados na
mesma ordem que os parâmetros correspondentes. Compare
os quatro últimos exemplos.

Exemplos:
tar cvf files.tar -C /etc arql -C /usr arq2
Cria o arquivo files.tar, muda para 0 diretorio /etc e inclui o arquivo
arq1 em files.tar, muda para o diretório lusr e inclui o arquivo
arg2, bem como imprime os nomes dos arquivos em stdout.

tar cvfb images.tar 512 *.gif

tar cvf images.tar: -b 512. *.gif

tar -cv -f images.tar -b 512 *.gif

tar -c -v -f images.tar -b 512 *.gif
Todos os exemplos acima incluem todos os arquivos com
extensão .gif no arquivo images.tar, com blocagem de 512 bytes.



