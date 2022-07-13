## telnet

Abre um canal de comunicação entre duas máquinas através do protocolo
TELNET.

Sintaxe: 

	telnet [ host [ port] ]

Parâmetro Descrição
--------- ---------
host      Identifica a máquina remota com a qual se quer
          estabelecer a conexão.
port      Identifica a porta através da qual se estabelecerá
          a conexão entre as duas máquinas.

Obs: Se não forem fornecidos parâmetros, telnet entrará no modo
de comando interativo. Para alternar para o modo interativo
durante uma sessão usa-se o caractere de escape CTRL-]
(^D).

Comandos:

Comando            Descrição
-------            ---------
open host [ port]  Abre uma conexão com host através da porta
                   especificada.
close              Encerra uma conexão TELNET e retorna ao
                   modo de comando.
quit               Fecha qualquer sessão aberta e termina a
                   execução de telnet. Um EOF (geralmente ^D)
                   no modo de comando tem o mesmo efeito.
z                  Suspende telnet. Este comando só funciona se
                   a shell do usuário implementar mecanismos de
                   controle de processos.
mode modo          Seleciona atransmissão dos dados por caractere
                   ou linha; character ou line, respectivamente.
status             Mostra o estado atual de telnet.
display [arg...]   Mostra o valor de um (ou todos) argumento(s)
                   dos comandos set e toggle (veja adiante).
?[comando]         Mostra informações de ajuda sobre comando.
                   Se invocado sem argumentos, listaos comandos
                   válidos.
![comando]         Invoca uma shelle executacomando caso este
                   tenha sido especificado. Disponível em algumas
                   versões de telnet.
send argumentos    Envia uma sequência especial de caracteres
                   para o host remoto. Os seguintes argumentos
                   podem ser especificados:
escape             Envia o caractere de escape (inicialmente "] ).
synch              Envia a sequência de sincronismo do protocolo
                   TELNET, o host remoto descarta todos os
                   caracteres recebidos que ainda não foram
                   interpretados.
brk                Envia a sequência de BRK (break).
ip                 Envia a sequência IP (Interrupt Process), que
                   faz com que o host remoto interrompa a
                   execução do processo que estiver sendo
                   executado.
ao                 Envia a sequência AO (Abort Output), que faz
                   o host remoto descartar toda a saída do host
                   remoto para o terminal do usuário.
ayt                Envia a sequência AYT (Are You There?) para
                   o host remoto, que pode escolher responder
                   ou não.
ec                 Envia a sequência EC (Erase Character), que
                   faz com que o host remoto cancele o último
                   caractere recebido.
el                 Envia a sequência EL (Erase Line), que faz
                   com que o host remoto descarte a linha que
                   estiver sendo digitada.
ga                 Envia a sequência GA (GO AHEAD). Sem
                   significado para o host remoto.
nop                Envia a sequência NOP (No Operation).
?                  Mostra informações sobre o comando send.
set variável valor Ajusta o valor de uma ou mais variáveis telnet.
                   Os valores especiaison e off ligam ou desligam
                   a função associada a uma variável (veja toggle
                   abaixo).
echo               Caractere para ligar ou desligar o eco local
                   dos caracteres digitados (Inicialmente ^E).
escape             Caractere de escape para o modo de comando
                   (inicialmente ^] ).
interrupt          Caractere para provocar interrupção do
                   processo remoto. O default dependerá da
                   configuração do terminal (veja stty).
quit               Caractere para provocar aborto de processo.
                   O default dependerá da configuração do
                   terminal (veja stty).
flushoutput        Caractere para provocar um Abort Output.
erase              Caractere usado para eliminar um caractere.
                   O valor default dependerá da configuração do
                   terminal (veja stty).
kill               Caractere usado para cancelar a entrada de
                   uma linha. O default dependerá da
                   configuração do terminal (veja stty).
eof                Caractere para demarcar o fim da entrada. O
                   default dependerá da configuração do terminal
                   (veja stty).
toggle args...     Inverte o valor associado a uma (ou várias)
                   variável(eis) booleana(s) (veja set acima).
localchars         Liga/desliga o reconhecimento local de certos
                   caracteres de controle.
autoflush          Liga/desliga o descarte da saída quando
                   enviando caracteres de interrupção.
autosynch          Liga/desliga o envio automático de caracteres
                   de interrupção no modo "urgente" de
                   transmissão.
crmod              Liga/desligao mapeamento local de caracteres
                   de retorno de carro (CR) recebidos.
options            Liga/desliga a visualização do processamento
                   de opções (debugging).
netdata            Liga/desliga a impressão em hexadecimal de
                   dados provenientes da rede (debugging).
?                  Mostra informações sobre o comandotoggle.

Exemplo:

	telnet localhost

