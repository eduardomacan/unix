## ps (BSD)

Mostra informações sobre os processos ativos.

Sintaxe:

	ps [-aCejlSuvwxp] [-txx] pids

Obs: Se invocado sem parâmetros, ps mostrará informações
suscintas sobre os processos associados ao terminal de
controle. Esta seção cobre os parâmetros válidos para os
vários sistemas que adotam a versão Berkeley do comando
ps.

Parâmetro Descrição
--------- ---------
-a        Mostra também informações de processos de
          outros usuários.
-C        Mostra o consumo da CPU, ignorando-se o
          “resident time”.
-e        Mostra também variáveis do ambiente
          (environment) em que o processo estiver sendo
          executado.
-j        Mostra informações associadas ao sistema de
          job control.
-l        Mostra a saída no formato longo.
-S        Muda o modo através do qual o tempo do
          processo é calculado, somando-se o tempo dos
          processosfilhos que já terminaram sua execução.
-u        Mostra o nome do usuário e hora do início do
          processo.
-v        Mostra informações associadas ao uso da
          memória virtual pelo processo.
-w        Não trunca as linhas para que caibam no terminal.
-x        Mostra também os processos não associados a
          um terminal de controle.
-p pid    Mostra o processo cujo número é dado por pid.
-t xx     Mostra todos os processo associados ao terminal
          especificado por xx.

Exemplo:

	ps -aux | grep macan

