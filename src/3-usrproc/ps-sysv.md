## ps (SYSV)

Mostra informações sobre os processos ativos.

Sintaxe: 

	ps -[adefl] [-t terms] [-p procs] [-u uids] [-g gids]

Obs: Se invocado sem parâmetros, ps mostrará informações
suscintas sobre os processos associados ao terminal de
controle. Esta seção cobre os parâmetros válidos para os
vários sistemas que adotam a versão System V do comando
ps.

Parâmetro Descrição
--------- ---------
-a        Mostra informações sobre os processos mais
          requisitados; ou seja, todos, menos os líderes de
          grupo de processos e aqueles não associados a
          um terminal.
-d        Mostra informações sobre todos os processos
          exceto líderes de grupo de processos (process
          group leaders).
-e        Mostra informações sobre todos os processos
          em execução no presente momento.
-f        Gera uma listagem completa (full). _
-l        Gera uma listagem no formato longo (long).
-t term   Mostra apenas os processos associados ao
          terminal especificado por term.
-p procs  Mostra apenas os processos cujos números
          (PIDs) estejam presentes na lista procs.
-u uids   Mostra apenas os processos cujos nomes (ou
          números) dos usuários proprietários (owners)
          estejam presentes na lista uids.
-g gids   Mostra apenas-os processos cujos grupos
          estejam presentes na lista uids.


Exemplo:

	ps -efu macan


