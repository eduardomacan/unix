## date
Mostra a data e a hora atuais do sistema, com a possibilidade de

formatação
Sintaxe:

da saída.
date [-u] [+formato]

Parâmetro Descrição

 

-u Universal time. Mostra o horário GMT.
+formato formato é uma string que contém informações
sobre a formatação da saída do comando date.
Os seguintes operandos especiais serão
substituídos por seus valores correspondentes
quando encontrados dentro da string formato:
Y%n Caractere newline (quebra de linha).
St Caractere de tabulação (TAB).
Y%m Mês do ano (01 a 12).
%od Dia do més (01 a 31).
%y Últimos dígitos do ano (00 a 99).
%D Data no formato MM/DD/AA.
Y%H Hora (00 a 23).
%M Minuto (00 a 59).
%sS Segundo (00 a 59).

31
Y%T Hora no formato HH:MM:SS.

ij Dia do ano (001 a 366).

ow Dia da semana (Dom=0 a Sáb=6).

‘ha Dia da semana abreviado (Sun ... Sat).
Y%h Mês abreviado (Jan, Feb,... Nov,Dec).
%r Hora no formato am/pm.

Exemplos:
date +"Agora são %H horas e %M minutos$n"
date +'\ Hoje 6 %d/%m/%y \'
date +"\\ Hoje 6 %d/%tm/%y \\"


