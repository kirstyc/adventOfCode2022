class Folder():
    def __init__(self, name) -> None:
        self.files = {}
        self.folders = {}
        self.parent = None
        self.size = 0
        self.name = name

    def addFile(self, name, size):
        self.files[name] = size
        self.size += size 

    def addFolder(self, name):
        self.folders[name] = Folder(name)

    def addParent(self, parent):
        self.parent = parent

    
class FileSystem():
    DOWN = 'cd'
    UP = '..'
    DIR = 'dir'
    TOTAL = 70000000
    REQ_SIZE = 30000000
    def __init__(self) -> None:
        self.working_dir = Folder('root')
        self.sum = 0 

    def calc_diff(self, val):
        diff = val - self.target
        if diff < self.diff and diff > 0:
            self.diff = diff 
            self.closest = val


    def recursive_closest(self, dir):
        # assumes it will be a directory and not a single file 

        # check for no subdirs
        if len(dir.folders) == 0:
            self.calc_diff(dir.size)
            return
            
        # check if dir is exact match
        if dir.size == self.target:
            self.diff = 0
            self.closest = self.target
            return
        
        # check if dir is too small 
        if dir.size < self.target:
            return 
        
        # recursive call 
        for f in dir.folders.values():
            self.recursive_closest(f)

        # now check this folder 
        self.calc_diff(dir.size)

    def closest(self, target):
        self.closest = 0
        self.diff = target
        self.target = target
        self.recursive_closest(self.working_dir)
        return self.closest


    def total(self):
        total = self.working_dir.size
        while (self.working_dir.name != 'root'):
            self.working_dir = self.working_dir.parent

        for f in self.working_dir.folders.values():
            total += f.size

        return total


    def input(self, line):

        parse = line.split()

        if len(parse) == 3:
            cmd = parse[1]
            name = parse[2]

        else:
            cmd = parse[0]
            name = parse[1]

        if cmd.isnumeric():
            self.working_dir.addFile(name, int(cmd))

        if FileSystem.UP in line:
            if self.working_dir.size <= 100000:
                self.sum += self.working_dir.size
            self.working_dir.parent.size += self.working_dir.size
            self.working_dir = self.working_dir.parent

        elif FileSystem.DOWN in cmd:
            self.working_dir.folders[name].addParent(self.working_dir)
            self.working_dir = self.working_dir.folders[name]

        elif FileSystem.DIR in cmd:
            cmd, name = line.split()
            self.working_dir.addFolder(name)




if __name__ == "__main__":
    f = open('input.txt', 'r', encoding='utf-8')
    lines = f.readlines()

    sum = 0
    fs = FileSystem()
    # remove first line 
    lines.pop(0)
    for line in lines:
        line = line.strip()
        fs.input(line)

    if fs.working_dir.size < 100000:
        fs.sum += fs.working_dir.size

    total = fs.total()
    target = fs.REQ_SIZE - (fs.TOTAL - total)
    closest = fs.closest(target) 

    print(fs.sum)
    print(f"{total} {target} {closest}")



