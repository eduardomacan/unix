## mv

Move ou renomeia arquivos e diretórios. Se múltiplos arquivos forem
especificados, destino deverá necessariamente ser um diretório.

Sintaxe: 

	mv [-fi] <arquivo> [arquivo ...] <destino>

Parâmetro Descrição
--------- ---------
-f        Não pede confirmação antes de sobrescrever
          um arquivo ja existente.
-i        Pede confirmação antes de mover um arquivo
          que irá sobrescrever outro.

Exemplos:

	mv livro livro.old

	mv linux/docs/*HOWTO ../linux/

