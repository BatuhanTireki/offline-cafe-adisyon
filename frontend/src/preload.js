/**
 * Preload Script
 * Renderer ve Main process arasında güvenli köprü
 */

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    // Backend port'unu al
    getBackendPort: () => ipcRenderer.invoke('get-backend-port'),
    
    // Backend hazır olduğunda dinle
    onBackendReady: (callback) => {
        ipcRenderer.on('backend-ready', (event, data) => callback(data));
    }
});
