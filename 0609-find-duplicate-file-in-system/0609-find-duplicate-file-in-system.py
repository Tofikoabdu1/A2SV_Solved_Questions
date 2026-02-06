class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        p ={}
        for w in paths:
            first , second = w.split(" ",1)
            s = second.split()
            p[first] = s
        # print(p)
        files = p.values()
        # print(list(files))
        file_c = [x.split("txt" , 1) for x in files]
        print(file_c)


        