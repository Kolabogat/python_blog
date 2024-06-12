import BlogList from './BlogList';
import Sidebar from './Sidebar';
import useFetch from './useFetch';
import { useParams } from "react-router-dom";


const BlogFilter = () => {
  const { slug } = useParams();
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog/filter=' + slug + '/')
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title={ `${ slug } blogs` } url={ `/filter_by/${ slug }` } /> }
        { error }
        { cat_error }
        { categories && <Sidebar categories={ categories } title='Categories' /> }
      </div>
    </div>
  );
}

export default BlogFilter;