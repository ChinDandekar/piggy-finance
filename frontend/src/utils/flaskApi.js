// flaskApi.js
import axios from 'axios';

const flaskApi = axios.create({
    baseURL: 'http://0.0.0.0:8000/',
});

export default flaskApi;