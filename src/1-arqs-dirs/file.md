## file

Determina o tipo dos arquivos examinando seu conteúdo.

Sintaxe:

	file [-cLz] [-m arq] [-f arq] [arquivo ...]


Parâmetro Descrição
--------- ---------
-c        Procura erros no arquivo de números mágicos
          (magic numbers) antes de usá-lo.
-f *arq*  Determina otipodos arquivos listados no arquivo
          *arq*.
-L        Segue links simbólicos.
-m *arq*  Usa o arquivo especificado por *arq* como arquivo
          de números mágicos, em vez de /etc/magic.
-z        Determina o tipo dos arquivos que foram
          comprimidos.

Exemplo:

	# Investiga o tipo do arquivo postscriptfile.ps.
	file postscriptfile.ps

