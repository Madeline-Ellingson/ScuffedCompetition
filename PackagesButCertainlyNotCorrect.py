class PKG:
    I, A, T, S, R = 0, 0, 0, 0, 0

    def __init__(self, str):
        I, A, T, S, R = str.split()
        self.I = int(I)
        self.A = int(A)
        self.T = int(T)
        self.S = int(S)
        self.R = int(R)


class PKG_set:
    pkgs = []
    indexs = []
    pkgs_del = []
    timestep = 1

    def append(self, PKG):
        self.pkgs.append(PKG)

    def isEmpty(self):
        if self.pkgs:
            return True
        else:
            return False

    def deliver(self, i):
        self.pkgs_del.append(self.pkgs[i])
        self.timestep += (2 * self.pkgs[i].T)
        self.pkgs.pop(i)

    def pop(self):
        self.pkgs.sort(key=lambda x: (x.R, x.S, -x.A), reverse=True)
        for i in range(len(self.pkgs)):
            if (self.pkgs[i].A <= self.timestep):
                self.deliver(i)
                return
            else:
                continue
        self.timestep += 1
        return self.pop()


if __name__ == '__main__':
    pkgs = PKG_set()

    numPKG = int(input())
    while numPKG > 0:
        str = input()
        pkgs.append(PKG(str))
        numPKG -= 1

    while pkgs.pkgs:
        pkgs.pop()

    for x in pkgs.pkgs_del:
        print(f"{x.I}")
