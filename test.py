import sys
print (u"脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):#这里参数从1开始
    print (u"参数", i, sys.argv[i])
