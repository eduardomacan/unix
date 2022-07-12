## uuencode

Converte arquivos binários em um equivalente ASCII, o qual poderá ser
utilizado para transmissão via e-mail.

Sintaxe:

	uuencode [arquivo] <nome>

Parâmetro Descrição
--------- ---------
arquivo   Arquivo de entrada. Se omitido, os dados serão
          lidos da entrada padrão (stdin).
nome      O nome que o arquivo terá ao ser decodificado.

Obs: Apenas as permissões de leitura e escrita serão preservadas
no arquivo decodificado.uencodegera arquivos, em média,
35% maiores do que seus originais binários. Veja também
uudecode.

Exemplos:

	uuencode Livro.tar.gz livro.tgz | mail editor

	uuencode forest.gif trees.gif > image.uu

