## dd

Copia, converte e formata arquivos.

df

Exemplos:

cut -d: -£1,5 /etc/passwd
Mostra userid e nome completo dos usuarios locais.

echo "Eduardo Marcel Maçan" |cut -c-7,15-
echo "blues&rock&bolero"|cut -di& -f1,2

Sintaxe: dd [opção=valor...]

Parâmetro Descrição

bs=n Configura ibs=n bytes e obs=n bytes.

cbs=n Converte n bytes de cada vez.

count=n Copia apenas n blocos de entrada.

ibs=n Lé n bytes de entrada de cada vez.

if=arq Lê o arquivo arq em vez de stdin.

obs=n Escreve n bytes no arquivo de saída de cada vez.

of=arq Escreve no arquivo arq em vez de escrever em

Obs:

Exemplos:

stdout e não trunca o arquivo.

seek=n Busca o n-ésimo bloco de tamanho obs do

arquivo de entrada antes de começar a cópia.

skip=n Ignora os n primeiros blocos de tamanho igual a

ibs na entrada.

conv=chave[,chave...]

Converte o arquivo segundo a lista de chaves
separadas por vírgulas. Chaves podem ser:
ascii Converte de EBCDIC para ASCII.
ebcdic Converte de ASCII para EBCDIC.
ibm Converte de ASCII para EBCDIC usando
tabela alternativa.
block 'Preenche registros terminados por newline
com espaços até que estes atinjam otamanho
especificado por cbs.
unblock Substitui espaços finais em registros de
tamanho fixo cbs por newline.
lcase Converte para minúsculas.
ucase Converte para maiúsculas.
swab Troca pares de bytes de posição.
noerror Ignora a ocorrência de erros.
notrunc Não trunca o arquivo de saída.
sync Preenche cada bloco de entrada com NULs até
atingir o tamanho especificado poribs.

n pode apresentar um multiplicador, que pode ser m
(megabytes), k (kilobytes), b (blocks - 512 bytes) ou c
(characters - bytes).

dd if=ebcdic.txt of=ascii.txt conv=ascii, lcase

Converte um arquivo de ebcdic para ascii e para letras minúsculas.

ls | dd conv=ucase

Converte a saída do comando Is para maiúsculas.



