## stty

Altera as opções de |/O de um terminal. Se invocado sem parâmetros,
stty mostrará a configuração atual do terminal na saída padrão de erros
(stderr).

Sintaxe: stty[-ag] [opção ...]

stty [carcontrole string]...

Utilização: Na segunda sintaxe descrita, stty mapeia um caractere de
controle para uma dada string.

Caracteres de controle:

 

eof Identifica o caractere de fim de arquivo.

eol Identifica o caractere de fim de linha.

erase Identifica o caractere de retrocesso (backspace).

intr Identifica o caractere de interrupção de processo.

kill Identifica o caractere que apaga toda a linha do
terminal.

quit Identifica o caractere de término de processo.

susp Identifica o caractere de suspensão de processo.

Parâmetro Descrição

-a Mostra o estado atual de todas as opções.

-g Mostra o estado atual num formato que pode ser

usado como argumento para o comando stty.

Opções:

Exemplos:
stty

stty

(a presença do caractere - desabilita a opção)
[-Jistrip  Limita (ou não) caracteres de entrada a 7 bits.
Elinicr Mapeia (ou não) NL para CR na entrada.
[igncr | Ignora (ou não) CR na entrada.

[-Jicrnl Mapeia (ou nao) CR para NL na entrada.

[-Jonicr | Mapeia (ou não) NL para CR-NL na saída.

[-Jisig Habilita (ou desabilita) achecagem de caracteres
contra os caracteres especiais INTR, QUIT e
SUSP.

[-Jicanon Habilita (ou desabilita) a entrada canônica
(processamento de ERASE e KILL)

[echo Ecoa ao terminal (ou não) todo caractere digitado.

[-Jechoe O caractere ERASE deve (ou não) apagar
visualmente o caractere anterior ao cursor no
terminal.

[-Jechok Ecoa (ou nao) um newline após um caractere
KILL.

[[lechonl Ecoa(ounão)newlines mesmo que echo esteja
desligado.

[-Jnoflsh Habilita (ou desabilita) descartes após INTR,
QUIT e SUSP.

[Jechoctl Seligado, ecoa caracteres de controle como?X,
caso contrário ecoa os próprios caracteres de
controle.

[Jechoke O caractere KILL deve (ou não) apagar
visivelmente a linha corrente do terminal.

rows n Configura a altura do terminal em linhas.

columns i Configura a largura do terminal em i colunas.

ek Volta os caracteres KILL e ERASE para os
defaults do sistema.

size Otamanho doterminal será impresso em umalinha;
primeiro o número de linhas, depois o de colunas.

sane Configura todos os modos para valores razoáveis
para utilização interativa em terminais.

[-Jert Configura ou desliga todos os modos adequados

a um device CRT.
[-]Jtostop Impede (ou não) a saída de dados de processos
em background para o terminal.

erase “H

Muito útil quando a tecla backspace não funciona corretamente. O
*H do exemplo foi obtido pressionando-se a tecla BackSpace para
associá-la à ação de retrocesso do cursor.

tostop

Permite uma conversa com outro usuário.

Sintaxe:

Obs:


