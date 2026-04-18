import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r"const stateToEstado = \{.*?(?<!:)NL':'([^']+)'.*?\}", text, re.DOTALL | re.IGNORECASE)
if m:
    print("stateToEstado NL:", repr(m.group(1)))
else:
    print("stateToEstado NL not found")

m2 = re.search(r'UANL.*?estado:"([^"]+)"', text)
if m2:
    print("univData UANL:", repr(m2.group(1)))
else:
    print("univData UANL not found")
