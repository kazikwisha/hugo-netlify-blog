### Blog
An experimental personal blog.

### Step 1: Pre - requisites

- Ensure you have installed hugo and the following pre-requisites

Am using Arch, check the equivalent for your distro.

```shell
$ sudo pacman -Syy && sudo pacman -S hugo

$ hugo version
```

```shell
$ ldd --version
```
```shell
$ sudo pacman -S glibc
```
### Step 2: Checkout a branch

- Checkout the right branch as per your requirement

The branches are:

- wip  :     Works in progress; stuff I know won't be finished soon
- feat :     Feature I'm adding or expanding
- bug  :     Bug fix
- draft :    Experimenting branch - where you can add a post with no intention of publishing.Ensure in the article metadata is false i.e `draft : false`

```shell
$ git checkout  draft
```

###  Step 3: How to Build and Run

**Make  all the necessary changes and build the site**

- Build site + drafts

```shell
$ make build_all
```
- Build site

```shell
$ make build
```
- Clear Cache
```shell
$ make clean
```
- View site locally
Navigate to `http://localhost:1313`

- If you're satisfied with what you see, then:

    - Check what you are committing

    `git status`

0. Stage & commit

    `git add . && git commit -m "<commit-messsage>"`

### Step 4: Checkout main branch, merge your branch and push the changes to remote

1.  Switch to main branch

    - Switch to the main branch

    `git checkout main`

2. Pull latest changes from remote

    - Set the latest changes for main

    `git pull origin main`

3. Merge changes

    - Then merge changes from your branch to `main`

    `git merge draft`

4. Push changes

    - Push changes to the remote repo.

    `git push origin main`

### View Site

- View the deployed [live](https://xbns.netlify.app site.


