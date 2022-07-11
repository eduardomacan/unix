## cp

Copia um ou vários arquivos. Quando vários arquivos estão sendo
copiados, destino deve se referir a um diretório.

Sintaxe: cp [-ipr] <arquivo> [arquivo ...] <destino>
Parâmetro Descrição

- Solicita confirmação antes de copiar cada arquivo.

-p Mantém na cópia as datas de modificação e as
E permissões do arquivo original.
-r Copia todos os arquivos e subdiretórios abaixo

do diretório especificado. Neste caso, destino
deve se referir a um diretório.
Exemplos:
cp -r ~leonardo/html/ /www
Copia todo o diretório html do usuário leonardo para o diretório /
www.


