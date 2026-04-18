const fs = require('fs');

const html = fs.readFileSync('/home/boyfer/ws/mex-edu-info-2026/index.html', 'utf8');

// Extract univData
const univDataMatch = html.match(/const univData = (\[[\s\S]*?\]);/);
if (!univDataMatch) {
    console.log("univData not found!");
    process.exit(1);
}
const univDataStr = univDataMatch[1];

let univData;
eval("univData = " + univDataStr);

const stateToEstado = {
    'BC':'Baja California','BCS':'Baja California Sur','SON':'Sonora','CHIH':'Chihuahua',
    'COAH':'Coahuila','NL':'Nuevo León','TAMPS':'Tamaulipas','SIN':'Sinaloa','DGO':'Durango',
    'ZAC':'Zacatecas','AGS':'Aguascalientes','SLP':'San Luis Potosí','NAY':'Nayarit',
    'JAL':'Jalisco','COL':'Colima','MICH':'Michoacán','GTO':'Guanajuato','QRO':'Querétaro',
    'HGO':'Hidalgo','MEX':'Estado de México','CDMX':'CDMX','MOR':'Morelos','TLAX':'Tlaxcala',
    'PUE':'Puebla','VER':'Veracruz','GRO':'Guerrero','OAX':'Oaxaca','CHIS':'Chiapas',
    'TAB':'Tabasco','CAMP':'Campeche','YUC':'Yucatán','QROO':'Quintana Roo'
};

const appState = { category: 'all', status: 'all', query: '', selectedState: 'NL' };

let filtered = univData.filter(u => {
    const catOk = appState.category === 'all' || u.tipo === appState.category;
    const stOk = appState.status === 'all' || u.estatus === appState.status;
    const search = `${u.nombre} ${u.siglas} ${u.ubicacion} ${u.fortalezas} ${u.estado}`.toLowerCase();
    const qOk = search.includes(appState.query);
    let stateOk = true;
    if (appState.selectedState) {
        const estadoName = stateToEstado[appState.selectedState];
        stateOk = u.estado === estadoName;
    }
    return catOk && stOk && qOk && stateOk;
});

console.log("Filtered length:", filtered.length);
if (filtered.length > 0) {
    console.log("First item:", filtered[0].nombre);
}
