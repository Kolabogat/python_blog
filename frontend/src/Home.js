import BlogList from './BlogList';
import Sidebar from './Sidebar';
import useFetch from './useFetch';

const Home = () => {
  const { data: blogs, error } = useFetch('http://localhost:8000/blogs')
  const { data: categories, cat_error } = useFetch('http://localhost:8000/categories')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={blogs} title='All Blogs' /> }
        { categories && <Sidebar categories={categories} title='Categories' /> }
      </div>
    </div>
  );
}

export default Home;