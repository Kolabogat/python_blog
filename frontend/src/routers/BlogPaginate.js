import BlogList from '../BlogList';
import Sidebar from '../inc/Sidebar';
import useFetch from '../useFetch';
import Paginate from '../Paginate';
import { useParams } from "react-router-dom";


const BlogPaginate = () => {
  const { page } = useParams();
  const { data: blogs, error } = useFetch('http://localhost:8000/api/blog/?page=' + page)
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/blog/categories/')

  return (
    <div className="Home">
      <div className='container'>
        { blogs && <BlogList blogs={ blogs } title='All blogs' url='' /> }
        { categories && <Sidebar categories={ categories } title='Categories' /> }
      </div>
    </div>
  );
}

export default BlogPaginate;