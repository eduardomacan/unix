## xargs
Constrói e executa linhas de comando a partir de stdin.
xargs [-pt] [-e [str }] [-i [str ]] 1 [n]] [-n n]


Sintaxe:

Exemplos:

find .

find .

Parâmetro
+t

-e str

-i str

-x
comando

arg

[-s n] [comando [arg ...]]
Descrição

Modo detalhado. Imprime a linha de comando
em stderr antes de executá-la.

Usa str como string de fim de arquivo. Ignora
toda a entrada que vier após uma linha contendo
str.

Substitui ocorrências de str nos argumentos
iniciais (veja args) por nomes lidos de stdin.
Usa no máximo n linhas de texto por linha de
comando; default=1.

Usa no máximo n argumentos por linha de
comando.

Modo interativo; pede confirmação antes de
executar cada linha de comando.

Usa no máximo n caracteres por linha de
comando. O defaulté o maior possível, variando
de sistema para sistema.

Termina se o tamanho máximo da linha de
comando (veja -s) for excedido.

O comando a ser executado em cada linha de
comando montada.

Argumento inicial a ser informado ao comando.

-name N*. txt | xargs -pn 2 compress

Comprime todos os arquivos com extensão txt abaixo do diretório
corrente, pedindo confirmação, dois arquivos de cada vez.

| xargs -pn 1 -e gif compress -v

Comprime arquivos um a um até encontrar a string gif em um nome
de arquivo ou diretório (saida de find) e encerra a leitura de stdin.


