## cut

Seleciona trechos de cada linha de arquivos texto.

Sintaxe:

	cut -flista [-dc] [-s] [arquivo ...]
	cut -clista [arquivo ...]

Parâmetro   Descrição
---------   ---------
-           Indica explicitamente que a entrada deve ser
            tomada de stdin.
-c *lista*  Seleciona caracteres de cada linha do arquivo.
            *lista* é uma lista de valores inteiros ou intervalos
            separados por virgulas.
-f *lista*  Seleciona campos em cada linha do arquivo.
            Veja também o parâmetro -c.
-d*c*       Especifica o delimitador de campos como sendo o
            caractere *c* em vez do caractere de tabulação.
-s          Ignora linhas sem delimitadores de campos.

Exemplos:

	# Mostra **userid** e nome completo dos usuários locais
	cut -d: -f1,5 /etc/passwd

	echo "Eduardo Marcel Macan"|cut -c-7,15-

	echo "blues&rock&bolero"|cut -d\& -f1,2
