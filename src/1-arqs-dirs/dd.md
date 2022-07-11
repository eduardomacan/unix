## dd

Copia, converte e formata arquivos.

Sintaxe: 

	dd [opção=valor...]

Parâmetro              Descrição
---------              ---------                                         
bs=n                   Configura ibs=n bytes e obs=n bytes.
cbs=n                  Converte n bytes de cada vez.
count=n                Copia apenas n blocos de entrada.
ibs=n                  Lê n bytes de entrada de cada vez.
if=arq                 Lê o arquivo arq em vez de stdin.
obs=n                  Escreve n bytes no arquivo de saída de cada vez.
of=arq                 Escreve no arquivo arq em vez de escrever em
                       stdout e não trunca o arquivo.
seek=n                 Busca o n-ésimo bloco de tamanho obs do
                       arquivo de entrada antes de começar a cópia.
skip=n                 Ignora os n primeiros blocos de tamanho igual a
                       ibs na entrada.
conv=chave[,chave...]  Converte o arquivo segundo a lista de chaves
                       separadas por vírgulas. Chaves podem ser:
                       **ascii**      Converte de EBCDIC para ASCII.
                       **ebcdic**     Converte de ASCII para EBCDIC.
                       **ibm**        Converte de ASCII para EBCDIC usando
                                      tabela alternativa.
                       **block**      Preenche registros terminados por newline
                                      com espaços até que estes atinjam otamanho
                                      especificado por cbs.
                       **unblock**    Substitui espaços finais em registros de
                                      tamanho fixo cbs por newline.
                       **lcase**      Converte para minúsculas.
                       **ucase**      Converte para maiúsculas.
                       **swab**       Troca pares de bytes de posição.
                       **noerror**    Ignora a ocorrência de erros.
                       **notrunc**    Não trunca o arquivo de saída.
                       **sync**       Preenche cada bloco de entrada com NULs até
                                      atingir o tamanho especificado por ibs.
                       **n**          pode apresentar um multiplicador, que pode ser m
                                      (megabytes), k (kilobytes), b (blocks - 512 bytes) ou
                                      c (characters - bytes).

Exemplos:

	# Converte um arquivo de ebcdic para ascii e para letras minúsculas.
	dd if=ebcdic.txt of=ascii.txt conv=ascii, lcase

	# Converte a saída do comando ls para maiúsculas.
	ls | dd conv=ucase

