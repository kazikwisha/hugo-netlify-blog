---
title: Booting from Live USB Probook 4540s Hp Laptop
date: 2020-11-08
tags: [troubleshooting]
description: how to fix the issue on booting from live USB
draft: false
---


#### Issue:Unable to boot from live USB

1. Press `ESC` to interrupt booting process.
2. Press `F10` "BIOS SetUp"
3. Navigate to `System Configuration` with Arrow Keys.
4. Select `Boot Options` and press Enter.
5. Under `Boot Mode`,Select UEFI(with CSM).
6. Under `UEFI Boot Order`, ensure Generic USB is the first choice.
7. Save your settings and Exit.
8. Now press `ESC` again while system boots.
9. Press `F9` to select Boot Device Options.
10. Select "USB Hard Drive" 