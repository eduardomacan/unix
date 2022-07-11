## grep
Encontra ocorrências de um padrão dentro de arquivos.
Sintaxe: grep [-cilnsv] <padrão> [arquivo ...]

Parâmetro Descrição

 

-C Mostra apenas o número de linhas que contêm
o padrão.

-i Não diferencia letras maiúsculas de minúsculas.

-l Mostra apenas os nomes dos arquivos que
contêm o padrão.

-n Mostra cada linha que contém o padrao
precedida por seu numero dentro do arquivo.
-s Não mostra mensagens de erro produzidas por
tentativas de acesso a arquivos.
“vv Mostra apenas as linhas que nao contém o
padrão especificado.
Obs: Recomenda-se quepadrão apareça entre aspas simples ('),

pois alguns caracteres (notadamente$,*,[," | ,(,)e\)tém
significado especial para a shell e podem ser interpretados
erroneamente.

Exemplos:
grep -ci 'Mauro' /etc/passwd
Mostra o número de usuários locais que se chamam "Mauro".

grep -l 'Ma&ccedil;an' html/*
Mostra os arquivos no diretório html que contêm a string Maçan
(em HTML).


