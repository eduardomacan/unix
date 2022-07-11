## tput

Usa osdados determcap para disponibilizar características dependentes
do tipo do terminal para a shell de maneira transparente.

Sintaxe:

Obs:

Exemplo:
tput

tset

Inicializa terminais.

ee

Sintaxe:

tput [-Ttipo] atributo

Parâmetro Descrição

 

-Ttipo Indica o tipo do terminal. Normalmente
desnecessária, usa o valor da variável de
ambiente TERM como default.

atributo | Indica o atributo das tabelas de características
de terminal (terminfo). Abaixo alguns atributos
válidos:

bel Emite um sinal sonoro (bip).

blink Envia a sequência de comandos que instrui o
terminal a mostrar o texto piscando.

bold Envia a sequência de comandos que instrui o
terminal a mostrar os caracteres em negrito
(bold).

civis Torna o cursor invisível.

clear Envia a sequência de limpeza de terminal
para o terminal atual.

cnorm Restaura os atributos do cursor.

cols Mostra o número de colunas do terminal.

cupyx Envia a sequência que move o cursor para a
posição X,Y do terminal.

lines Mostra o número de linhas do terminal.

rmso Sequência para cancelar texto reverso.

smso Sequência para iniciar texto reverso.

tput envia as sequências de terminal para stdout, sendo
possivel redirecionar sua saída para arquivos ou dispositivos,
oque pode ser muito útil. Alguns terminais não implementam
todas as características disponibilizadas por tput.

clear; tput 12 34;echo "O0i7!“ztput 24 O
Digite o texto acima em uma linha ou em um script e veja a string
"Oi!" aparecer no meio da tela.


