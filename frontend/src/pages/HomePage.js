import logo from '../logo.svg';
import { useBackend } from '../utils/useBackend';
import '../App.css';

/**
 * React component representing the main App.
 *
 * @component
 * @return {JSX.Element} The rendered App component.
 */
export default function HomePage() {

  var response = "couldn't connect to backend";

  console.log('About to make GET request to /get');
  const { data: dataResponse, error: _error, status: _status } =
  useBackend(
      // Stryker disable next-line all : don't test internal caching of React Query
      ["/get"],
      { method: "GET", url: "/get" },
      []
  );
  
  response = dataResponse;
  window.console.log("response: " + response['message']);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          response: {response['message']}
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