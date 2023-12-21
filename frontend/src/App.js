import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useBackend } from './utils/useBackend';



/**
 * React component representing the main App.
 *
 * @component
 * @return {JSX.Element} The rendered App component.
 */
function App() {

  var response = "couldn't connect to backend";

  const { data: dataResponse, error: _error, status: _status } =
  useBackend(
      // Stryker disable next-line all : don't test internal caching of React Query
      ["/api/get"],
      { method: "GET", url: "/api/get" },
      []
  );
  
  response = dataResponse;

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          response: {response}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
