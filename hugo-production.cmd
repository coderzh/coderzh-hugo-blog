@echo off 
rd /S /Q public

::git subtree add --prefix=public git@github.com:coderzh/coderzh-hugo-blog.git gh-pages --squash
::git subtree pull --prefix=public git@github.com:coderzh/coderzh-hugo-blog.git gh-pages

hugo -v  --cacheDir="./cache"

copy /Y copy_to_public\* public\

git add -A
git commit

git push origin master
git subtree push --prefix=public git@github.com:coderzh/coderzh-hugo-blog.git gh-pages

