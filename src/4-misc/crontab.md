## crontab 
Instala, lista ou remove arquivo crontab de usuário.

Sintaxe:

Obs:

Exemplos:
crontab [arquivo]
crontab [ -! | -r| -e]

Parâmetros Descrição

 

-| Mostra o arquivo crontab atual do usuario.

+r Remove o arquivo crontab atual do usuário.

-e Edita o arquivo crontab atual do usuário. Presente
em algumas versões de crontab.

arquivo | Indicaumarquivodecrontabaser posto ematividade,
veja o formato do arquivo crontab abaixo.

Um arquivo de crontab é um arquivo texto onde cada linha

especifica um comando e a periodicidade com queo mesmo

será executado (automaticamente) pelo sistema, no formato:

minuto hora dia mês dia da semana comando

Os campos podem ser separados por espaços ou TABs, os
cinco primeiros podem assumir um valor numérico, um
intervalo (no formato m-n), asterisco ou umalista de quaisquer
destes, separada por vírgulas. Os valores válidos são O a 59
paraminuto, 0a 23 parahora, 1 a 31 paradia, 1a 12paramês
e0a6paradia da semana (0=domingo).

Seguem exemplos de linhas válidas de um arquivo crontab:

0 0 16 7 * mail -s'Feliz aniversario!' macan
Enviará e-mail ao autor deste guia todo dia 16 de julho às 00:00h.

0,15,30,45 8-11,13-16 * * 1-5 /bin/teste.pl
Executa o script teste.pl de quinze em quinze minutos, de segunda
a sexta-feira, no horário comercial.



