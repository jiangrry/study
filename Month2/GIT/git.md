# GIT结构

    工作区：项目所在操作目录，实际操作项目区域
    暂存区：用于记录工作区的工作（修改）内容
    仓库区：用于备份工作区的内容
    远程仓库区：远程主机上的GIT仓库
    
    
# GIT基本命令
    1、初始化Git仓库 >>> git init
    2、查看当前分支状态 >>> git status
    3、将文件提交到暂存区 >>> git add file1 file2
    4、删除暂存区的文件 >>> git init git rm -cached file
    5、文件的移动删除 >>> git mv test/filename
    6、将暂存区内容保存提交 >>> git commit -m 'message'
    7、查看提交日记 >>> git log/git log --pretty=oneline 每个日志只显示一行
    8、查看当前文件和提交文件的差异 >>> git diff file
    9、删除暂存区的文件 >>> git init git rm -cached file
    
# 版本控制 
    1、回到上一版本 >>> git reset --hard HEAD^  
       回到上一版本用一个^,回到上两个版本就用^^,超过10个版本就用HEAD~10
       可以在git log下获取到commit_id信息，使用git reset --hard commit_id来进行回滚版本
    2、记录标签 >>> git tag [版本号]
        该操作会将版本号记录在分支上
       查看标签 >>> git show [版本号] 查看标签commit的具体内容
       删除标签 >>> git tag -d [版本号] 删除标签信息
       回复到版本号下的状态 >>> git reset --hard [版本号] 恢复到版本号下的标签状态
    3、