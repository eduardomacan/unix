## chgrp

Muda o grupo de um arquivo.

Sintaxe:

	chgrp [-R] <grupo> <arquivo> [arquivo ...]

Parâmetro Descrição
--------- ---------
-R        Muda ogrupo de todos os arquivos e subdiretórios
          abaixo do diretório especificado.

Obs:
O grupo de um arquivo só pode ser mudado pelo dono; os
grupos válidos são aqueles a que o dono pertence. Apenas
o superusuário (root) pode mudar o grupo de arquivos dos
outros usuários.

