## diff

Mostra as diferenças entre dois arquivos

	diff [-bcefir] [-D str] [-S arq] <arquivo1> <arquivo2>

Parâmetro Descrição
--------- ---------
-b        Ignora sequências de espaços em branco e
          caracteres de tabulação (TAB).
-c        Produz uma listagem das diferengas usando
          linhas de contexto.
-D str    Produz uma versão mista dos dois arquivos,
          usando controles do pré-processador de C e str
          como macro de controle.
-e        Cria uma sequência de comandos do editor ed
          que permite recriararquivo2a partir doarquivo1.
-f        Produz uma saída similar à opção -e, mas de
          interpretação mais simples.
-         Considera letras maiúsculas e minúsculas
          equivalentes.
-S arq    Inicia a comparação de dois diretórios a partir do
          arquivo arg.
-r        Também processa os subdiretórios quando
          comparando diretórios.

Exemplo:

	diff -f /etc/passwd.old /etc/passwd


