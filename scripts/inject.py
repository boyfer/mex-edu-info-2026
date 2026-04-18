import re

with open('/home/boyfer/ws/mex-edu-info-2026/new_map.svg', 'r') as f:
    svg_content = f.read()

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'r') as f:
    html = f.read()

pattern = re.compile(r'<svg id="mexicoMap" viewBox="[^"]+" xmlns="http://www.w3.org/2000/svg">.*?</svg>', re.DOTALL)

new_svg = f'<svg id="mexicoMap" viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg">\n{svg_content}\n</svg>'

new_html = pattern.sub(new_svg, html)

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'w') as f:
    f.write(new_html)
