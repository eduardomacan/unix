## tee

Mostra a saída de um programa e a escreve em um arquivo
simultaneamente.

Sintaxe: 

	tee [-ai] [arquivo ...]

Parâmetro Descrição
--------- ---------
-a        Append. Concatena a saída ao arquivo, em vez
          de sobrescrevê-lo.
-i        Ignora interrupções.

Exemplo:

	# Guarda uma cópia de sua seção de ftp em ftp.out.

	ftp ftp.cdrom.com | tee ftp.out

