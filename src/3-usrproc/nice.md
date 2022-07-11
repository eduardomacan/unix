## nice

Faz com que um processo seja executado com uma prioridade de
escalonamento diferente da padrão.

Sintaxe:

Obs:

Exemplo:

nice

nice [-#] <comando> [args]

Parâmetro Descrição

 

-# Valor a ser adicionado à prioridade do processo
que será executado. Quanto maior este valor,
MENOR será a prioridade de escalonamento do
processo. Em alguns sistemas este valor
representa o valor absoluto da prioridade.

comando Ocomandoaserexecutado com uma prioridade
diferente.

args Os argumentos do comando a ser executado.

Os valores padrão de nice e as prioridades limites variam
entre as várias versões do Unix, portanto convém consultar
os manuais do sistema para a obtenção dos valores corretos.
O nome nice vem do fato de alguém estar sendo "bacana"
com os outros usuários do sistema, baixando a prioridade de
um processo. Apenas o super-usuário pode aumentar a
prioridade de escalonamento (especificando valores
negativos de nice).

-4 find / -name readme.txt -print



