#!/usr/bin/env python3

import pandoc
import fileinput
import sys 

NAME = 'guia-unix'
FORMATS = {'pdf': ['--toc', '--toc-depth=2', '-s'], 
           'epub': ['--toc', '--toc-depth=2', '-s'], 
           'html': ['--toc', '--toc-depth=2', '-s'], 
           'txt': [], 
           'rtf': ['--toc', '--toc-depth=2', '-s'], 
           'docx': ['--toc', '--toc-depth=2', '-s'], 
           'odt': ['--toc', '--toc-depth=2', '-s']
           }
FILES = [ 
         "src/0-intro.md",
         "src/1-arqs-dirs.md", 
          "src/1-arqs-dirs/awk.md", 
         "src/1-arqs-dirs/basename.md", 
         "src/1-arqs-dirs/cat.md", 
          "src/1-arqs-dirs/cd.md",
        "src/1-arqs-dirs/chgrp.md", 
          "src/1-arqs-dirs/chmod.md", 
          "src/1-arqs-dirs/cksum.md",
          "src/1-arqs-dirs/cmp.md", 
          "src/1-arqs-dirs/comm.md", 
          "src/1-arqs-dirs/compress.md",
          "src/1-arqs-dirs/cpio.md", 
          "src/1-arqs-dirs/cp.md", 
          "src/1-arqs-dirs/cut.md", 
          "src/1-arqs-dirs/dd.md",
          "src/1-arqs-dirs/df.md", 
          "src/1-arqs-dirs/diff.md", 
          "src/1-arqs-dirs/du.md",
          "src/1-arqs-dirs/file.md", 
          "src/1-arqs-dirs/find.md",
          "src/1-arqs-dirs/grep.md",
          "src/1-arqs-dirs/head.md", 
          "src/1-arqs-dirs/ln.md", 
          "src/1-arqs-dirs/ls.md",
          "src/1-arqs-dirs/mkdir.md",
          "src/1-arqs-dirs/mkfifo.md",
          "src/1-arqs-dirs/more.md",
          "src/1-arqs-dirs/mv.md",
          "src/1-arqs-dirs/paste.md",
          "src/1-arqs-dirs/patch.md",
          "src/1-arqs-dirs/pwd.md",
          "src/1-arqs-dirs/rmdir.md", 
          "src/1-arqs-dirs/rm.md",
          "src/1-arqs-dirs/sort.md",
          "src/1-arqs-dirs/split.md",
          "src/1-arqs-dirs/strings.md",
          "src/1-arqs-dirs/tail.md",
          "src/1-arqs-dirs/tar.md",
          "src/1-arqs-dirs/touch.md",
          "src/1-arqs-dirs/uncompress.md",
          "src/1-arqs-dirs/uniq.md",
          "src/1-arqs-dirs/uudecode.md",
          "src/1-arqs-dirs/uuencode.md",
          "src/1-arqs-dirs/vi.md",
          "src/1-arqs-dirs/wc.md",
        "src/2-terminal.md",
        "src/2-terminal/banner.md",
        "src/2-terminal/clear.md",
          "src/2-terminal/echo.md",
          "src/2-terminal/mesg.md",
          "src/2-terminal/stty.md",
          "src/2-terminal/talk.md",
          "src/2-terminal/tput.md",
          "src/2-terminal/tset.md",
          "src/2-terminal/tty.md",
          "src/2-terminal/wall.md",
          "src/2-terminal/write.md",
        "src/3-usrproc.md",
          "src/3-usrproc/atq.md",
          "src/3-usrproc/atrm.md",
          "src/3-usrproc/at.md",
          "src/3-usrproc/bg.md",
          "src/3-usrproc/env.md",
          "src/3-usrproc/fg.md",
          "src/3-usrproc/finger.md",
          "src/3-usrproc/groups.md",
          "src/3-usrproc/id.md",
          "src/3-usrproc/jobs.md",
          "src/3-usrproc/kill.md",
          "src/3-usrproc/last.md",
          "src/3-usrproc/login.md",
          "src/3-usrproc/logout.md",
          "src/3-usrproc/nice.md",
          "src/3-usrproc/nohup.md",
          "src/3-usrproc/passwd.md",
          "src/3-usrproc/ps-bsd.md",
          "src/3-usrproc/ps-sysv.md",
          "src/3-usrproc/su.md",
          "src/3-usrproc/users.md",
          "src/3-usrproc/whoami.md",
          "src/3-usrproc/who.md",
          "src/3-usrproc/w.md",
        "src/4-misc.md",
        "src/4-misc/apropos.md",
        "src/4-misc/biff.md",
          "src/4-misc/calendar.md",
          "src/4-misc/cal.md",
          "src/4-misc/crontab.md",
          "src/4-misc/date.md",
          "src/4-misc/false.md",
          "src/4-misc/hostname.md",
          "src/4-misc/lpr.md",
          "src/4-misc/man.md",
          "src/4-misc/sleep.md",
          "src/4-misc/tee.md",
          "src/4-misc/test.md",
          "src/4-misc/time.md",
          "src/4-misc/tr.md",
          "src/4-misc/true.md",
          "src/4-misc/uname.md",
          "src/4-misc/uptime.md",
          "src/4-misc/whatis.md",
          "src/4-misc/xargs.md",
          "src/4-misc/yes.md",
          "src/5-net/ftp.md",
          "src/5-net/lp.md",
      "src/5-net.md",
            "src/5-net/ftp.md",
          "src/5-net/mail.md",
          "src/5-net/rcp.md",
          "src/5-net/rsh.md",
          "src/5-net/ruptime.md",
          "src/5-net/rup.md",
          "src/5-net/rusers.md",
          "src/5-net/rwall.md",
          "src/5-net/rwho.md",
          "src/5-net/telnet.md",
          "src/5-net/whois.md",
          "src/6-outro/outro.md"
         ]

# used for debugging purposes
if len(sys.argv) > 1:
  FILES = filter(lambda x: x in sys.argv, FILES)
# make combined Markdown

with open("out/guia-unix.md", 'w') as mdfile:
    try:
        lines=fileinput.input(files=FILES)
        name=''
        for line in lines:
            oldname,name = name, lines.filename()
            if name != oldname:
                print(f'Reading file: {name}')
            mdfile.write(line)
    except UnicodeDecodeError as e:
        print (f'{lines.filename()}, {lines.lineno()}: {e}', file=sys.stderr)

print('Processing document')                
doc = pandoc.read(file="out/guia-unix.md", format="markdown")

for file_format,opts in FORMATS.items():
  print(f'Generating {file_format} output')
  pandoc.write(doc, file=f'out/{NAME}.{file_format}',options=opts)
