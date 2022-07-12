## su

Troca o ID efetivo do usuário. Solicita confirmação através de senha para
efetuar a execução da shell, exceto quando executado pelo superusuario
(root).

Sintaxe:

	su [-] [user]

Parâmetro Descrição
--------- ---------
-         Executa uma shell de login, carregando todo o
          ambiente do usuário.
user      O nome do usuário para o qual se quer altemar. Se
          omitido, su tomará o usuário root como padrão.

Exemplo:

	su - macan

