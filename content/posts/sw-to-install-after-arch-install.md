---
title: Configure cinnamon desktop with nemo in arch system
date: 2020-11-17
tags: [arch]
description: software to install after arch installation
draft: false
---

### 1 Install Vivaldi as alternate browser
```bash
# pacman -S vivaldi
```

### 2 Mount Google Drive on Linux

https://www.omgubuntu.co.uk/2017/04/mount-google-drive-ocamlfuse-linux

Then configure it at start up

Add the following custom command for "Startup Applications".


`google-drive-ocamlfuse /home/<username>/googledrive`



### 3 Install Nemo Plugins
Nemo is the default file manager for cinnamon but you may need to install the following plugins.

```bash
# pacman -S nemo-fileroller nemo-preview
```
- nemo-fileroller - support compressed file formats (zip, tar, gz)
- nemo-preview - press the spacebar to view a preview of the selected file.

i usually install `zip` and `unrar` separately incase i may want to purge everything nemo in future and use windows manager like `i3`.

For uncompressing `tar.gz` files, `bstar` comes installed by default in arch.


### 4 Show and Enable Cinnamon Desktop Icons 
Press WinKey,then Search (System Settings)

System Settings --> Desktop

Enable the following Desktop Icons
- Computer
- Home
- Trash
- Mounted Drives


Then run below command to enable the desktop icons for easier navigation

```bash
$ sudo gsettings set org.nemo.desktop show-desktop-icons true
```

Ensure you change the default file manager to nemo

```bash
$ sudo nano /usr/share/applications/mimeinfo.cache
```
Change `inode/directory=nemo.desktop`

### 5 Install Lepton for Github Gists
https://snapcraft.io/install/lepton/arch
