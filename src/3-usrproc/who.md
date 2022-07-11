## who
Mostra quem está usando qual terminal.
Sintaxe: who [arquivo] [am i]

Parâmetro Descrição

 

arquivo | Indica o nome de um arquivo alternativo a ser
usado como fonte de informações para who.
ami Mostra o nome real do usuário (real user name).
Exemplo:

who am i

Obs: Por default, who usará os dados do arquivo utmp, a não ser
que um arquivo alternativo seja indicado. Se invocado sem
argumentos, who mostrará o login de todos os usuários com
processos associados a terminais, o nome dos terminais e
dados sobre atividade e tempo de login.


