import re

class ContentCleaner:
    PATTERNS=[r"\bcookie\b",r"\bprivacy policy\b",r"\ball rights reserved\b"]

    def clean(self,text):
        for p in self.PATTERNS:
            text=re.sub(p,"",text,flags=re.I)
        return re.sub(r"\s+"," ",text).strip()
