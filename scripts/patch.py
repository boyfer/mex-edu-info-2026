import re

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'r') as f:
    html = f.read()

# Patch renderCards logic
# Remove || u.estado === 'Nacional' to fix the filtering bug
html = html.replace("stateOk = u.estado === estadoName || u.estado === 'Nacional';", "stateOk = u.estado === estadoName;")

# Add logic for current date evaluation
status_script = """
    // Calculate estatus dynamically
    const now = new Date();
    univData.forEach(u => {
        // Simple heuristic: we have manually injected fecha_limite below
        if (!u.fecha_limite) {
            u.estatus = 'cerrada';
            return;
        }
        const limitDate = new Date(u.fecha_limite + 'T23:59:59');
        const diffMs = limitDate - now;
        const diffDays = diffMs / (1000 * 60 * 60 * 24);
        
        if (diffDays < 0) {
            u.estatus = 'cerrada';
        } else if (diffDays <= 14) {
            u.estatus = 'cerca de terminar';
        } else {
            u.estatus = 'abierta';
        }
    });

    let filtered = univData.filter(u => {
"""
html = html.replace('let filtered = univData.filter(u => {', status_script)

# Add fecha_limite to univData
# Let's do it via simple regex injection
replacements = {
    'UNAM': '2026-02-03',
    'IPN': '2026-03-20',
    'UDG': '2026-02-28',
    'UANL': '2026-04-23',
    'UAM': '2026-02-20',
    'BUAP': '2026-05-15',
    'UASLP': '2026-05-31',
    'UAEMex': '2026-02-24',
    'UV': '2026-02-27',
    'UG': '2026-02-28',
    'UAQ': '2026-05-31',
    'UAEH': '2026-04-26',
    'UADY': '2026-03-15',
    'ITESM': '2026-06-05',
    'ITAM': '2026-06-01',
    'IBERO': '2026-08-01',
    'UP': '2026-05-31',
    'UDLAP': '2026-06-01',
    'ANÁHUAC': '2026-07-31',
    'UDEM': '2026-05-31',
    'ULSA': '2026-07-30',
    'ITESO': '2026-08-01',
    'UVM': '2026-08-15',
    'UNITEC': '2026-08-30',
    'UABJO': '2026-04-29',
    'UTM': '2026-06-26',
    'UMAR': '2026-06-26',
    'URSE': '2026-08-01',
    'ANÁHUAC OAX': '2026-07-31',
    'UNSIS': '2026-05-25',
    'UNPA': '2026-05-25'
}

for siglas, date_str in replacements.items():
    html = re.sub(rf'(siglas:"{siglas}",)', rf'\1 fecha_limite:"{date_str}",', html)

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'w') as f:
    f.write(html)
