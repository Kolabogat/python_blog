import './App.css';
import { BrowserRouter as Router , Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Sidebar from './Sidebar';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
          <Routes>
            <Route exact path='/' element={ <Home /> } />
          </Routes>
      </div>
    </Router>
  );
}

export default App;
