## compress

Comprime arquivos aplicando a codificação adaptativa de Lempel-Ziv.
O arquivo comprimido terá a extensão .Z.

Sintaxe: compress [-cvf] [-b bits] <arquivo> [arquivo ...]

Parâmetro Descrição

 

-b bits Define o tamanho (em bits) das substrings usadas
no processo de compressão (9a 16, default=16).

-c Comprime para a saída padrão (stdout), sem
alterar arquivos.

-f Comprime sem considerar se o tamanho do

arquivo vai ser realmente reduzido. Sobrescreve
arquivos com o mesmo nome.

V Mostra estatísticas de compressão na saída de
erro padrao (stderr) .

Exemplo:

compress -v *.txt
Comprime todos os arquivos com extensão txt.


