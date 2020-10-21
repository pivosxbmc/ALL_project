;等待
ControlFocus("打开","","Edit1")
WinWait("[CLASS:#32770]","",2)
;ControlSetText("打开","","Edit1","C:\Users\DELL\Pictures\Feedback\anxin.png")
Sleep(2000)
ControlClick("打开","","Button1")
MsgBox(0, "指南", "Hello World!3333333")


