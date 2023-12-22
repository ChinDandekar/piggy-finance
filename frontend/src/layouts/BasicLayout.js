import { Container } from "react-bootstrap";
import '../App.css';

export default function BasicLayout({ children }) {


  return (
    <div className="App">
      <header className="App-header">
      <Container expand="xl" className="pt-4 flex-grow-1">
        {children}
      </Container>
      </header>
    </div>
  );
}