import { Container, Nav, Navbar} from "react-bootstrap";
import { LogoutButton } from "../components/logoutbuton";

export default function AppNavbar() {
  return (
    <>
      <Navbar>
        <Container>
            <Nav className="justify-content-end" style={{ width: "100%" }}>
              <LogoutButton/>
            </Nav>
        </Container>
      </Navbar >
    </>
  );
}