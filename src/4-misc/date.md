## date

Mostra a data e a hora atuais do sistema, com a possibilidade de
formatação da saída.

Sintaxe:

	date [-u] [+formato]

Parâmetro Descrição
--------- ---------
-u        Universal time. Mostra o horário GMT.
+formato  formato é uma string que contém informações
          sobre a formatação da saída do comando date.
          Os seguintes operandos especiais serão
          substituídos por seus valores correspondentes
          quando encontrados dentro da string formato:
%n        Caractere newline (quebra de linha).
%t        Caractere de tabulação (TAB).
%m        Mês do ano (01 a 12).
%d        Dia do més (01 a 31).
%y        Últimos dígitos do ano (00 a 99).
%D        Data no formato MM/DD/AA.
%H        Hora (00 a 23).
%M        Minuto (00 a 59).
%S        Segundo (00 a 59).
%T        Hora no formato HH:MM:SS.
%j        Dia do ano (001 a 366).
%w        Dia da semana (Dom=0 a Sáb=6).
%a        Dia da semana abreviado (Sun ... Sat).
%h        Mês abreviado (Jan, Feb,... Nov,Dec).
%r        Hora no formato am/pm.

Exemplos:

	date +"Agora são %H horas e %M minutos$n"

	date +' Hoje é %d/%m/%y '

	date +"\\ Hoje é %d/%m/%y \\"

