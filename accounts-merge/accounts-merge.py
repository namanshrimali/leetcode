class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        for account in accounts:
            first_email = account[1]
            if first_email not in email_map:
                email_map[first_email] = []
            for email in account[2:]:
                email_map[first_email].append(email)
                if email in email_map:
                    email_map[email].append(first_email)
                else:
                    email_map[email] = [first_email]
        
        visited = set()
        def dfs(email):
            nonlocal email_list
            if email in visited:
                return
            visited.add(email)
            email_list.append(email)
            if email in email_map:
                for adj_email in email_map[email]:
                    dfs(adj_email)
        
        merged_accounts = []
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email in visited:
                continue
            email_list = []
            dfs(first_email)
            email_list.sort()
            email_list.insert(0, name)
            merged_accounts.append(email_list)
            
        return merged_accounts