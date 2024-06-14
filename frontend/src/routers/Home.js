import BlogList from '../BlogList';
import Sidebar from '../inc/Sidebar';
import useFetch from '../useFetch';

const Home = () => {
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog/')
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/blog/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title='All Blogs' url='' /> }
        { categories && <Sidebar categories={ categories } title='Categories' /> }
      </div>
    </div>
  );
}

export default Home;