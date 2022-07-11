## lpr
Envia arquivos para a fila de impressão.
Sintaxe: Ip [-c] [-d dest] [-n& ] [arquivo ...]
Parâmetro Descrição

-c Envia cópias dos arquivos para a fila de impressão.
Modificações feitas nos arquivos durante aimpressão
não se refletirão no resultado impresso.

-d dest Envia um arquivo para impressão na impressora
cujo nome seja dest.

-n# Imprime # copias de cada arquivo.

Exemplo:
lp -dlaserl readme.txt install.txt

