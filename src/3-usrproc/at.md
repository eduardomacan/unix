## at
Executa comandos em outra hora.
Sintaxe: at [-m] [-f script] hora [data] [+ incr]

Parâmetro Descrição

hora Pode ter os seguintes formatos (h=horas
m=minutos):hh:mmouhhmm. Os valoresnoon,
midnighte now são válidos.

data Umnome de mês (Jan, Feb, ... Dec) seguido de
um dia e, possivelmente, um ano precedido por
vírgula. Os valores today e tomorrow são
válidos.

+ incr Um número seguido de uma das seguintes
palavras: minutes, hours, days, weeks, months
ou years (ou singular). O modificador next pode
aparecer antes do incremento (equivale a + 1).

-fscript Lê os comandos do arquivo script a serem
executados.

-l[jobs] Lista os jobs pendentes na fila do at. Se uma
lista de identificadores de jobs (job ids) for
passada como parâmetro, listará apenas o status
daqueles jobs. Essa opção inexiste em alguns
sistemas; para estes casos, use o comandoatq.

-m Envia e-mail avisando que o comando foi
executado.

-rjobs Remove todos os jobs especificados pela lista
de job ids (jobs). Alguns sistemas não
implementam essa opção; para estes casos,
utilize o comando atrm.

Obs: Caso não seja fornecido um arquivo com os comandos a
serem executados, at lerá os comandos da entrada padrão

(stdin) até encontrar o caractere de fim de arquivo (EOF).

Exemplos:
at -m now + 1 week
at -mf comandos now + 3 days
at 18:30 Jan 24


