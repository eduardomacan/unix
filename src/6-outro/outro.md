# Correspondência DOS-UNIX

Esta tabela demonstra a correspondéncia entre alguns comandos do DOS e os comandos do Unix e nao uma equivaléncia. Os comandos do Unix sao, em geral, mais complexos e poderosos do que os correspondentes no MS-DOS.

 Comando do DOS    Correspondente UNIX
 --------------    --------------------
  ATTRIB           chmod             
  CD               cd
  CLS              clear
  COMP             diff
  COPY             cp
  DATE             date
  DEL              rm
  DELTREE          rm -rf
  DIR              ls
  ECHO             echo
  EDIT             vi
  EDLIN            ed
  HELP             man
  MD               mkdir
  MORE             more
  MOVE             mv
  PRINT            lp , lpr
  RD               rmdir
  REN              mv
  SORT             sort
  TIME             date
  TYPE             cat
  VER              uname -a
  XCOPY /S         cp -r

Table: Tabela simplificada de Correspondência DOS-UNIX


# Leitura Recomendada

- UNIX System Programming, Keith Haviland e Ben Salama, Addison-
Wesley Publishing.
- The UNIX System, S. R. Bourne, Addison-Wesley Publishing.
- The UNIX System V Environment, S. R. Bourne, Addison-Wesley
  Publishing.
- Modern Operating Systems, Andrew S. Tanembaum, Prentice Hall.
- Operating systems: Design and Implementation, Andrew S.
  Tanembaum, Prentice Hall.
- Computer Networks, Andrew S. Tanembaum, Prentice Hall.
- The C Programming Language, B. W. Kernighan e D. M. Ritchie,
  Prentice Hall .
- Internetworking with TCP/IP: Principles, Protocols and
  Architecture, D. Comer, Prentice Hall.

Obs: Parte destes titulos esta disponivel em portugués, consulte a
livraria mais proxima.

# WWW

Pagina oficial da lista de discussão linux-br, a maior 
e mais antiga do pais.

  ~ <http://www.openline.com.br/linux-br>

Lista de Usuários Avançados de Linux (lista fechada, 
inscrição mediante indicação).

  ~ <http://www.mondotech.com/lual>

Site oficial da linux international.

  ~ <http://www.linux.org>

Site oficial da freebsd.org no Brasil.

  ~ <http://www.br.freebsd.org>

O Site do Servidor X Free.

  ~ <http://www.xfree86.org>

Free Software Foundation.

  ~ <http://www.gnu.org>

Debian GNU/LINUX.

  ~ <http://www.debian.org>

Home page da lista Linux-BR.

  ~ <http://www.openline.com.br/linux-br>

Unix World on-line Magazine.

  ~ <http://unixworld.com/unixworld>

Unix Guru Universe.

  ~ <http://www.ugu.com>

Mirror brasileiro oficial da Sunsite.

  ~ <http://sunsite.unicamp.br>

Sunsite Archives.

  ~ <http://sunsite.unc.edu>

FTP Sites

Mirror dos pacotes GNU (Free Software Foundation).

  ~ <ftp://ftp.unicamp.br/pub/software/gnu>

GNU Software.

  ~ <ftp://ftp.unicamp.br/pub/gnu>

Arquivos da DICAS-L.

  ~ <ftp://ftp.unicamp.br/pub/dicas-1>

Internet RFC (Request For Comments).

  ~ <ftp://ftp.unicamp.br/pub/documents/rfc/>

# Listas de Discussão

listproc@netway.unicamp.br

  ~ Dicas-l, uma lista moderada com dicas periódicas valiosas para administradores.
Para se inscrever, envie para o endereço acima a mensagem:
subscribe dicas-l nome completo.

listproc@listas.ansp.br

  ~ Este servidor disponibiliza duas listas nacionais de grande importância, linux-br
e redes-l. Para se inscrever envie uma mensagem com os seguintes comandos:
subscribe linux-br nome completo.
subscribe redes-| nome completo.

petidomo@igm.unicamp.br
  ~ Este serrvidor distribui a lista FreeBSD-I. Para se inscrever, envie o comando add
FreeBSD no corpo do e-mail.

# Software Livre

Há alguns anos a Free Software Foundation (FSF) vem produzindo software
com qualidade no minimo equivalente à dos similares comerciais; o software é
desenvolvido por voluntários de várias partes do mundo e garante a liberdade do
usuário de redistribui-lo e modificá-lo, pois o código fonte está sempre disponível,
o que facilita a adaptação do código a várias plataformas.

Você pode encontrar seu programa "free" preferido, compilado para várias
arquiteturas e se não houver versão disponível para seu sistema, você poderá
tomar a iniciativa de portá-lo, sem depender do interesse comercial de uma grande
companhia.

A iniciativa de produção de software livre\*, patrocinada ou não pela FSF,
trouxe grandes contribuições ao público, entre elas os sistemas Unix free,
destacando-se Linux e FreeBSD.

Para saber mais sobre "free software" consulte as páginas da seção
Internet deste guia.

\* A tradução adequada de "free" para este caso é "livre" e não "grátis", pois o
usuário tem todaliberdade com o sofware. Os direitos de cópia são reservados ao autor,
que os cede ao interesse público. O software é pago mediante doação para o autor ou
instituição que detiver os direitos do software.

# A Respeito do Autor

Eduardo Marcel Maçan, natural de Santa Mariana - PR, ingressou no curso
de Engenharia de Computação da Universidade Estadual de Campinas (UNICAMP)
em 1992, tendo trabalhado desde então com administração e desenvolvimento
para o sistema Unix.

Fundador da lista de discussão linux-br, atualmente presta consultoria em
projeto, implantação e integração de redes, Intranet e Internetworking, suporte
Unix, desenvolvimento de material didático e cursos para a Mondo Technologies.

# Sobre Este Guia

Escrever um guia de consulta rápida para UNIX é uma tarefa no mínimo
desafiadora. Há inúmeras versões de UNIX, comerciais ou não, cada uma sendo
constantemente modificada de forma independente, sem muita preocupação de se
adotar (ou respeitar) padrões de desenvolvimento.

Esta desordem aliada à quantidade assombrosa de informação envolvida
nos comandos do sistema resulta na necessidade de se estabelecer critérios
quanto ao que é realmente útil em um guia de consulta rápida e a quem o mesmo
se destina.

Este guia foi escrito baseando-se na experiência do autor com vários
"sabores" de UNIX, a saber: Linux, FreeBSD, SunOS, Solaris, HP-UX, AIX e OSF/1
e nos manuais dos quatro primeiros. Visamos sempre a documentação do que era
comum a todas as versões de cada comando, delimitando desta forma um núcleo
de informação genérica o suficiente para que pudéssemos afirmar que este guia
será útil em qualquer versão de sistema e para toda classe de usuários.

Os iniciantes têm nesta seleção de comandos um volume de informações
bem além do essencial, a nível de usuário, e uma tabela de correspondência de
comandos que facilita muito a migração a partir de um ambiente DOS / Windows,
tornando possível o ingresso imediato no mundo de um dos mais completos e
fascinantes sistemas operacionais já desenvolvidos.

O texto deste guia foi inteiramente composto e editado usando free
software. O autor utilizou o sistema operacional Linux (Debian/GNU), XFree86
(sistema de janelas) e o editor de textos GNU Emacs (ainda estou tentando
convencer a editora a usar LaTeX para a formatação. :-)).

O autor deste guia pode ser contatado pela Internet, através do endereço:

E-Mail: macan@novatec1.com

Sugestões e comentários sobre este guia são sempre bem-vindos.

# Convenção Utilizada neste Guia
 
Convenção       Significado
---------       -----------
[ texto ]       Texto é opcional.
\<texto\>       Texto é obrigatório.
texto...        Texto pode ocorrer mais de uma vez.
texto1 | texto2 Texto1 etexto2 são alternativas mutuamente exclusivas.

# Licença

O conteúdo deste guia tanto no formato Markdown original quando nos formatos derivados de seu processamento (pdf, epub, etc) é regido pela licença Creative Commons [CC BY 4.0], o que significa que trabalhos derivados são permitidos, contanto que o autor original seja mencionado e receba os devidos créditos pelo material utilizado.

[CC BY 4.0]: https://creativecommons.org/licenses/by/4.0/

Os scripts utilizados para o preprocessamento do guia são licenciados sob a Licença MIT.

Copyright 2022 Eduardo M. Maçan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
