## tail

Mostra as linhas finais de um arquivo. Algumas versões de tail aceitam
no máximo um arquivo como entrada.

Sintaxe: tail[-cn|-nn|-bn][-f] [arquivo ...]
tail [-#[b|c|I] ] [-f] [arquivo ...]

Parâmetro

Descrição

 

-bn
-cn
-f

-nn
-#[b|c|l]

Exemplo:

Mostra os últimos n blocos do arquivo.

Mostra os últimos n caracteres do arquivo.

Faz com que tail não pare de ler o arquivo
mesmo encontrando seu fim. Útil quando o
arquivo está aumentando constantemente.
Mostra as últimas n linhas do arquivo.
Ondefé o número delinhas (default), caracteres
ou blocos a serem mostrados. Presente apenas
em algumas versões do comando tail.

tail /var/adm/messages
Lista as últimas mensagens do sistema.



