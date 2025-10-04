## xargs

Constrói e executa linhas de comando a partir de stdin.

Sintaxe:

	xargs [-pt] [-e [str }] [-i [str ]] 1 [n]] [-n n]
	      [-s n] [comando [arg ...]]


Parâmetro Descrição
--------- ---------
-t        Modo detalhado. Imprime a linha de comando
          em stderr antes de executá-la.
-e str    Usa str como string de fim de arquivo. Ignora
          toda a entrada que vier após uma linha contendo
          str.
-i str    Substitui ocorrências de str nos argumentos
          iniciais (veja args) por nomes lidos de stdin.
-l n      Usa no máximo n linhas de texto por linha de
          comando; default=1.
-n n      Usa no máximo n argumentos por linha de
          comando.
-p        Modo interativo; pede confirmação antes de
          executar cada linha de comando.
-s n      Usa no máximo n caracteres por linha de
          comando. O defaulté o maior possível, variando
          de sistema para sistema.
-x        Termina se o tamanho máximo da linha de
          comando (veja -s) for excedido.
comando   O comando a ser executado em cada linha de
          comando montada.
arg       Argumento inicial a ser informado ao comando.

Exemplos:

	# Comprime todos os arquivos com extensão txt 
      # abaixo do diretório corrente, pedindo confirmação, 
      # dois arquivos de cada vez.

	find . -name N*. txt | xargs -pn 2 compress

	# Comprime arquivos um a um até encontrar a string 
      # gif em um nome de arquivo ou diretório (saida de
      # find) e encerra a leitura de stdin.

	find .| xargs -pn 1 -e gif compress -v

