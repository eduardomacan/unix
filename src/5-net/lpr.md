## lpr

Envia arquivos para afila de impressão remota. Caso nenhuma impressora
seja especificada, Ipr usará a impressora padrão do sistema.

Sintaxe: 

	lpr [-hmrs][-J jobJ[-Pprinter][ -n& ][arquivo ...]

Parâmetro Descrição
--------- ---------
-h        Não imprime a página de identificação da
          impressão.
-m        Envia mail ao final da impressão.
-r        Remove o arquivo após a impressão (com a
          opção -s).
-s        Usa links simbólicos em vez de copiar os arquivos
          para o diretório de spool.
-J job    Nome a ser impresso na página de identificação.
          O nome do primeiro arquivo é o default.
-Pprinter Envia um arquivo para impressão na impressora
          cujo nome seja printer.
-n#       Imprime # cópias de cada arquivo.

Exemplo:

	lpr -Plaser3 -J game readme.txt install.txt


