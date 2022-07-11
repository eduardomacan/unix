## df

Mostra dados de ocupação dos sistemas de arquivo especificados oudo
sistema de arquivo onde residem os arquivos passados como parâmetro.
Chamado sem parâmetros, df mostra a ocupação de todos os sistemas
de arquivos montados (mounted).

Sintaxe: 

	df[-k] [arquivo...] [filesystem...]

Parâmetro Descrição
--------- ---------
-k        Mostra a ocupação em kilobytes em vez de
          blocos de disco (algumas versões de df).

Exemplo:

	df /tmp / /var

