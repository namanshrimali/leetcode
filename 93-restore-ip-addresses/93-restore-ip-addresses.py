class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def form_ip(ip_arr = [], idx=0, part_remaining=4):
            nonlocal sol            
            if idx == len(s):
                if part_remaining == 0:
                    sol.append(''.join(ip_arr))
                return
            
            if s[idx]=='0':
                if part_remaining>1:
                    updated_ip_arr = ip_arr+[s[idx], '.']
                else:
                    updated_ip_arr = ip_arr+[s[idx]]
                form_ip(updated_ip_arr, idx+1, part_remaining-1)
                
            else:
                i = idx+1
                while i<=len(s) and i-idx<=3 and int(s[idx:i])<=255:
                    if part_remaining>1:
                        updated_ip_arr = ip_arr+[s[idx:i], '.']
                    else:
                        updated_ip_arr = ip_arr+[s[idx:i]]
                    
                    form_ip(updated_ip_arr, i, part_remaining-1)
                    
                    i+=1
        sol = []
        form_ip()
        return sol
                
        