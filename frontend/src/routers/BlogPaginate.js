import BlogList from '../BlogList';
import Sidebar from '../inc/Sidebar';
import useFetch from '../useFetch';
import Paginate from '../Paginate';
import { useParams } from "react-router-dom";


const BlogPaginate = () => {
  const { page } = useParams();
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog_list/?page=' + page)
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title='All blogs' url='' /> }
        { error }
        { cat_error }
        { categories && <Sidebar categories={ categories } title='Categories' /> }
      </div>
    </div>
  );
}

export default BlogPaginate;