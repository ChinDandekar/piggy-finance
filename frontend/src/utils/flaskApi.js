import axios from "axios";

const apiUrl = process.env.REACT_APP_API_URL;
console.log('API URL:', apiUrl); // https://api.example.com

const flaskApi = axios.create({
    baseURL: apiUrl, // Replace with your Flask app's URL
  });

export default flaskApi;