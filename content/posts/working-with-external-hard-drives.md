---
title: Fixing NTFS hard drive that refuses to mount
date: 2020-11-08
tags: [troubleshooting]
description: how to fix NTFS hard drive that refuses to mount
draft: false
---

This could be that is is not automounting coz of an error to do
with bad sectors etc.

```shell
$ yes | sudo pacman -S ntfs-3g

```
Then

```
$ sudo ntfsfix /dev/sdX
```
where `/dev/sdX` is the Hard Drive e.g `/dev/sdd1`

###  Checking the type of your mounted partitions or devices

```shell
$ sudo blkid /dev/sdd
```
Where `/dev/sdd1` is your

### Check your mounted partitions/devices
```shell
$ cat /proc/mounts
```
or

```shell
$ cat /etc/fstab
```
### mount device(hard drive) using terminal
```
$ sudo mount -t ntfs /dev/sdd1 /mnt
```
### unmount device from  using terminal 

```shell
$ sudo umount /dev/sdd1
```