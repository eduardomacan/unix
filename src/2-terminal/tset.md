## tset

Sintaxe:

	tset [-Qs] [-] [-e c] [-k c] [-i c] [-m map] [term]

Parâmetro Descrição
--------- ---------
term      Especifica um tipo de terminal,
-I        Não envia as strings de inicialização para o
          terminal.
-Q        Não mostra os valores dos caracteres erase e
          kill.
-s        Gera os comandos da shell para configurar a
          variável TERM.
-         Mostra apenas o nome do terminal.
-e c      Configura o caractere erase como sendo c.
-k e      Configura o caractere kill como sendo c.
-m map    Mapeia portas (ports) a terminais. **map** tem o
          formato **[porta] [op veloc]:tipo**, onde op é um
          operador. Oteste será feito contra otipo da porta
          e sua velocidade. Caso o teste seja positivo,
          configura o tipo de terminal correspondente. Se
          tipo começar com uma interrogação, tset pedirá
          confirmação ao usuário. Os operadores válidos
          são:

Operador Significado
-------- -----------
\>       Maior do que.
\<       Menor do que.
\=       Igual a.
\@       Igual a (equivalente a =).
!        Negação (usado em conjunto com outro
         operador).

Obs: Os valores do mapeamento devem aparecer entre aspas
simples (') para evitar interpretação de caracteres especiais
pela shell.

Exemplo:

	# Mostra os comandos da shell necessários para configurar o
	# terminal como vt100 se estiver associado a uma linha discada a
	# menos de 1200 bauds, vt220 a 9600 bauds e vt100 caso seja um
	# xterm.

	tset -IQs -m ‘dialup<1200:vt100’ 
	     -m ‘dialup@9600:vt220’ ‘xterm:vt100’


