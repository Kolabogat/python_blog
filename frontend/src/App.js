import './App.css';
import { BrowserRouter as Router , Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import BlogDetail from './BlogDetail';
import BlogFilter from './BlogFilter';
import Footer from './Footer';
import BlogList from './BlogList';
import BlogPaginate from './BlogPaginate';
import CreateRouter from './routers/CreateRouter';
import BlogFilterPaginate from './BlogFilterPaginate';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
          <Routes>
            <Route exact path='/' element={ <Home /> } />
            <Route exact path='/page/:page' element={ <BlogPaginate /> } />
            <Route exact path='/filter_by/:slug' element={ <BlogFilter /> } />
            <Route exact path='/filter_by/:slug/page/:page' element={ <BlogFilterPaginate /> } />
            <Route exact path='/blog/:id' element={ <BlogDetail /> } />
            <Route exact path='/add_blog' element={ <CreateRouter /> } />
          </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
