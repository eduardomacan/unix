## env

Executa um comando em um ambiente modificado.

Sintaxe: 

	env [-][-i] [-u nome] [var=valor]... [comando [args]

Parâmetro Descrição
--------- ---------
-i        Começa um ambiente do zero, ignorando as
          variaveis de ambiente atuais.
-         O mesmo que -i.
-u nome   Elimina a variável dada por nome ao ambiente
          montado por env.
var=valor Cria a variável de ambiente dada por var e lhe
          atribui o valor especificado.
comando   Comando a ser executado em ambiente
          modificado.
args      Argumentos do comando a ser executado por
          env.

Obs: Caso não seja especificado um comando, env listará todas
as variáveis do ambiente montado. As variáveis de ambiente
criadas. por env só estarão disponíveis para o comando
especificado durante sua execução.

Exemplos:

	
	# Executa o comando echo num ambiente onde a variável NOME está
	# definida.

	env NOME=Eduardo echo SNOME

	# Executa o comando echo num ambiente onde nenhuma variável
	# está definida.

	env -i echo $HOME


