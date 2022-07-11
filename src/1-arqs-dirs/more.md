## more

Mostra arquivos texto página a página.

Sintaxe: 

	more [-csu] [arquivo ...]

Parâmetro Descrição
--------- ---------
-c        Escreve a partir do topo da tela em vez de rola-
          la.
-s        Substitui múltiplas linhas em branco consecutivas
          por apenas uma.
-u        Trata caracteres de retrocesso (backspace) e
          sequéncias CR-LF de maneira especial.

Exemplo:

	# Útil para investigação de diretórios com muitas entradas.
	ls -la |more

	more /etc/passwd

