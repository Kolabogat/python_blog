import BlogList from './BlogList';
import Sidebar from './Sidebar';
import useFetch from './useFetch';

const Home = () => {
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog_list/')
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title='All Blogs' /> }
        { error }
        { cat_error }
        { categories && <Sidebar categories={ categories.results } title='Categories' /> }
      </div>
    </div>
  );
}

export default Home;