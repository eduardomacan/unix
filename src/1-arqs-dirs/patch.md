## patch

Atualiza arquivos com as modificações indicadas pela saída do comando
diff.

Sintaxe: 

	patch [arqorig]

Obs: **patch** lerá o arquivo de diferenças gerado por diff da entrada
padrão e o aplicará ao arquivo arqorig, gerando assim uma
versão idêntica do arquivo contra o qual arq1 foi comparado
por diff. Caso *argorig* não seja especificado, patch perguntará
ao usuário a qual arquivo devem ser aplicadas as alterações.

