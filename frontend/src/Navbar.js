import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <Link to="/"><h1>Python Blog</h1></Link>
      <div className="links">
        <Link to="/add_blog" className='button-blue'>Add Blog</Link>
      </div>
    </nav>
  );
}

export default Navbar;