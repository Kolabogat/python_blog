import './App.css';
import { BrowserRouter as Router , Route, Routes } from 'react-router-dom';
import Navbar from './inc/Navbar';
import Home from './routers/Home';
import BlogDetail from './BlogDetail';
import BlogFilter from './routers/BlogFilter';
import Footer from './inc/Footer';
import BlogPaginate from './routers/BlogPaginate';
import CreateRouter from './routers/CreateRouter';
import BlogFilterPaginate from './routers/BlogFilterPaginate';

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
