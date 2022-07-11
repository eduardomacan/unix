## paste

Mostra lado a lado o conteúdo de arquivos.

Sintaxe: 

	paste [-d lista] [-s] [arquivo ...]

Parâmetro Descrição
--------- ---------
-d	  lista Usa os caracteres da string lista como 
          separadores em vez de TAB. Quando o último 
          caractere for utilizado, o primeiro será utilizado i
          novamente. Os seguintes caracteres especiais 
          podem ser usados como separadores:
          **\\n** Quebra de linha (newline).
          **\\t** Tabulação (TAB).
          **\\\\** Barra invertida (backslash).
          **\0** String vazia (não o caractere NUL).
-s        Concatena todas as linhas de cada arquivo em separado, na ordem em que foram especificados na linha de comando.
-         Usa stdin como entrada.

Obs: Caso um arquivo seja menor do que os outros, ele será
tratado como se tivesse um número infinito de linhas vazias
após sua última linha.

