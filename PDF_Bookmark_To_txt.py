# -*- coding: utf-8 -*-
import sys
import os
import glob

from PdfBookmark import PdfBookmark

#show version
vn='1.0.1'
print("Version:"+vn)
print('============================================')
# 要檢查的目錄路徑
folderpath = "PDF/"

# 檢查目錄是否存在，
if not os.path.isdir(folderpath):
  try:
   os.makedirs(folderpath)
# 檔案已存在的例外處理
  except FileExistsError:
   print("file exist!")

for files in glob.glob(folderpath +"*.pdf"):
   exportFile=os.path.splitext(files)[0]+"_bookmark.txt"
   bm1 = PdfBookmark(files)
   bm1.exportBookmark(exportFile)

print("done") 
os.system('pause')


