def detailCpu_Mem():
    import os, re
    import platform
    cpu = 0.0
    memory = 0.0
    if platform.system() == 'Linux':
        os.system('ps -o %mem, ax |sort -b -k3 -r |head -150 >/opt/Tmp/detailcpu.txt')
        os.system('ps -o %cpu, ax |sort -b -k3 -r |head -150 >/opt/Tmp/detailmem.txt')
        detailcpu = open('/opt/Tmp/detailcpu.txt', "r")
        detailmem = open('/opt/Tmp/detailmem.txt', "r")
        for i in detailcpu:
            if not re.search("%CPU", i):
                cpu += float(i)
                print(i)
                if float(i) == 0.0:
                    break
        for i in detailmem:
            if not re.search("%MEM", i):
                memory += float(i)
                print(i)
                if float(i) == 0.0:
                    break
    elif platform.system() == 'Windows':
        print(platform.system())
        detailcpu = open('detailcpu.txt', "r")
        detailmem = open('detailcpu.txt', "r")
        for i in detailcpu:
            if not re.search('%CPU', i):

                cpu += float(i)
                print(i)
                if float(i) == 0.0:
                    break
        for i in detailmem:
            if not re.search('%MEM', i):

                memory += float(i)
                print(i)
                if float(i) == 0.0:
                    break
    return cpu


detailCpu_Mem()
