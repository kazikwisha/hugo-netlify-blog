---
title: Performing a  zero fill using a live USB
date: 2020-11-08
tags: [troubleshooting]
description: how to perform a zero fill using a live USB
draft: false
---

```shell
$ sudo shred -n 2 -z -v /dev/sda
```

Verify the device by listing `fdisk -l`

- `-n` is the number of passes.
- `-z` will zero your drive.
- `-v` will display the progress of shred as it works

SSD owner should use 1 pass instead of 2 if they want to reuse the drive.

### Wipe Disk

```shell
$ sudo parted /dev/sda --align opt mklabel gpt 0 931.53G
```

You may get this warning:
The disk label on `/dev/sda` will be destroyed and all data will be lost.
You want to continue?
Yes/No
Type `Yes` if sure, otherwise `No`

Go Back to verify the device using `fdisk -l`

### Check Disk Usage
```shell
$ sudo df -h
```

```
$ sudo df -h -t ext -t vfat -t swap
``` 