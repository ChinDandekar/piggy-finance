import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import ConstructionPage from "./pages/ConstructionPage";
import PostButtonPage from "./pages/PostButtonPage";

import "bootstrap/dist/css/bootstrap.css";

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<ConstructionPage/>} />
        <Route exact path="/postbutton" element={<PostButtonPage />} />
        <Route exact path="/home" element = {<HomePage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
