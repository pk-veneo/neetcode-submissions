class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for m in emails:
            local, domain = m.split("@")
            local = local.replace(".","")

            if "+" in local:
                local = local[:local.index("+")]
            seen.add(local + "@" + domain)
        return len(seen)


            



        