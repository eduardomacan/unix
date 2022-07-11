## bg

Põe em background um processo em execução.
Sintaxe: bg [%id]

Utilização: Comando interno da shell. Quando um processo está
ocupando o terminal e digitamos *Z (CTRL-Z) o processo
recebe um sinal SIGSTOP e a shell interrompe a execução
do mesmo. bgiirá colocar o processo interrompido no modo
de execução em background (em segundo plano) e o
processo poderá continuar sua execução.

Parâmetro Descrição

 

id Nocasodehaver vários processos interrompidos,
indica qual processo será colocado em
background.

24
 

Obs: O identificador (id) do processo será indicado pela shell
assim que executarmos um comando em modo background
(com'&') ouinterrompermos um processo pressionando?Z.
Uma lista dos processos pode ser obtida com o comando
jobs. Um processo em background geralmente pode escrever
sua saída no terminal (isso pode ser desabilitado com stty)
e interromperá sua execução se precisar ler dados da
entrada padrão (stdin).

Exemplo:

fsequência exemplo de comandos... respostas

tda shell em itálico
find / -print

SZ
{1]+ Stopped find / -print
bg %1 ¢

Elja = find /--print

