# _*_ coding: utf-8 _*_
#python setup.py py2exe
import py2exe
from distutils.core import setup
import sys
from glob import glob

sys.path.append('G:\\pythonproject\\Microsoft.VC90.CRT')
 
data_files = [("Microsoft.VC90.CRT", glob(r'G:\\pythonproject\\Microsoft.VC90.CRT\\*.*'))]

includes = ['encoding', 'encodings.*']

options = {"py2exe":
           {'compressed': 1,
            # compressed:,布尔类型：是否压缩‘library.zip’，建议压缩写2，不压缩写0
            'optimize': 2,
            # optimize:,string或者int类型的优化等级（0，1，2）
            # optimize:,0=不优化（产生.pyc）1=正常优化（就像python -O）2=高度优化（像python -OO）
            # optimize:,详细信息参阅：http://docs.python.org/distutils/apiref.html#module-distutils.util
            'ascii': 1,
            # ascii:,布尔类型：不要自动包含编码和解码器
            'includes': includes,
            # includes:,列表：需要包含模块的名字
            # 'bundle_files': 1,
            # bundle_files:,将dll打包进zipfile或者exe中。
            # bundle_files:,有效的值为：3=不打包（默认值）2=打包所有除了python解释器 1=打包所有包括python解释器
            # unbuffered:,如果True，使用没有缓存的stdout和stderr           
            # packages:,列表：需要包含的包和子包
            # ignores:,列表：如果找不到便可以忽略的模块
            # excludes:,列表：不需要包含的库名字
            "dll_excludes" : ["D:\\Python27\\Lib\\socket.pyc"],#系統自帶socket？包含了反而出錯
            # dll_excludes:,列表：不需要包含的dll
            # dist_dir:,编译最终文件的目录
            # typelibs:,列表：需要包含的gen_py产生的typelibs            
            # xref:,布尔类型：创建并显示一个模块的交叉引用
            # skip_archive:,布尔类型：不要将python的字节码文件归档，直接把他们放到文件系统里            
            # custom-boot-script:,当运行环境建立起来后运行的python文件
           }
         }
 
setup(data_files = data_files,
      version='0.2017.12.1',
      console = [{ 'script': 'G:\\pythonproject\\print-Project\\1130\\print-client1129-big5.py',
                  'icon_resources':[(1, 'G:\\pythonproject\\print-Project\\1125\\booktime.ico')] }],
      description = 'print-CLIENT-1201,utf8,XuTing',
      name = "print-CLIENT-1201"
      )
