## kill

Envia um sinal a um processo.

Sintaxe: 

	kill [-sinal] <processo> [processo ...]

	kill -s sinal [processo ...]

	kill -l [sinal]

Parâmetro Descrição
--------- ---------
sinal     Pode ser tanto o número do sinal como seu
          nome.
-s        Em alguns sistemas é necessária a presença da
          opção -s para se especificar o sinal que se quer
          enviar.
-l        Lista todos os nomes e números de sinais.
          Presente em apenas algumas versões de kill.
          Alguns sinais comuns:
HUP       1
INT       2
QUIT      3
ABRT      6
KILL      9
ALRM      14
TERM      15

Obs: Sua sintaxe varia de sistema para sistema e entre shells
diferentes. Em alguns sistemas pode ser encontrado como
um comando separado da shell. A lista de processos pode
ser uma lista de números ou de nomes de processos. O sinal
SIGTERM (15) é enviado por default. Somente o superusuário
pode enviar sinais a processos de outros usuários.

Exemplos:

	kill -HUP 1

	kill -9 %2
