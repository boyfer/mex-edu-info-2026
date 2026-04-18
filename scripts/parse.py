import xml.etree.ElementTree as ET

tree = ET.parse('/tmp/mx-all.svg')
root = tree.getroot()

ns = {'svg': 'http://www.w3.org/2000/svg', 'hc': 'https://highcharts.com/docs/mc'}

state_map = {
    'Baja California': 'BC',
    'Baja California Sur': 'BCS',
    'Sonora': 'SON',
    'Chihuahua': 'CHIH',
    'Coahuila': 'COAH',
    'Nuevo León': 'NL',
    'Tamaulipas': 'TAMPS',
    'Sinaloa': 'SIN',
    'Durango': 'DGO',
    'Zacatecas': 'ZAC',
    'Aguascalientes': 'AGS',
    'San Luis Potosí': 'SLP',
    'Nayarit': 'NAY',
    'Jalisco': 'JAL',
    'Colima': 'COL',
    'Michoacán': 'MICH',
    'Guanajuato': 'GTO',
    'Querétaro': 'QRO',
    'Hidalgo': 'HGO',
    'México': 'MEX',
    'Estado de México': 'MEX',
    'Distrito Federal': 'CDMX',
    'Ciudad de México': 'CDMX',
    'Morelos': 'MOR',
    'Tlaxcala': 'TLAX',
    'Puebla': 'PUE',
    'Veracruz': 'VER',
    'Guerrero': 'GRO',
    'Oaxaca': 'OAX',
    'Chiapas': 'CHIS',
    'Tabasco': 'TAB',
    'Campeche': 'CAMP',
    'Yucatán': 'YUC',
    'Quintana Roo': 'QROO'
}

out_svg = []
import re

for path in root.findall('.//svg:path', ns):
    d = path.get('d')
    desc = path.find('hc:desc', ns)
    if desc is not None:
        name_elem = desc.find('hc:name', ns)
        if name_elem is not None and name_elem.text in state_map:
            abbr = state_map[name_elem.text]
            name = name_elem.text
            if name == 'México':
                name = 'Estado de México'
            if name == 'Distrito Federal':
                name = 'CDMX'
            out_svg.append(f'<path class="state-path" data-state="{abbr}" data-name="{name}" d="{d}" />')
            
            # Simple bounding box / centroid calculator
            coords = [float(c) for c in re.findall(r'-?\\d+\\.\\d+|-?\\d+', d)]
            if coords:
                xs = coords[0::2]
                ys = coords[1::2]
                cx = sum(xs) / len(xs)
                cy = sum(ys) / len(ys)
                # Adjust for specific states if needed
                if abbr == 'CDMX':
                    cy -= 10
                out_svg.append(f'<text class="map-label" data-state="{abbr}" x="{cx:.1f}" y="{cy:.1f}">{abbr}</text>')

vw = root.get('viewBox', '0 0 700 700')
print('ViewBox:', vw)
with open('/home/boyfer/ws/mex-edu-info-2026/new_map.svg', 'w') as f:
    f.write('\\n'.join(out_svg))

