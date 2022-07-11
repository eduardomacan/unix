## ls

Lista o conteúdo de diretórios.

Sintaxe:

	ls [-aAcCdfFiLqrRstu1] [arquivo ...]


Parâmetro Descrição
--------- ---------
-a        Inclui entradas do diretório cujos nomes
          comecem com ".", normalmente omitidas.
-A        Lista todas as entradas, exceto "." e "..", esta
          opção é default para o superusuário (root).
-c        Usa a data de modificação do arquivo para a
          ordenação ou impressão.
-C        Formata a saída em múltiplas colunas; default
          quando a saída é o terminal.
-d        Trata diretórios como arquivos comuns e não
          segue links simbólicos.
-f        Não ordena a saída.
-F        Diferencia os tipos de arquivos concatenando
          caracteres a seus nomes:
          **/**    Diretórios.
          **\*** Arquivos executáveis.
          **\@**    Links simbólicos.
          **=**    Sockets.
          **|**    Pipes.
-i        Imprime o número do i-node de cada arquivo.
-l        Lista usando o formato longo.
-L        Se o argumento for um link simbólico, lista o
          arquivo ou diretório referenciado.
-q        Força a impressão de caracteres não gráficos
          nos nomes dos arquivos, como, por exemplo,
          pontos de interrogação (?).
-r        Reverte a ordenação para obter ordem alfabética
          inversa, ou arquivos mais antigos primeiro.
-R        Lista também o conteúdo dos subdiretórios
          abaixo do diretório especificado.
-s        Mostra o número de blocos de disco usados
          pelos arquivos.
-t        Ordena os resultados cronologicamente.
-u        Usa a data do ultimo acesso ao arquivo paraa
          ordenação ou impressão.
-1        Mostra um elemento por linha de saida.

Obs:      O formato longo mostra informações sobre o tipo de arquivo
          e suas permissões de acesso como uma string de dez
          caracteres, onde o primeiro identifica o tipo dos arquivos da
          seguinte forma:

Caractere Tipo
-----     ------------
**b**     Block device.
**e**     Character device.
**d**     Diretório.
**l**     Link.
**p**     FIFO (named pipe).
**s**     Socket da familia AF_UNIX.
**-**     Arquivo comum (plain file).

Os outros nove caracteres referem-se cada um a um bit de
permissão de acesso, os três primeiros às permissões do
proprietário, os três seguintes às permissões do grupo do
arquivo e os últimos às permissões de acesso para outros
grupos. Podem assumir os seguintes valores:

Caractere  Permissão
-----      ----------------
**r**      permissão de leitura.
**w**      permissão de escrita.
**x**      permissão de execução.
**-**      bit de permissão desligado.

Os caracteres de permissão de execução do proprietário e
do grupo serão mostrados como "s" se os bits de setuid e
setgid do arquivo estiverem ligados, respectivamente. O
sticky bit ligado será mostrado como um "t” no lugar do
caractere de permissão de execução para outros grupos. As
letras "S"e"T" maiúsculas serão mostradas no lugar de "s“e
"t" quando o bit de permissão de execução correspondente
não estiver ligado.

Exemplos:

	ls -la /etc/passwd ls /etc
	ls -lad /etc de sla-fero

