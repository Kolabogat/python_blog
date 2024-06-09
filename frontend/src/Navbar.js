import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <h1>Python Blog</h1>
      <div className="links">
        <Link to="/create" className='button-blue'>Create</Link>
      </div>
    </nav>
  );
}

export default Navbar;