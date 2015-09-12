@echo off 
rd /S /Q public
md public

hugo server -w -v
