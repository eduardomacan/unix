## test

Checa tipos de arquivos e compara valores. Resultado do teste como
valor de retorno do comando.

Sintaxe: 

	test [expr]

Parâmetro Descrição
--------- ---------
-b arq     Verdadeiro se arq existir e for um block device.
-c arq     Verdadeiro se arq existir e for um character device.
-d arq     Verdadeiro se arq existir e for um diretório.
-f arq     Verdadeiro searq existir e for um arquivo regular.
-g arq     Verdadeiro se arq existir e seu bit setgid estiver
           ligado.
-h arq     Verdadeiro se arq existir e for um link simbólico.
-k arq     Verdadeiro searqexistir e seu bitsticky estiver
           ligado.
-n str     Verdadeiro se a string str tiver comprimento
           diferente de zero.
-p arq     Verdadeiro se arq existir e for um FIFO.
-r arq     Verdadeiro seargexistiretiver permissão de leitura.
-s arq     Verdadeiro seargexistire tivertamanho diferente
           de zero.
-t [n]     Verdadeiro se o arquivo aberto com descritor de
           arquivo n estiver associado a um terminal (defaut
           n=1).
-u arq     Verdadeiro se arq existir e seu bit suid estiver
           ligado.
-w arq     Verdadeiro se arq existir e tiver permissão de
           escrita.
-x arg     Verdadeiro se arq existir e for executável.
-z str     Verdadeiro se a string str tiver comprimento zero.
s1         Verdadeiro se s1 tiver comprimento maior do
           que zero.
s1!=s2     Verdadeiro se as strings s1 e s2 não forem
           idênticas.
s1=s2      Verdadeiro se as strings s1 e s2 foremidénticas.
n1 op n2   Verdadeiro, de acordo comos valores numéricos
           de n1 en2 eo operador utilizado. Operadores
           podem ser:
-eq        Igual a.
-ne        Diferente de.
-gt        Maior do que.
-ge        Maior ou igual a.
-It        Menor do que.
-le        Menor ou igual a.

Operador Significado
-------- -----------
!        Operador de negação.
-a       Operador “e” binário.
-o       Operador “ou” binario (-a tem maior precedéncia
         do que -o).

Exemplos (shell scripts):

~~~~~~~~~~~~
#!/bin/sh
# Script para testar tipo de um arquivo.
# Exemplo 1 do comando test.
# Uma implementação simplista do comando “file” 
# do Unix, em shell script.
# Eduardo Macan - 1997

if “tests
  then
    for FILE In S*
    do
      if test -h SFILE
      then
        echo “SFILE e' um link simbólico.”
      elif test -b SFILE
      then
        echo “SFILE e' um block device.”
      elif test -c $FILE
      then
        echo “SFILE e' um character device.”
      elif test -d $FILE
      then
        echo “SFILE e' um diretorio.”
      elif test -p $FILE
      then 
        echo “SFILE e' um FIFO.”
      elif test -f $FILE
      then
        echo “SFILE e’ um arquivo comum.”
      fi
    done
  else
    echo “uso: testa [arquivo... ]”
  fi

#!/bin/sh
#Exemplo 2 do comando test
#Eduardo Marcel Macan - 1997
echo “Quantos anos voce tem?”
read AGE
if test SAGE CIC
then
  echo “Voce ainda nao nasceu?”
elif test SAGE -eq 18
then
  echo “Parabens, voce ja pode ser preso!”
elif test SAGE -lt 10
then
  echo “Seu pai sabe que voce esta aqui?”
elif test SAGE -gt 18 -a SAGE -lt 80
then
  echo “Lembre-se do Imposto de renda...
elif test SAGE -gt 79
then
  echo “Vida longa e prospera.”
else
  echo “Volte para seu videogame!”
fi

#!/bin/sh
#Exemplo 3 do comando test
echo “Voce gosta de batatas [s|n]?”
read RESP
if test SRESP
  then
    if test SRESP = s -o SRESP = S
       then echo “Eu tambem gosto! :)”
       exit O
    elif test SRESP ='n -o SRESP = N
      then echo “Eu gosto. :p”
      exit 1
    fi
fi
echo "Responda s ou n da proxima vez! :("
exit 1

~~~~~~~~~~~~

