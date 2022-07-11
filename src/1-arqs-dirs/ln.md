## ln

Cria links para arquivos ou diretórios. In cria tanto links simbólicos (soft
links) como diretos (hard links). Default=links diretos.

Sintaxe:

	ln [-fs] <destino> <nome>
	ln [-fs] <arquivo> [arquivo ...] <diretório>

Parâmetro Descrição
--------- ---------
-f        Força a criação do link, ignorando acessibilidade
          ou existência de arquivos.
-s        Cria um link simbólico (soft link).

