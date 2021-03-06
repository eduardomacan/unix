## vi 

Editor de textos.

Sintaxe:

	vi [arquivo]

Utilização:

Há dois modos de trabalho no vi, o modo de comando e o
modo de edição ou entrada. No modo de comando pode-se
movimentar pelo texto, copiar e eliminar linhas e caracteres;
o modo de edição é onde entramos o texto propriamente dito.

Vários comandos nos levam ao modo de edição, mas
apenas a tecla de escape (\<esc\>) nos leva ao modo de
comando. Pode-se fazer com que um comando se repita
automaticamente um determinado número de vezes,
bastando digitar o número de repetições antes do nome do
comando. Os comandos que permitem essa característica
estarão precedidos por [n]; omitir n equivale a digitar 1 antes
do comando.

Comando   Descrição
-------   ---------
[n]h      Move o cursor n caracteres à esquerda.
[n]l      Move o cursor n caracteres à direita.
[n]k      Move o cursor n caracteres acima.
[n]j      Move o cursorn caracteres abaixo.
/texto    Procura a cadeia texto no arquivo e move o
          cursor para a sua primeira letra.
[n]a      Insere texto após o cursor.
[n]i      Insere texto antes do cursor.
[n]o      Insere uma nova linha abaixo do cursor e inicia
          a inserção de texto.
[n]O      Insere uma nova linhaacimado cursor inicia a
          inserção de texto.
[n]yy     Copia a linha em que se encontra o cursor.
u         Desfaz a última edição feita no texto.
[n]p      Insere a linha copiada após a linha onde está o
          cursor.
[n]dd     Elimina a linha onde está o cursor (a linha apagada
          pode ser inserida novamente com p).
[n]x      Elimina o caractere sobre o cursor.
:w [nome] Atualiza o arquivo editado ou grava-o com outro
          nome caso tenha sido especificado um nome.
:w nome   Grava o texto no arquivo especificado por nome.
:q[!]     Sai do editor de textos. Se o texto foi modificado
          e não foi salvo o caractere opcional ! fará com
          que qualquer modificação seja ignorada.
\<esc\>   Entra no modo de comando ou cancela
          comandos não terminados.
[n].      Repete n vezes o último comando que modificou o
          texto.
número    Move ocursor para a linha número.
0 (zero)  Move o cursor para o primeiro caractere dalinha.
[n]A      Entra no modo de edição, inserindo o texto ao
          final da linha.
[n]G      Move o cursor até a linhan ou até a última linha
          caso n não tenha sido especificado.
[n]J      Junta n linhas consecutivas do texto a partir do
          cursor.
U         Restaura a linha atual ao estado em que ela se
          encontrava antes da ultima visita do cursor.
[n]~      Inverte a caixa (case) dosn caracteres seguintes
          ao cursor.

Obs: Note que alguns caracteres especiais podem utilizar mais de
uma posição na tela e, que algumas linhas de texto podem
utilizar mais do que o número de caracteres mostrados em
uma linha do terminal; as modificações se aplicam a toda a
linha de texto sobre a qualo cursor se encontrarenão à linha
do terminal.

