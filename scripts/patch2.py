import re

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'r') as f:
    html = f.read()

# 1. Provide a more robust time calculation for "Mexico time"
# 2. Extract out the logic from renderCards and put it in DOMContentLoaded

original_code = """
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
"""

# remove it from renderCards
html = html.replace(original_code, "")

# inject it into DOMContentLoaded
new_code = """
function calculateDynamicStatus() {
    const mxTimeStr = new Date().toLocaleString("en-US", { timeZone: "America/Mexico_City" });
    const now = new Date(mxTimeStr);
    
    univData.forEach(u => {
        if (!u.fecha_limite) {
            u.estatus = 'cerrada';
            return;
        }
        // Limit date implicitly at 23:59:59
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
}

window.addEventListener('DOMContentLoaded', () => {
    calculateDynamicStatus();
    initCharts();
"""

html = html.replace("window.addEventListener('DOMContentLoaded', () => {\n    initCharts();", new_code)

with open('/home/boyfer/ws/mex-edu-info-2026/index.html', 'w') as f:
    f.write(html)
