class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            if segment[0] != '0':
                return int(segment)<=255
            else:
                return len(segment)==1
        def form_ip(ip_arr = [], idx=0, part_remaining=4):
            nonlocal sol        
            if idx == len(s):
                if part_remaining == 0:
                    sol.append(''.join(ip_arr))
                return
            if not part_remaining <= len(s)-idx <= part_remaining*3:
                return
            i = idx+1
            segment = s[idx:i]
            while i<=len(s) and valid(segment):
                if part_remaining>1:
                    updated_ip_arr = ip_arr+[segment, '.']
                else:
                    updated_ip_arr = ip_arr+[segment]
                form_ip(updated_ip_arr, i, part_remaining-1)  
                i+=1
                segment = s[idx:i]
        sol = []
        form_ip()
        return sol
                
        