---
title: Installing Tex Live Full in Arch Linux
date: 2020-11-08
tags: [arch]
description: a work around on tex live installation
draft: false
---

You may encounter the following issues when installing text live full [from here](https://aur.archlinux.org/packages/texlive-full/)

and setting it up to work with `TextStudio`

```shell
# pacman -S texstudio
```

#### Error 1: No such file or directory

This error is shown when you run these series of command

```shell

# git clone https://aur.archlinux.org/texlive-full.git

# cd texlive-full

# makepkg -sri
```
```shell
WARNING: Using existing $srcdir/ tree
==> Entering fakeroot environment...
==> Starting package()...
/home/josphat/.cache/yay/texlive-full/PKGBUILD: line 29: /home/josphat/.cache/yay/texlive-full/src/install-tl-20200704/install-tl: No such file or directory
==> ERROR: A failure occurred in package().
    Aborting...
Error making: texlive-full
```

**The Fix/Work Around**
Change PKGBUILD'S file `pkgver` from `$date "+%Y%m%d"` to `pkgver="20200706"`.
You obtain this date from the downloaded directory path `texlive-full/src/install-tl-<date>`


### Error 2: xelatex command not found

Set Path to Tex Binaries permanently, in `.profile` file

```shell
export PATH="/opt/texlive/2020/bin/x86_64-linux:$PATH"
```

or else you can create this file ` texlive-full.sh ` in `/etc/profile.d/` before you begin installation as shown in error 1 above

```shell
_year=2020
[ -d /opt/texlive/${_year}/bin/x86_64-linux ] && export PATH=$PATH:/opt/texlive/${_year}/bin/x86_64-linux
[ -d /opt/texlive/${_year}/texmf-dist/doc/man ] && export MANPATH=:$MANPATH:/opt/texlive/${_year}/texmf-dist/doc/man
[ -d /opt/texlive/${_year}/texmf-dist/doc/info ] && export INFOPATH=:$MANPATH:/opt/texlive/${_year}/texmf-dist/doc/info

```
Then
```
$ source ~/.profile
```
or after login `$ tex --version` should show you the tex version verbose.


### Error 3: You can't compile the document in a non writable directory

If you run this series of commands to  make the directory where you`.tex` files reside writable.
As in

```shell
# su
# Password:
# chmod 0777 -R resume-cover-letter/
# ls -la .
```
This show the directory as writable
```
drwxr-xr-x 4 josphat josphat 4096 Jul  7 15:10 .
drwxr-xr-x 3 josphat josphat 4096 Jun 28 15:51 ..
drwxr-xr-x 6 josphat josphat 4096 Jun 28 22:17 configurations
drwxrwxrwx 5 josphat josphat 4096 Jul  8 08:44 resume-cover-letter
```
But it is bug in Arch,that texstudio flagged as won't fix.

http://sourceforge.net/p/texstudio/bugs/1814

**Work Around**
The work around is to compile the files via terminal
```
# xelatex cover-letter.tex
```


