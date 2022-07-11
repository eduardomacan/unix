## ftp

Transfere arquivos entre máquinas da rede.

Sintaxe:

ftp [-ginv] [maquina]

Parâmetro Descrição

-g Desabilita o "globbing" dos nomes de arquivos,
habilitado por default. Veja o comandoglob abaixo.

-i Não pede confirmação antes da transferência de
múltiplos arquivos. Veja o comandoprompt abaixo.

-n Desabilita o "auto-login”. Veja o comando open
abaixo. -
v Habilita a saida descritiva. Default se a entrada

padrão estiver associada a um terminal.

Comandos:

Ilcmd [args]]
Invoca uma shell na máquina local e executa o
comando cmd.

appendarq local[arq remoto]
Concatena o arquivo na máquina localarq local
ao arquivo remoto arq remoto.

ascii Ativa o modo de transferência adequado para a
transferência de arquivos texto.

bell Soa um alarme a cada transferência de arquivo
completada.

binary Ativa o modo de transferência adequado a
arquivos binários.

bye Encerra a sessão como servidor remoto e saido

programa ftp. Um caractere EOF (geralmente
"D) tem o mesmo efeito.

case Converte o nome dos arquivos transferidos para
minúsculas.

cd dir remoto
Muda diretório de trabalho na máquina remota
paradir remoto.

cdup Muda para o diretório pai do diretório atual no
servidor.

chmod modo arquivo remoto
Muda o modo de acesso de arquivo remoto
para aquele especificado por modo.

close Termina a sessão com o servidor remoto e
retorna ao interpretador de comandos.
cr Liga/desliga a filtragem de caracteres CR durante

transferências do tipoascii. Ativada é o default.

deletearq remoto
Remove oarquivoarq_remotodamaquinaremota.

dir [dir remoto] [arg local]
Mostra o conteúdo do diretório dir remoto,
opcionalmente colocando a saída no arquivo
arq local.

disconnect O mesmo que close.

getarq remoto [arq local]
Transfere o arquivo da máquinaremotaarg remoto
paraamáquinalocal, renomeando-o paraarq local
caso esse parâmetro seja fornecido.

glob Liga/desliga a expansão de nomes de arquivos
para os comandos mget , mput e mdelete. O
default é a expansão de nomes ativada.

hash Mostra um caractere % (hash) para cada bloco de
dados recebido (1Kbyte).

help [cmd] Mostraumamensageminformativa sobre ocomando
cmd. Se nenhum comando for especificado, lista
todos os comandos disponiveis.

idle[seg] Ajustaoreldgio deinatividade no servidor remoto
paraseg segundos. Seseg nãofor especificado,
mostra o valor atual do contador.

lcd [dir local]
Muda o diretório de trabalho na máquina local.
Se dir local não for especificado, o diretório
HOME do usuário será usado.


Exemplos:

Is [dir remoto] [arq local]
Similar a dir, porém inclui informações
dependentes de sistema fornecidas pelo servidor.
mdelete [args remotos]
Similar a delete para múltiplos arquivos.
mdirarqs remotos arq local
Gera umalistagem dearqs_remotosno arquivo
localarq_local.
mgetarqs_remotos
Similar a get para multiplos arquivos.
mkdir dir_remoto
Cria um diretório na máquina remota.
misarqs remotos arq local
Gera listagem similar à de Is para os arquivos
dados por args remotos e grava sua saída no
arquivo localarg local.
modtimearq remoto
Mostra a data de modificação do arquivo remoto
arq remoto.
mputargs locais
Copia os arquivos dados porargs Jocais para o
diretório detrabalho corrente na máquina remota.
newerarquivo
Copia um arquivo somente se a versão remota
for mais recente do que a versão local, cujo
nome será dado por arquivo.
openhost[porta]
Abre uma conexão com o host na porta
especificada. Se a opção auto-login estiver
habilitada, ftp tentará logar no host remoto.
prompt | Ligaou desliga o modo interativo, ondeftp pede
confirmação antes de transferir ou eliminar
múltiplos arquivos.
putarq local[arq remoto]
Armazena um arquivo na máquina remota,
opcionalmente com o nome dado por

arq remoto.
pwd Imprime o diretório corrente da máquina remota.
quit O mesmo que bye.

recvarq remoto [arg local]
O mesmo que get.
remotehelp [comando]
Pede informações sobre os comandos do
servidor ftp remoto.
renamenome velho novo nome
Altera o nome do arquivo remoto chamado
nome. velho, chamando-o denovo nome.
reset Sincroniza o cliente com o servidor de ftp.
rmdir diretório
Remove do servidor o diretório especificado.
runique  Evitaa sobreposição de arquivos, concatenando
a seu nome um sufixo numérico.
sendarq local [arq remoto]
O mesmo que put.
status Mostra o estado atual do ftp.
sunique Oequivalente arunique para o sistema remoto.
type [tipo] Muda o "tipo de representação" para tipo. Os
tipos asciie binary (ou image) são válidos, sendo
ascii o default.
useruser-name
Identifica o usuário no servidor ftp. Se uma
senha de acesso for necessária o servidor irá
pedi-la.
verbose Aciona o modo detalhado de apresentação.
Default se os comandos estiverem sendo
digitados em um terminal.
? [comando]
O mesmo que help.

ftp sunsite.unc. edu
ftp -niv ftp. Linux,org < comandos.txt &


