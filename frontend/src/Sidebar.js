import { Link } from "react-router-dom";
import useFetch from './useFetch';

const Sidebar = ({ categories, title }) => {

  return (
    <div className='sidebar'>
      <h2>{ title }</h2>
      <div className='categories '>
        <Link to='/'>
          <div className='category'>
            <p>All</p>
          </div>
        </Link>

        {categories.map((category) => (
          <Link to={ `/filter_by/${ category.slug }` } className="text-decoration: none;">
            <div className='category' key={category.id}>
              <p>{category.category}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>

  );
}

export default Sidebar;