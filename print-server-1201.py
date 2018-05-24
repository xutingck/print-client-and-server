#-*- coding: UTF-8 -*-
import socket, time, SocketServer, struct
import os, thread, random, re, win32api, win32print, datetime

host = ''
port = 12305

def renamefile():
    time.sleep(2)
    filepath1 = os.getcwd()
    print filepath1
    filename = 'logtext.txt'
    hostname = socket.gethostname()
    nowtime = str(datetime.datetime.now())
    nowtime = re.sub(':', '-', nowtime)
    print 'Rename logtext.txt file time :', nowtime
    logfile.write('\nRename logtext.txt file time :%s'%nowtime)
    newname = str(hostname) + str('@') + str(nowtime) +str('logtext.txt')
    print "New name :", newname
    logfile.write('\nNew name: %s' % newname)
    old_name = os.path.join(filepath1, filename)
    new_name = os.path.join(filepath1, newname)
    os.system(str(str('attrib -s -h /s ')+ str(old_name)))
    os.rename(old_name, new_name)
    print "\nRename finish."
    logfile.write("\nRename finish.")

def printer():
    win32api.ShellExecute(0, #父窗口的句柄，如果没有，则为0
                          'open',#操作，为open或print
                          'D:\\PRINT\\printdata.exe',#要运行的程式或脚本
                          '',#要向窗口传递的参数，如果打开的是文件则为空
                          '',#程序初始化的目录
                          0)#是否显示窗口，0否，1是
    time.sleep(3)
    #sleep(3) 等待打印完成
    """
    path1 = os.getcwd()
    thefilename1 = filenewname
    thefilename2 = os.path.join(path1,thefilename1)
    f = open(thefilename2, 'rb')
    
    printer_name = win32print.GetDefaultPrinter ()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32print.StartDocPrinter(hPrinter, 1, ("SCY Detection DATA", None, 'raw'))
    # raw_data could equally be raw PCL/PS read from some print-to-file operation
    win32print.StartPagePrinter(hPrinter)
    
    while True:
        writedata1 = f.readline()
        writedata2 = re.sub("   ", " ", writedata1)
        writedata2 = re.sub("--", "-", writedata2)
        print writedata2
        if writedata2 != "":
            win32print.WritePrinter(hPrinter, writedata2)
        else:
            break
    
    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)
    win32print.ClosePrinter(hPrinter)
    """
def conn_thread(connection , address): 
    try:            
        path1 = os.getcwd()
        connection.settimeout(10)            
        fileinfo_size = struct.calcsize('128sl') 
        buf = connection.recv(fileinfo_size)
        if buf:
            filename , filesize =struct.unpack('128sl',buf) 
            timenow = datetime.datetime.now()
            global filenewname
            filenewname = './PRINTDATA.DAT'
            logfile.write(str(timenow) + str('\n'))
            print 'File is %s, filesize is %s \n' %(filenewname , filesize)            
            recvd_size = 0
            filetoprint = open(filenewname,'wb')
            filetoprint.write('\n- - - - - - - - - - - - - - - - - -\n')
            logfile.write(str('Start receiving ...\n'))
            print 'Start receiving ...'
                
            while not recvd_size == filesize:
                if filesize - recvd_size > 4096:
                    rdata = connection.recv(4096)
                    recvd_size += len(rdata)
                else:
                    rdata = connection.recv(filesize - recvd_size) 
                    recvd_size = filesize
                filetoprint.write(rdata)
            filetoprint.close()
            printer()
            os.remove(filenewname)
            logfile.write(str('Receive and Print done ...\n'))
            print 'Receive and Print done ...'
            logfile.close()
            bigsize = os.path.getsize('./logtext.txt')
            if bigsize > 1000000000 :
                renamefile()
            
    except socket.timeout():
        connection.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(12)
print 'Waiting for connect...'
        
while True:
    try:
        connection , address = s.accept()
        time_now = datetime.datetime.now()
        print time_now
        print 'Connected by {x} at {y}'.format(x = address, y = time_now)
        print '-- -- -- -- -- -- -- -- -- -- -- -- --'
        logfile = open('./logtext.txt', 'a+')
        logfile.write(str('Connected by {x} at {y}.\n'.format(x = address, y = time_now)))
        thread.start_new_thread( conn_thread , (connection , address) )        
    except:
        pass

s.close()
