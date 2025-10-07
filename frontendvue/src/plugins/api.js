import axios from 'axios';

// Vite expõe variáveis que começam com VITE_ via import.meta.env.
// Permitir também um fallback para compatibilidade com outras convenções
// (por exemplo VUE_APP_API_BASE_URL) e, por fim, '/' como fallback seguro.
const base = import.meta.env.VITE_API_BASE_URL || import.meta.env.VITE_APP_API_BASE_URL || '/';
axios.defaults.baseURL = base;

export default axios;