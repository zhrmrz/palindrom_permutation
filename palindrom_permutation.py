class Sol:
    def palindrom_permutation(self,string):
        x=0
        for char in string:
            c=string.count(char)
            if c%2==1:
                x+=1
        if x>1:
            return False
        return True


if __name__ == '__main__':
    p1=Sol()
    print(p1.palindrom_permutation('aab'))
