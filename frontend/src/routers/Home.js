import BlogList from '../BlogList';
import Sidebar from '../inc/Sidebar';
import useFetch from '../useFetch';

const Home = () => {
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog_list/')
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title='All Blogs' url='' /> }
        { error }
        { cat_error }
        { categories && <Sidebar categories={ categories } title='Categories' /> }
      </div>
    </div>
  );
}

export default Home;