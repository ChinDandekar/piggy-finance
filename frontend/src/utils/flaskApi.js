import axios from "axios";

const flaskApi = axios.create({
    baseURL: 'http://0.0.0.0:8000/', // Replace with your Flask app's URL
  });

export default flaskApi;