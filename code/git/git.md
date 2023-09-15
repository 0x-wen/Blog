# Tutorial

## 1.参与开源项目

```shell
# 1.fork 目标仓库 -> 个人项目
# 2.git clone 个人项目
# 3.添加上游仓库例：
git remote add upstream git@github.com:microsoft/playwright.git
# 4.切换个人项目分支 
git checkout main
# 5.更新上游代码
git fetch upstream
# 6.合并代码至指定分支
git merge upstream/main
# 7.更新代码 保持目标库与个人库一致
git push

# 8.新建分支
git checkout -b xxx
# 9.开发 -> push 至个人仓库
# 10.提交pr  等待 review 通过合并至主分支
# 11.删除本地分支,同步上游 main 分支
```

## 2.拉取开源项目指定分支

```shell
git clone xxx

# 使用 git fetch 命令获取项目的最新标签信息。例如：
git fetch --tags

# 使用 git checkout 命令切换到指定标签。例如，如果您要切换到名为 v1.0.0 的标签，可以使用以下命令：
git checkout tags/v0.34.24

# 基于拉取的分支代码，创建新的分支，方便记录更改信息
git switch -c new_branch
```

## 3.强制拉取远程仓库代码

```shell
git fetch --all   # 从远程仓库获取最新的代码和分支信息。
git reset --hard  # 将本地代码重置为远程分支的最新版本。

# 注意，这些命令会覆盖本地未提交的更改，请谨慎使用。如果你有未提交的更改，可以先将它们提交或者暂存起来，再执行上述命令。

git fetch origin v7  # 从远程仓库获取 v7 分支的最新代码。
git reset --hard origin/v7  # 将本地代码重置为远程 v7 分支最新
```
