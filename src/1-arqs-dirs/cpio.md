## cpio

Armazena ou recupera arquivos guardados em arquivos de
armazenamento.

Sintaxe:

	cpio -o [acvB] [C val]
	cpio -i [cdfmrstuvS6B] [padrão ...]
	cpio -p [adimuv] <diretorio>

Parâmetro Descrição
--------- ---------
-6        Processa arquivos no formato antigo de cpio.
          Usado somente com -i.
-B        Usa blocos de 512 bytes.
-C *val*  Usa blocos de val * 512 bytes.
-S        Troca a posição das metades de cada palavra (4
          bytes) nos arquivos.
-a        Mantém o tempo de cesso (access time) dos
          arquivos fonte.
-c        Escreve e lê informações de cabeçalho no
          formato ASCII. Um arquivo criado com -c precisa
          ser lido com -c.
-d        Cria diretórios conforme a necessidade.
-f        Só copia arquivos que não coincidam com os
          padrões especificados.
-i        Lê da entrada padrao um arquivo criado por **cpio -o**
          e extrai os arquivos armazenados.
-l        Usa links em vez de copiar arquivos, sempre que
          possivel. Deve ser usado com -p.
-m        Mantém a data de modificação dos arquivos.
          Não funciona com diretórios.
-o        Lê nomes de arquivos da entrada padrão (stdin)
          e os copia para a saída padrão, junto com a
          informação necessária para recuperá-los com
          **cpio -i**.
-p        Lê nomes de arquivos da entrada padrão (stdin)
          e copia os arquivos para o diretório especificado.
-r        Renomeia arquivos interativamente. Um ponto
          (.) mantém o mesmo nome do arquivo, enter faz
          cpio ignorar o arquivo.
-s        Troca a posição dos bytes dos arquivos. Deve
          ser usada com -i.
-t        Cria uma tabela de conteúdo. Não copia arquivos.
-u        Copia incondicionalmente, substituindo arquivos
          homônimos que sejam mais novos.
-V        Lista o nome dos arquivos.

Exemplos:

	# Copia todos os arquivos listados pelo 
    # arquivo  texto arquivos.txt
	# para o arquivo de armazenamento arq.cpio.
	cpio -o < arquivos.txt > arq.cpio

	# Extrai todos os arquivos armazenados 
    # em arq.cpio.
	cpio -i < arg.cpio

