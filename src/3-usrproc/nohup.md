## nohup

Faz com que um comando continue sua execução mesmo que o usuário
que o iniciou saia do sistema.

 

Sintaxe: nohup <comando> [args]

Parâmetro

Descrição

comando O comando a ser executado. Este poderá ser

executado em background se após seus
argumentos estiver presente o caractere &.

args Os argumentos a serem passados em linha de
comando para o comando cmd.
Obs: Em algumas versões de nohup, a saída do comando

executado é armazenada num arquivo chamadonohup.out,
no diretório corrente, ou no diretório HOME do usuário caso
o diretório corrente não ofereça permissão de escrita.

Exemplo:

nohup find / -print &


