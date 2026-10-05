class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for l in magazine:
            dic[l] = dic.get(l, 0) + 1
        print(dic)

        copy_dic = dic.copy()
        for i in range(len(ransomNote)):
            print(copy_dic)

            if ransomNote[i] in dic:
                if copy_dic[ransomNote[i]] >0:
                    copy_dic[ransomNote[i]] -= 1
                    print(copy_dic)
                    continue
                else :
                    return False
            elif ransomNote[i] not in dic:
                return False

                copy_dic[ransomNote[i]] -= 1
                print(copy_dic)
            # if any(v ==0  for v in copy_dic.values()):
            #     return True

        return True

                
        
