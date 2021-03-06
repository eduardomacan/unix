## chmod

Altera permissões de acesso a arquivos.

Sintaxe:

	chmod [-R] <modo> <arquivo> [arquivo ...]

Parâmetro Descrição
--------- ---------
-R        Muda o modo de acesso de todos os arquivos e
          subdiretórios abaixo do diretório especificado.
          modo Pode assumir modo simbólico ou absoluto, como
          descrito a seguir:

Modo simbólico:

O modo simbólico é uma lista de expressões da forma
**[identificador ...] operando [valor]** separada por vírgulas.

Identificador Descrição
------------- ---------
u             Permissões para o dono do arquivo.
g             Permissões para o grupo do arquivo.
o             Permissões para outros grupos.
a             Todos os anteriores (all). Default se o
              identificador for omitido.

Operando Descrição
-------- ---------
\+        Adiciona permissão às permissões
          existentes no arquivo.
\-        Retira permissão das permissões
          existentes no arquivo.
\=       Assinala explicitamente uma permissão
         (zerando as outras).

Valor Descrição
----- ---------
r     Permissão para leitura.
w     Permissão para escrita.
x     Permissão para execução.
X     Permissão para execução se o arquivo
      for um diretório ou já houver permissão.
s     Bit setgid se atribuido a g, setuid se
      atribuído au.
t     Bit *sticky*.

Modo absoluto:

As permissões neste modo são representadas por um
número octal de quatro dígitos, da forma **EUGO**.

Dígito Significado
------ -----------
E      Atributos especiais.
U      Permissões para o dono do arquivo.
G      Permissões para o grupo do arquivo.
O      Permissões para outros grupos.
Para os dígitos UGO temos a seguinte interpretação:
Valor Octal Significado
----------- -----------
0           Nenhuma permissão.
1           Permissão de execução.
2           Permissão de escrita.
3           Permissão de execução e escrita.
4           Permissão de leitura.
5           Permissão de execução e leitura.
6           Permissão de leitura e escrita.
7           Permissão de leitura, escrita e execução.

Para o dígito E temos a seguinte interpretação:

Valor Octal Significado
----------- -----------
0           Nenhum atributo especial ligado.
1           Bit sticky ligado.
2           Bit setgid ligado.
3           Bits sticky e setgid ligados.
4           Bit setuid ligado.
5           Bits sticky e setuid ligados.
6           Bits setuid e setgid ligados.
7           Bits sticky, setuid e setgid ligados.
Atributos especiais:

Bit         Significado
---         -----------
**setuid**  O arquivo é executado como se fosse
            invocado pelo proprietário; nãofaz sentido
            para diretórios.
**setgid**  O arquivo é executado sob seu grupo,
            mesmo que o usuário invocador não
            participe dele; todo arquivo criado em um
            diretório **setgid** é criado com o mesmo
            grupo do diretório.
**sticky**  Um arquivo criado sob um diretório com
            o bit sticky ligado pode ser apagado
            apenas por seu proprietário. A
            interpretação do sticky bit pode variar
            entre sistemas Unix.

Obs: No modo absoluto, os zeros à esquerda são ignorados, no
modo simbólico só faz sentido omitir valor utilizando o
operador = para zerar os bits de permissão. Apenas o
superusuário (root) pode alterar os atributos de um arquivo
de outro usuário.

Exemplos:

	# Adiciona permissão de execução pelo dono ao arquivo meu. script
	chmod u+x meu script

	# Adiciona permissão de leitura e escrita para o dono e para o grupo
	# de usuários ao qual o arquivo meu script pertence.
	chmod ug+rw meu script

	# Adiciona permissão de execução e escrita pelo dono ao mesmo
	# tempo que retira a permissão de escrita do grupo e deixa outros
	# grupos apenas lerem o conteúdo do arquivo.
	chmod u+wx,g-w,o0=r meu script

	# Confere permissão de leitura, escrita e execução ao nes do
	# arquivo, leitura e execução ao grupo do arquivo e nenhuma
	# permissão aos demais grupos de usuários.
	chmod 750 helloworld

	# Equivalente ao anterior.
	chmod 0750 helloworld

	# Liga o sticky bit do diretório e dá permissão de leitura, escrita e
	# execução a todos os usuários do sistema.
	chmod 1777 -macan/PUB/

	# Confere permissão de leitura, escrita e execução ao dono e de
	# execução para grupo e outros ao diretório HOME.
	chmod 711 ~

