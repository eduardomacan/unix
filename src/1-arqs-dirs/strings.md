## strings

Encontra texto em arquivo binários.

Sintaxe: 

	strings [-ao] [arquivo ...]

Parâmetro Descrição
--------- ---------
-a        Procura strings ao longo de toda a extensão do
          arquivo e não somente nos segmentos de texto
          e dados dos arquivos objeto.
-o        Imprime o offset de cada string dentro do arquivo.

Exemplo:

	strings /usr/lib/libc.a

