import { Container } from "react-bootstrap";
import AppNavbar from "../nav/AppNavbar.js";
import '../App.css';

export default function BasicLayout({ children }) {


  return (
    <div className="App">
      <header className="App-header" style={{ height: '5%', position: 'fixed', width: '100%', zIndex: 1000 }}>
      <AppNavbar />
    </header>
      <Container expand="xl" className="pt-4 flex-grow-1">
        {children}
      </Container>
    </div>
  );
}