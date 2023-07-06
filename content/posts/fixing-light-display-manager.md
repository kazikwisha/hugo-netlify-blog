---
title: Fixing a crushing Light Display Greeter other than the service
date: 2020-11-08
tags: [troubleshooting]
description: how to fix a crushing Light Display Greeter
draft: false
---

Boot from Live USB

mount `root` partition
```
$ mount /dev/sda3 /mnt
```

Enter a chroot to the root directory, here in `/` mounted as `/mnt`

```
$ arch-chroot /mnt
```
Then execute this command

```
$ nano /etc/lightdm/lightdm.conf
```

Toggle the available greeters, this is to fix situations where one greeter crushes
such that you can't login to the system.

Gtk-greeter bit more stable than the other, but lacks major functionalities seen in the
others like webkit2 and patheon.

#### 1. Available Greeters
```
$ ls -1 /usr/share/xgreeters
```

#### 2. Gnome GTK
```
greeter-session=lightdm-gtk-greeter

user-session=gnome
```
#### 3. WebKit2
```
greeter-session=lightdm-webkit2-greeter

user-session=webkit2
```

#### 4. Cinnamon
```
greeter-session=lightdm-gtk-greeter

user-session=cinnamon-session-cinnamon

```



