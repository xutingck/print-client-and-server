#coding:UTF-8
import socket, os, struct, re, time, datetime

time_now = datetime.datetime.now()
print " <-- <-- <-- START --> --> --> "
print "Version : 2017-11-27, JY IT."
print "Welcome to use."

filepath = "./TEXTDATA.txt"
listtxt = []
count = 0

with open("./IPconfig.bin", 'r') as f:
    serverIP = f.readline()

def renamefile():
    time.sleep(2)
    filepath1 = os.getcwd()
    print filepath1
    filename = 'logtext.txt'
    hostname = socket.gethostname()
    nowtime = str(datetime.datetime.now())
    nowtime = re.sub(':', '-', nowtime)
    print 'rename logtext.txt file time :', nowtime
    #logfile.write('\nrename logtext.txt file time :%s'%nowtime)
    newname = str(hostname) + str('@') + str(nowtime) +str('logtext.txt')
    print "New name :", newname
    #logfile.write('\nNew name: %s' % newname)
    old_name = os.path.join(filepath1, filename)
    new_name = os.path.join(filepath1, newname)
    #print old_name, new_name
    os.rename(old_name, new_name)
    print "\nRename finish."
    #logfile.write("\nRename finish.")

def transmission():
    logfile.write('Start to connect.')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((serverIP, 12305))
    
    print "成功連接服務器。".decode('utf-8').encode('big5')
    logfile.write('\nConnect sucessfully.')
    fileinfo_size = struct.calcsize('128sl')        
    fhead = struct.pack('128sl',os.path.basename(filepath),os.stat(filepath).st_size)
    s.send(fhead)
    timenow = datetime.datetime.now()
    print ('結果文件將被發送...%s'%timenow).decode('utf-8').encode('big5')
    logfile.write(str('\n') + str(timenow))
    logfile.write(str("\n") + str(filepath) + str('is sending...'))
    fo = open(filepath,'rb')
    while True:
        filedata = fo.read(4096)
        if not filedata:
            break
        s.send(filedata)
    fo.close()
    print '結果文件被發送。'.decode('utf-8').encode('big5')
    logfile.write(str('\nFile send.'))
    s.close()

def try_transmission():
    try:
        transmission()
    except:
        print "失敗！！！沒有連上服務器，是不是沒有網絡？結果將不會被打印，請手抄結果。".decode('utf-8').encode('big5')
        logfile.write("\nFAIL!!! CANN'T CONNECT TO SERVER NOW, PLEASE WRITE THE RESULT ON A PAPER!!!")
        pass

def do():
    # 把TEXTDATA写入到logfile
    f = open(filepath, 'rb')
    copyfile = str('\n\n') + str(f.readlines()) +str('\n\n')
    f.close()
    logfile.write( copyfile )
    # 打开TEXTDATA，并判断传送不传送；
    # 如果是OK的，不传；
    # 如果是NG的，传送给服务端打印。
    f = open(filepath, 'r')
    while True:
        line = f.readline()
        print "line1 :", line
        if line == "":
            f.close()
            #renamefile()
            os.system(str(str('attrib -s -h /s ')+ str(filepath)))
            os.remove(filepath)
            break
        if '----' in line:
            line = f.readline()
            print "line2 :",line
            print '上面為line2檢測結果。'.decode('utf-8').encode('big5')
            if line != "" and line != "\n":
                f.close()
                print '文件關閉。'.decode('utf-8').encode('big5')
                print '開始連接服務器，並打印文件。'.decode('utf-8').encode('big5')
                try_transmission()
                #renamefile()
                #print "Rename finish."
                os.system(str(str('attrib -s -h /s ')+ str(filepath)))
                os.remove(filepath)                
                print '刪除結果文件。'.decode('utf-8').encode('big5')
                break
            else:
                print "line2檢測結果為空的，產品檢測為OK，或，檢測結果有NG，但最終被認定為OK，將不會打印出結果。".decode('utf-8').encode('big5')
                break


def ifthereisvalue():
    if os.path.isfile(filepath):
        time.sleep(5)
        print '結果文件存在，如果結果為達到不良標準，將被打印。'.decode('utf-8').encode('big5')
        logfile.write('\nFILE EXIST.')
        #print 'LISTTXT, ', listtxt
        #logfile.write('\nLISTTXT, %s' % listtxt)
        listtxt.append(os.path.getmtime(filepath))
        # 以下两个if-else是为判断TEXTDATA是否为同一个文件，
        # 如果是新的文件，就执行传送动作，如果不是，就不传送。
        if len(listtxt) >= 2:
            if listtxt[-1] == listtxt[-2]:
                #print 'listtxt 2, ', listtxt
                logfile.write('\nlisttxt 2, %s'% listtxt)
                k = len(listtxt) - 2
                for i in range(0, k):
                    listtxt.remove(listtxt[i])
                print 'ifthereisvalue() stop.檢測結果文件重複或被打開，將強制刪除。 '.decode('utf-8').encode('big5')
                logfile.write('\n')
                os.system(str(str('attrib -s -h /s ')+ str(filepath)))
                os.remove(filepath)
                print '文件重複或文件被非正常打開，現在將其關閉並移除。'.decode('utf-8').encode('big5')
            else:
                #print 'do 2'
                do()
        else:
            #print 'do 1'
            do()


while True:
    try:
        logfile = open('./logtext.txt', 'a+')
        time4 = datetime.datetime.now()
        #logfile.write('\n{c} time(s), {t}.'.format(c = count, t = time4))
        ifthereisvalue()
        count += 1
        time5 = datetime.datetime.now()
        print '{c} 次完成, 在{t}。'.format(c = count, t = time5).decode('utf-8').encode('big5')
        logfile.write('\n{c} time(s) finish @ {t}.'.format(c = count, t = time5))
        time.sleep(20)
        logfile.close()
        bigsize = os.path.getsize('./logtext.txt')
        if bigsize > 1000000000 :
            renamefile()
    except:
        pass
