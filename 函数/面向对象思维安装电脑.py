
class Cpu(object):
    def __init__(self,pinp,core,interface):
        self.pinp = pinp
        self.core = core
        self.interface = interface

class Ram(object):
    def __init__(self,pinp,size):
        self.pinp = pinp
        self.size = size


class Disk(object):
    def __init__(self,pinp,size):
        self.pinp = pinp
        self.size = size


class Computer(object):
    def __init__(self,cpu_interface,ram_count,disk_count):
        self.cpu_interface = cpu_interface
        self.ram_count = ram_count
        self.disk_count = disk_count
        self.__cpu = None
        self.__rams = []
        self.__disks = []



    def add_cpu(self,cpu):
        if cpu.interface == self.cpu_interface:
            self.__cpu = cpu
        else:
            print("cpu添加失败")

    def add_ram(self,ram):
        if len(self.__rams) == self.ram_count:
            print("不能添加内存")
        else:
            self.__rams.append(ram)

    def add_disk(self,disk):
        if len(self.__disks) == self.disk_count:
            print("不能安装硬盘")
        else:
            self.__disks.append(disk)

    def run(self):
        if not self.__cpu:
            return
        elif len(self.__rams) == 0:
            print("没有安装内存条")
        elif len(self.__disks) == 0:
            print("没有安装硬盘")
        else:
            print("电脑正常运行")

def main():
    compter = Computer('11211',2,2)

    cpu = Cpu('daier','2','11211')

    ram1 = Ram('daier','4GB')
    ram2 = Ram('daier','4GB')

    disk1 = Disk('daier','256GB')

    #组装电脑
    compter.add_cpu(cpu)
    compter.add_disk(disk1)
    compter.add_ram(ram1)
    compter.add_ram(ram2)

    compter.run()

if __name__ == '__main__':
    main()