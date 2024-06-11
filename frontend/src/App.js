import './App.css';
import { BrowserRouter as Router , Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import BlogDetail from './BlogDetail';
import Create from './Create';
import BlogFilter from './BlogFilter';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
          <Routes>
            <Route exact path='/' element={ <Home /> } />
            <Route exact path='/filter_by/:slug' element={ <BlogFilter /> } />
            <Route exact path='/blog/:id' element={ <BlogDetail /> } />
            <Route exact path='/add_blog' element={ <Create /> } />
          </Routes>
      </div>
    </Router>
  );
}

export default App;
