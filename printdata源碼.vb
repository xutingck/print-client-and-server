新建一个“标准EXE工程”，
然后在“工程资源管理器”窗口中的“Form1”上点鼠标右键，
在弹出的菜单中点“移除 Form1”。
第二步：在工程资源管理器窗口内点鼠标右键，依次点菜单“添加”→“添加模块”。
（这一步也可以在主菜单上操作：“工程”→“添加模块”　）
弹出的窗口中，直接点“打开”按钮。
第三步：在刚才打开的模块代码窗口中，输入：Sub Main　按回车键。
然后，继续输入你需要执行的代码到过程 Main内就行了。

Sub Main()
    Dim Str As String
    Open "D:\PRINT\printdata.dat" For Input As #1
    Do While Not EOF(1)
        Line Input #1, Str
        Printer.ScaleHeight = 1
        Printer.Print Str
    Loop
    Printer.EndDoc
    Close #1
End Sub
