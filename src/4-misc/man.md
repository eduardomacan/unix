## man

Consulta os manuais on-line do sistema. 

Sintaxe: 

	man [-fk] [seção] [chave ...]

	man [-fk] [-s seção] [chave ...]

Parâmetro Descrição
--------- ---------
-f        Mostra descrições de uma linha sempre que
          chave coincidir com uma entrada do manual.
-k        Pesquisa informações sobre palavras-chave nas
          descrições das páginas dos manuais on-line.
-s seção  Algumas versões de man necessitam do
          parâmetro -s caso se queira especificar uma
          seção dos manuais onde buscar a informação.

Obs: As páginas do manual são tradicionalmente divididas em 8
seções principais, a saber:

Seção Descrição
----- ---------
1     Comandos de usuário.
2     Chamadas de sistema.
3     Subrotinas (programação).
4     Dispositivos.
5     Formatos de arquivos.
6     Jogos.
7     Miscelânea.
8     Administração do sistema.

Exemplos:

	man man

	man ls

	man -k tape

