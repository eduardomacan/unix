## write

Envia uma mensagem a um terminal.
Sintaxe: write usuário [terminal]

Parâmetro Descrição

 
term Indica para qual terminal deve ser enviada a
mensagem.
Obs: write continuará copiando linhas para o outro terminal até

encontrar o caractere de fim de arquivo (EOF, normalmente
CTRL-D); neste momento, write escreverá EOT no outro
terminal e terminará sua execução.

Exemplo:
write suzie

Oi, vamos almocar? :)
“0



