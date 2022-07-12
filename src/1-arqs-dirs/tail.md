## tail

Mostra as linhas finais de um arquivo. Algumas versões de tail aceitam
no máximo um arquivo como entrada.

Sintaxe: 

	tail[-cn|-nn|-bn][-f] [arquivo ...]

	tail [-#[b|c|I] ] [-f] [arquivo ...]

Parâmetro Descrição
--------- ---------
-b n      Mostra os últimos n blocos do arquivo.
-c n      Mostra os últimos n caracteres do arquivo.
-f        Faz com que tail não pare de ler o arquivo
          mesmo encontrando seu fim. Útil quando o
          arquivo está aumentando constantemente.
-n n      Mostra as últimas n linhas do arquivo.
-#[b|c|l] Onde # é o número de linhas (default), caracteres
          ou blocos a serem mostrados. Presente apenas
          em algumas versões do comando tail.

Exemplo:

	# Lista as últimas mensagens do sistema.
	tail /var/adm/messages

