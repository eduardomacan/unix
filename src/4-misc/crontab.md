## crontab 

Instala, lista ou remove arquivo crontab de usuário.

Sintaxe:

	crontab [arquivo]

	crontab [ -! | -r| -e]

Parâmetros Descrição
---------- ---------
-l         Mostra o arquivo crontab atual do usuario.
-r         Remove o arquivo crontab atual do usuário.
-e         Edita o arquivo crontab atual do usuário. Presente
           em algumas versões de crontab.
arquivo    Indica um arquivo de crontab a ser posto em atividade,
           veja o formato do arquivo crontab abaixo.

Obs: Um arquivo de crontab é um arquivo texto onde cada linha
especifica um comando e a periodicidade com queo mesmo
será executado (automaticamente) pelo sistema, no formato:

minuto hora dia mês dia da semana comando

Os campos podem ser separados por espaços ou TABs, os
cinco primeiros podem assumir um valor numérico, um
intervalo (no formato m-n), asterisco ou uma lista de quaisquer
destes, separada por vírgulas. Os valores válidos são O a 59
para minuto, 0 a 23 para hora, 1 a 31 para dia, 1a 12 para mês
e 0 a 6 para dia da semana (0=domingo).

Exemplos:

	# Seguem exemplos de linhas válidas de um arquivo crontab:

	# Enviará e-mail ao autor deste guia todo dia 16 de julho 
	# às 00:00h.
	0 0 16 7 * mail -s'Feliz aniversario!' macan

	# Executa o script teste.pl de quinze em quinze minutos,
        # de segunda a sexta-feira, no horário comercial.

	0,15,30,45 8-11,13-16 * * 1-5 /bin/teste.pl

