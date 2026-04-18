const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('/home/boyfer/ws/mex-edu-info-2026/index.html', 'utf8');
const dom = new JSDOM(html, { runScripts: "dangerously" });

// Mock Canvas
dom.window.HTMLCanvasElement.prototype.getContext = function () {
    return {
        fillRect: function() {},
        clearRect: function() {},
        getImageData: function() { return { data: [] }; },
        putImageData: function() {},
        createImageData: function() { return []; },
        setTransform: function() {},
        drawImage: function() {},
        save: function() {},
        fillText: function() {},
        restore: function() {},
        beginPath: function() {},
        moveTo: function() {},
        lineTo: function() {},
        closePath: function() {},
        stroke: function() {},
        translate: function() {},
        scale: function() {},
        rotate: function() {},
        arc: function() {},
        fill: function() {},
        measureText: function() { return { width: 0 }; },
        transform: function() {},
        rect: function() {},
        clip: function() {}
    };
};

// Mock Element.scrollIntoView
dom.window.Element.prototype.scrollIntoView = function() {};

dom.window.addEventListener('load', () => {
    try {
        console.log("Calling selectState directly for NL!");
        dom.window.selectState('NL', 'Nuevo León');
        
        const grid = dom.window.document.getElementById('universityGrid');
        console.log("Grid cards appended:", grid.children.length);
        if (grid.children.length > 0) {
            console.log("Is grid hidden?", grid.className.includes('hidden'));
        }
        const noResClass = dom.window.document.getElementById('noResults').className;
        console.log("NoResults visible?", !noResClass.includes('hidden'));
    } catch(e) {
        console.error("Caught error:", e);
    }
});
