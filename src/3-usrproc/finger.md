## finger

Mostra informações sobre usuários locais ou remotos.

Sintaxe: finger [-Imsp] [usuário ...]

 

Parâmetro Descrição
-| Saida em formato longo.
-m Compara apenas o nome de login do usuário e
não seu nome completo.
-s Força a saída em modo simplificado (short).
-p Não imprime o arquivo .plan do usuário.
Obs: Os usuários podem ser especificados pelos userids (ou login

names) para usuários locais, ou usuário Qnome.da.maquina
para usuários de máquinas remotas.

Exemplos:
finger root

finger president@whitehouse.gov

