## rsh

Executa um comando no host especificado. Se invocado sem a
especificação de um comando, executa uma shell interativa no host
remoto.

Sintaxe: 

	rsh [-Iuser] host [comando]

Parâmetro Descrição
--------- ---------
-l user   Permite executar a shell como outro usuario no
          host remoto (por default, o nome do usuário
          remoto será o mesmo do local).

Exemplo:

	#outro.host.exemplo e dracula sao nomes
	#ficticios de hosts.

	rsh -l macan outro.host.exemplo
	rsh dracula

