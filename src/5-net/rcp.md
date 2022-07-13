## rcp

Copia arquivos de uma maquina remota.

Sintaxe: 

	rcp [-pr] <fonte> <destino>

Parâmetro Descrição
--------- ---------
-p        Mantém os atributos do arquivo original, como,
          por exemplo, datas de acesso e modificação e
          permissões de acesso.
-r        Copia também o conteúdo dos subdiretórios
          abaixo do diretório especificado.
fonte     Especifica um arquivo ou diretório em máquina
          remota, podendo assumir duas formas:
          maquina:path ou ainda usuario@maquina:path 
          (o ultimo, no caso do arquivo pertencer a outro usuario).
destino   Similar a fonte. Quando multiplos arquivos são
          especificados por fonte, o destino precisa
          necessariamente ser um diretório.

Obs: O usuário e a máquina destino precisam ter permissão de
acesso via rede nas máquinas fonte. Consulte o manual do
sistema para maiores informações.

Exemplo:

	# Copia o arquivo teste.pl, residente em /bin na máquina
	# chamada cradle para o diretório corrente.

	rcp -p leonardo@cradle:/bin/teste.pl .

	# Copia todo o diretório /home/macan/bin da maquina chamada
	# dracula para o diretorio corrente.

	rcp -r dracula:/home/macan/bin/ .



