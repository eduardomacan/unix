## ftp

Transfere arquivos entre máquinas da rede.

Sintaxe:

	ftp [-ginv] [maquina]

Parâmetro Descrição
--------- ---------
-g        Desabilita o "globbing" dos nomes de arquivos,
          habilitado por default. Veja o comando glob abaixo.
-i        Não pede confirmação antes da transferência de
          múltiplos arquivos. Veja o comandoprompt abaixo.
-n        Desabilita o "auto-login”. Veja o comando open
          abaixo. 
-v        Habilita a saida descritiva. Default se a entrada
          padrão estiver associada a um terminal.

Comandos:

Comando           Descrição
-------           ---------
![cmd [args]]     Invoca uma shell na máquina local e executa o
                  comando cmd.
append loc[rem]   Concatena o arquivo *loc* na máquina local 
                  ao arquivo remoto *rem*.
ascii             Ativa o modo de transferência adequado para a
                  transferência de arquivos texto.
bell              Soa um alarme a cada transferência de arquivo
                  completada.
binary            Ativa o modo de transferência adequado a
                  arquivos binários.
bye               Encerra a sessão como servidor remoto e saido
                  programa ftp. Um caractere EOF (geralmente
                  ^D) tem o mesmo efeito.
case              Converte o nome dos arquivos transferidos para
                  minúsculas.
cd dir            Muda diretório de trabalho na máquina remota
                  para dir.
cdup              Muda para o diretório pai do diretório atual no
                  servidor.
chmod modo arq    Muda o modo de acesso do arquivo remoto arq
                  para aquele especificado por modo.
close             Termina a sessão com o servidor remoto e
                  retorna ao interpretador de comandos.
cr                Liga/desliga a filtragem de caracteres CR durante
                  transferências do tipo ascii. Ativada é o default.
delete arq        Remove o arquivo arq da máquina remota.
dir [dir] [arq]   Mostra o conteúdo do diretório remoto dir,
                  opcionalmente colocando a saída no arquivo
                  local arq.
disconnect        O mesmo que close.
get arq [loc]     Transfere o arquivo arq da máquina remota
                  para a máquina local, renomeando-o para loc
                  caso esse parâmetro seja fornecido.
glob              Liga/desliga a expansão de nomes de arquivos
                  para os comandos mget , mput e mdelete. O
                  default é a expansão de nomes ativada.
hash              Mostra um caractere # (hash) para cada bloco de
                  dados recebido (1Kbyte).
help [cmd]        Mostra uma mensagem informativa sobre o comando
                  cmd. Se nenhum comando for especificado, lista
                  todos os comandos disponiveis.
idle[seg]         Ajusta o relógio de inatividade no servidor remoto
                  para seg segundos. Se seg não for especificado,
                  mostra o valor atual do contador.
lcd [dir]         Muda o diretório de trabalho na máquina local.
                  Se dir não for especificado, o diretório
                  HOME do usuário será usado.
ls [dir] [arq]    Similar a dir, porém inclui informações
                  dependentes de sistema fornecidas pelo servidor.
mdelete [arqs]    Similar a delete para múltiplos arquivos.
mdir arqs loc     Gera uma listagem de arqs no arquivo
                  local loc.
mget arqs         Similar a get para multiplos arquivos.
mkdir dir         Cria um diretório na máquina remota.
mls arqs loc      Gera listagem similar à de ls para os arquivos
                  dados por arqs e grava sua saída no arquivo local loc.
modtime arq       Mostra a data de modificação do arquivo remoto arq.
mput arqs         Copia os arquivos dados por arqs para o
                  diretório de trabalho corrente na máquina remota.
newer arq         Copia um arquivo somente se a versão remota
                  for mais recente do que a versão local, cujo
                  nome será dado por arq.
open host[porta]  Abre uma conexão com o host na porta
                  especificada. Se a opção auto-login estiver
                  habilitada, ftp tentará logar no host remoto.
prompt            Liga ou desliga o modo interativo, onde ftp pede
                  confirmação antes de transferir ou eliminar
                  múltiplos arquivos.
put arq [rem]     Armazena um arquivo na máquina remota,
                  opcionalmente com o nome dado por rem.
pwd               Imprime o diretório corrente da máquina remota.
quit              O mesmo que bye.
recv rem [loc]    O mesmo que get.
remotehelp [cmd]  Pede informações sobre os comandos do
                  servidor ftp remoto.
rename old new    Altera o nome do arquivo remoto chamado
                  old, chamando-o de new.
reset             Sincroniza o cliente com o servidor de ftp.
rmdir dir         Remove do servidor o diretório especificado.
runique           Evita a sobreposição de arquivos, concatenando
                  a seu nome um sufixo numérico.
sendarq loc [rem] O mesmo que put.
status            Mostra o estado atual do ftp.
sunique           O equivalente a runique para o sistema remoto.
type [tipo]       Muda o "tipo de representação" para tipo. Os
                  tipos ascii e binary (ou image) são válidos, sendo
                  ascii o default.
user nome         Identifica o usuário nome com o servidor ftp. Se uma
                  senha de acesso for necessária o servidor irá
                  pedi-la.
verbose           Aciona o modo detalhado de apresentação.
                  Default se os comandos estiverem sendo
                  digitados em um terminal.
? [comando]       O mesmo que help.

Exemplos:

	ftp sunsite.unc. edu
	
	ftp -niv ftp.linux.org < comandos.txt &


