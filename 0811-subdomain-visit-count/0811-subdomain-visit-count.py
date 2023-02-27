from collections import defaultdict 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_counts = defaultdict(int) 
        for count_domain in cpdomains: 
            count, domain = count_domain.split() 
            count = int(count) 
            all_domains = domain.split('.') 
            for ix in range(len(all_domains)):
                domain = '.'.join(all_domains[ix:]) 
                subdomain_counts[domain] += count 
        result = [] 
        for domain, count in subdomain_counts.items(): 
            result.append(str(count) + ' ' + domain) 
        return result 
            
        