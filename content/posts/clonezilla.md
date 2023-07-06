---
title: How to clone/restore partition to image
date: 2020-11-08
tags: [how-to]
description: how to clone & restore image using clonezilla
draft: true
---
## Notes to Self



### How to clone/restore partition to image
Probably you will want to clone `/home` partition to backup your data as well as
transfer it to another home partition in another computer.

Some of the things to recall when using [clonezilla](https://clonezilla.org/)
or rather [clonezilla live](https://clonezilla.org/clonezilla-live.php).

1. If you want to clone an image faster, a void compressing it.This save time

For instance cloning 120 GB partition takes 2 hours if the write speed is 1GB/minute.

As long as where you are writing your image has enough space to accomodate the image,you are good to go.

something greater than 120 GB will do for example.

2.  Accept to run `fsck` to fix some issues with inodes, blocks etc  to make your image restorable.

3. Choose `-k` - Do not Create a partition table on the target disk.Especially when restoring the parts.
   - You actually don't want to mess with your partition table hence you data that is already there.

4. Select the Parent Directory where the image will be cloned to/from.In other words,
   Don't select directly the `CMLZ`  image.Can't recall well the correct suffix of the image.

   TODO:
   Check it out next time.

5. When cloning from source linux to destination linux,you can avoid the option of selecting `ntfs`,since this
   represents the format for windows and you are not working with that.

   https://clonezilla.org/screenshots/?in_path=/00_Clonezilla

