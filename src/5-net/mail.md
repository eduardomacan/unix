## mail

Sistema de processamento de correspondência eletrônica.

Sintaxe: 

	mail [-ilnv] [-s ass] [-c lista] [-b lista] end...

	mail [-ilnNv] -f [nome]

	mail [-ilnNv] [-u user]

Parâmetro Descrição
--------- ---------
-v        Modo detalhado (verbose). Os detalhes da
          entrega de mail serão mostrados no terminal do
          usuário.
-i        Ignora sinais de interrupção do terminal. Útilem
          linhas com ruido.
-l        Força o modo interativo mesmo quando a entrada
          não for o terminal.
-n        Inibe a leitura do arquivo de inicialização global
          do sistema de mail.
-N        Inibe a exibição inicial dos cabeçalhos das
          mensagens.
-s ass    Especifica o assunto (subject) em linha de
          comando. Apenas o argumento seguinte à opção
          -S será considerado. Assuntos contendo espaços
          deverão aparecer entre aspas.
-c lista  Envia uma copia da mensagem para os
          endereços especificados em lista.
-b lista  Envia uma cópia da mensagem para os
          endereços especificados em lista, sem que os
          outros destinatários saibam.
-f[nome]  Lê o conteúdo do arquivo nome para
          processamento (ou de mbox, caso nenhum
          nome de arquivo tenha sido especificado).
-u nome   Lê o mailbox do usuário especificado por nome.

Utilização: Se invocado sem parâmetros, mail irá mostrar o conteúdo
do mailbox e esperar por comandos do usuário, que podem
ser:

Comando Descrição
------- ---------
?       Lista os comandos disponíveis de forma suscinta.
! cmd   Abre uma shell e executa o comando cmd.
R       Reply. Responde ao remetente da mensagem
        corrente.
a[args] Sem argumentos, mostra todos os aliases
        definidos; com um argumento, mostra apenas
        um alias; com mais de um argumento, define o
        alias com o nome dado pelo primeiro argumento.
c [dir] Muda o diretório corrente para aquele
        especificado pordir ou para o diretório HOME do
        usuário caso não haja argumentos.
d[msgs] Marca as mensagens cujos identificadores
        estejam na lista msgs para eliminação. Se
        nenhuma mensagem tiver sido especificada, a
        mensagem corrente será marcada.
e[msgs] Edita todas as mensagens dadas por msgs,
        passando uma a uma para o editor.
x       Sai abandonando alteragées feitas no mailbox
        ou no arquivo que estiver sendo processado.
m addr  Envia mail para todos os enderegos especificados
        na lista addr.
n       Passa para a próxima mensagem; equivale a "+"
        ou CR (carriage return).
q       Termina a execução do programa e efetiva todas
        as alterações feitas pelo usuário (eliminando
        mensagens marcadas, etc.).
r       Reply. Envia mensagem ao remetente e demais
        destinatários de uma mensagem.
s list file Toma uma lista de mensagens e as concatena
        ao arquivo cujo nome seja o dado por file, na
        ordem especificada.
sh      Invoca uma shell interativa.
u       Undelete. Remove a marca de eliminação de
        uma mensagem.
w list file Idem a s, exceto pelo fato dos cabeçalhos das
        mensagens serem ignorados.
z       Avança uma página na lista de mensagens.
z-      Retrocede uma pagina na lista de mensagens.
Edição  Quando usamos os comandosm, rou R, ou especificamos
        um destinatário em linha de comando, entramos no modo de
        edição de mensagens. Aqui utilizamos os chamados "tilde
        escapes”, comandos especiais que devem ser digitados no
        início de uma linha para serem reconhecidos. Se o caractere
        “=" for necessário no início da linha da mensagem, este deve
        ser digitado duas vezes.
~!cmd   Abre uma shell e executa o comando cmd,
        retornando à mensagem em edição.
~cnomes Acrescenta os nomes da lista nomes à lista de
        receptores das cópias da mensagem.
~d      Insere o arquivo dead.letter na mensagem
        corrente.
~e      Invoca o editor de textos e edita a mensagem que
        estiver sendo composta. Ao final da edição pode-se
        continuar acrescentando texto à mensagem.
~f msgs Insere as mensagens especificadas na
        mensagem em edição.
~h      Edita os campos do cabeçalho (header) da
        mensagem.
~m msgs Insere as mensagens da listamsgs endentadas
        na mensagem em edição.
~q      Aborta a mensagem em edição, guardando seu
        conteúdo no arquivo dead.letter.
~r file  Insere o arquivo file na mensagem em edição.
~s string Muda o assunto (subject) da mensagem para
         string.
-w nome  Grava o conteúdo da mensagem em edição no
         arquivo nome.
~|cmd    Passa a mensagem em edição para o programa
         cmd através de um pipe.

Obs: Dentre todas as ferramentas que compõe um sistema UNIX,
os agentes de mail são, sem dúvida, os mais populares eos
que apresentam maior variedade de implementação. O
agente documentado aqui é o popular mailx, presente na
maioria dos sistemas, tiver sido escolhido pela generalidade
almejada por este guia. As listas de mensagens requeridas
por alguns comandos são listas de números ou intervalos
separados por vírgulas. Intervalos têm a forma X-Y (leia de
X a Y).

Exemplos:

	cat arq1.txt arq2.txt | mail -s textos macan

	mail macan -c wada, tulio, mauronr -b flexa

	mail -s "falha no backup" root


