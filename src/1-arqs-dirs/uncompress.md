## uncompress

Descompacta arquivos compactados porcompress, restaurando seus
nomes originais.

Sintaxe:

	uncompress [-cv] [arquivo ...]

Parâmetro Descrição
--------- ---------
-c        Descompacta direcionando a saída para a saída
          padrão (stdout), sem alterar arquivos.
-v        Imprime suas ações na saída de erro padrão
          (stderr).

Exemplo:

	# Descomprime os arquivos comprimidos no 
	# exemplo do comando compress.

	uncompress -v \*.txt.Z

