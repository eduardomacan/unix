## rcp
Copia arquivos de uma maquina remota.
Sintaxe: rcp [-pr] <fonte> <destino>
Parâmetro Descrição

-p Mantém os atributos do arquivo original, como,
por exemplo, datas de acesso e modificação e
permissões de acesso.

-[ Copia também o conteúdo dos subdiretórios
abaixo do diretório especificado.

fonte Especifica um arquivo ou diretório em máquina
remota, podendo assumir duas formas:
require ou ainda

usuario@maquina:path (0 ultimo, no caso do
arquivo pertencer a outro usuario).
destino Similar a fonte. Quando multiplos arquivos sao
especificados por fonte, o destino precisa
necessariamente ser um diretório.
Obs: O usuário e a máquina destino precisam ter permissão de
acesso via rede nas máquinas fonte. Consulte o manual do
sistema para maiores informações.

Exemplo:
rep -p leonardo@cradle:/bin/teste.pl
Copia o arquivo teste.pl, residente em /bin, para a máquina
chamada cradle.
rep -r dracula:/home/macan/bin/ .
Copia todo o diretório /home/macan/bin da maquina chamada
dracula para o diretorio corrente.


