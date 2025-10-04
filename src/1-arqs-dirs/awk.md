## awk
Descrição

:   Linguagem para processamento de padrões. Para uma descrição
detalhada da linguagem AWK e seus comandos, consulte os manuais
on-line do sistema (**man awk**).

Sintaxe 

	awk [ -f *arq* ][ -F *c* ] ['prog'] [arquivo ...]

Parâmetro     Descrição
---------     ---------
**-**         Toma a entrada de stdin.
**-f** *arq*  Usa o conjunto de padrões definidos no arquivo 
              *arq* para processar sua entrada.
**-F** *c*    Muda o caractere separador de campos.
*arquivo*     Especifica um arquivo de entrada. 
              Um nome de arquivo no formato **string=valor** 
              será tratado como uma atribuição de valor à
		      variável string e será executado no momento
		      em que seria processado caso fosse um arquivo
		      válido.
**'prog'**    Sequência de declarações *padrão-ação*
              separadas por ponto e vírgula (;). Uma declaração
		      *padrão-ação* tem o seguinte formato: 
		      **padrão { ação }**

Utilização:

Comparam-se os padrões especificados em prog a cada linha dos arquivos de entrada, executando uma ação associada sempre que houver correspondência. Um padrão vazio corresponde a todas as linhas da entrada, a ação vazia imprime a linha que correspondeu ao padrão.

Padrões: 

Um padrão é uma combinação booleana de expressões relacionais ou regulares, com sintaxe similar à da linguagem C. Dois padrões especiais, **BEGIN** e **END**, são usados para tomar ações antes do processamento da primeira linha de entrada e após o processamento da última linha, respectivamente.

Ações: 

Uma ação é uma sequência de comandos separados por ponto e virgula (;) TAB ou newiline.

Comandos
  
	if (expr) comando [ else comando ]
	while ( expr ) comando
	do comando while (expressão )
	for ( expr; expr ; expr) comando
	for ( variavel in lista ) comando
	break
	continue
	{ [ comando ...] }
	variável=expr
	print [expressão ...]
	printf formato [, expressão [, ...]]
	next
	exit [n]

Expressões

Expressões em AWK têm sintaxe semelhante à da linguagem
C, sendo válidos os operadores relacionais e de atribuição
definidos nesta linguagem, a saber:

Operador    Significado
--------    -----------
**+**       Adição.
**-**       Subtração.
** \* **    Multiplicação.
**/**       Divisão.
**\%**      Módulo.
**\^**      Exponenciação.
**++**      Incremento.
**--**      Decremento.
**+=**      Soma de valor à variável.
**-=**      Subtração de valor da variável.
** \*= **   Multiplicação de variável por valor.
**/=**      Divisão de variável por valor.
**\%=**     Módulo de variável por valor.
**^=**      Exponenciação de variável por valor.
**>**       Maior que. 
**>=**      Maior ou iguala.
**<**       Menor que.
**<=**      Menor ou igual a.
**!=**      Diferente de.
**?:**      Condicional.

Funções

Função                Definição
------                ---------
exp(x)                Retorna o valor de e”.
log(x)                Retorna o logaritmo natural de x.
sqrt(x)               Retorna a raiz quadrada de x.
index(s,t)            Retorna a posição da primeira ocorrência
                      da string s dentro da string t, ou zero se
                      não houver ocorrências.
int(s)                Converte a strings para um valor inteiro.
                      Se s não for especificada, usa toda a
		      linha de entrada.
lenght(s)             Retorna o comprimento da string s, ou da
                      linha de entrada se s não for especificada.
match(s,er)           Retorna a posição da primeira ocorrência da
                      expressão regular er dentro da string s, ou
                      zero se não houver ocorrências.
split(s,a,fs)         Divide a strings em vários elementos de
                      um vetor **a[n]** e retorna **n**. A divisão é feita
                      usando a expressão regular fs ou o
                      separador de campos FS se fs não for
                      especificado.
sprintf(fmt,exp,...)  Formata as expressões de acordo com o
                      formato especificado por fmt e retorna a
                      string resultante (equivalente à função
                      sprintf da linguagem C).
substr(s,m,n)         Retorna uma substring des comncaracteres
                      começando na posição m.
getline               Carrega a próxima linha de entrada em
                      $0, retornando 1 em caso de sucesso, O
                      para fim de arquivo e -1 para erro.


Variaveis e constantes:

Variáveis podem ser elementos de vetor (representados por
**x[y]**, onde **x** é um vetor e **y** o índice) ou campos do arquivo
de entrada (representados por **$n**, onde **n** representa o
número do campo). Os vetores podem ser indexados por
strings, as quais aparecem, obrigatoriamente, entre aspas
duplas (").

Variáveis internas:

Variável                 Significado
--------                 -----------
FILENAME                 Nome do arquivo de entrada corrente.
NF                       Número de campos no registro (linha de
                         entrada) corrente.
NR                       Número do registro corrente.
OFS                      Separador de campos da saida (default
                         espaço).
ORS                      Separador de linhas de saida (default
                         newline).
RS                       Separador de linhas da entrada (default
                         newline).
FS                       Separador de campos (default espaço e
                         TAB).

### Exemplos:

	# Mostra os usuarios locais do sistema e seus
	# respectivos nomes completos.
	awk -F: '{print $1 " -> " $5)' /etc/passwd

~~~~~~~
 # Programa - AWK Eduardo M. Macan 1996
 # Calcula as médias dos alunos e a média da 
 # classe, a partir  de um arquivo texto contendo
 # um nome e duas notas em cada linha 
 # (por exemplo: Eduardo 5.7 7.5).

BEGIN {
	printf("Aluno\t\tMedia Final\n")
}

S1 {
	++alunos;
	media=($2 + $3) / 2;
	printf ("%s\t\t%.2£\n",$1,media) ;
	total+=media
}

END {
	printf("Media da turma : %.2f\n",total/alunos)
}
#fim do programa
~~~~~~~

