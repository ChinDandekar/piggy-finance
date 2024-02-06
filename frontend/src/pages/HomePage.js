import piggy from '../assets/piggy-construction.png';
import { TypeAnimation } from 'react-type-animation';
import { useBackend } from '../utils/useBackend';
import '../App.css';
import { LoginButton } from '../components/loginbutton';

/**
 * React component representing the main App.
 *
 * @component
 * @return {JSX.Element} The rendered App component.
 */
export default function HomePage() {

  var response = "couldn't connect to backend";

  const { data: dataResponse, error: _error, status: _status } =
  useBackend(
      // Stryker disable next-line all : don't test internal caching of React Query
      ["/get"],
      { method: "GET", url: "/get" },
      []
  );
  
  response = dataResponse;
  window.console.log("response: " + response['isLoggedIn']);



  if(!response.isLoggedIn)
  {
      return (
        <div className="Home">
        <header className="Home-header">
        <TypeAnimation
          sequence={[
            // Same substring at the start will only be typed once, initially
            'Welcome to Piggy Finance, no need to break the piggy bank',
            1000,
            'Welcome to Piggy Finance, turning your financial squeals into financial deals!',
            1000,
            'Welcome to Piggy Finance, your favorite pig mascot',
            1000,
            'Welcome to Piggy Finance, your personal financial planner',
            1000,
          ]}
          speed={50}
          style={{ fontSize: '2em' }}
          repeat={0}
        />
        </header>
        <div className="button-container">
        <LoginButton />
      </div>
      </div>
      );
  }
  
  return (
    <div className="Home">
      <header className="Home-header">
        <img src={piggy} className="Home-logo" alt="logo" />
        <p>
          Welcome, {response.name}
        </p>
      </header>
    </div>
  );
}