## ruptime
Mostra o status de cada máquina da rede local, obtendo seus dados de
pacotes difundidos pelas máquinas de tempos em tempos (geralmente
entre 1 e 3 minutos).

Sintaxe: 

	ruptime [-alrtu]

Parâmetro Descrição
--------- ---------
-a        Conta até mesmo os usuários que estejam
          inativos há mais de uma hora.
-l        Ordena a saída pela carga média de cada host.
-r        Inverte a ordenação da saída.
-t        Ordena a saída por tempo de atividade do sistema
          (uptime).
-u        Ordena a saida pelo numero de usuarios.

Obs: Uma máquina é considerada inativa (down) quando a mesma
não difunde informações sobre seu estado há algum tempo
(geralmente entre 5 e 11 minutos, dependendo do sistema
utilizado).

Exemplo:

	ruptime -1

