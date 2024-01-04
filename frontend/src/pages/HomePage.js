import under_construction from '../assets/under-construction.png';
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
        <img src={under_construction} className="App-logo" alt="logo" />
        <p>
          This website is currently under development. Please check back later for updates.
        </p>
        <a
          className="Repo-link"
          href="https://github.com/ChinDandekar/piggy-finance"
          target="_blank"
          rel="noopener noreferrer"
        >
          GitHub Repository
        </a>
      </header>
    </div>
  );
}