## cut

Seleciona trechos de cada linha de arquivos texto.

Sintaxe:

cut -flista [-dc] [-s] [arquivo ...]
cut -clista [arquivo ...]

Parâmetro Descrição

- Indica explicitamente que a entrada deve ser
tomada de stdin.
-clista Seleciona caracteres de cada linha do arquivo.
É Lista é umalista de valores inteiros ouintervalos
separados por virgulas.

-flista Seleciona campos em cada linha do arquivo.
Veja também o parâmetro -c.
-de Especifica o delimitador de campos como sendo o

caractere c em vez do caractere de tabulação.
-s Ignora linhas sem delimitadores de campos.


