## fg

Põe em foreground um processo em execução.
Sintaxe: fg [%id]

Utilização: Comando interno da shell. Quando um processo foi
interrompido ou está sendo executado em background (veja
bg), o comando fg transferirá o controle do terminal para o
processo.

Obs: Uma lista dos processos e seus respectivos identificadores
poderá ser obtida com o comando jobs. Se nenhum
identificador de job for especificado, o último processo
interrompido será colocado em foreground.

Parâmetro Descrição

 

id No caso de haver varios processos interrompidos,
indica qual processo sera colocado em foreground.

Exemplo:
fsequência de comandos, respostas da shell
tem itálico.
vi&
[1] xxx  (<-- número do processo)
[1]+ Stopped (tty output) vi
fg %1


