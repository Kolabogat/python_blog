import { Link } from "react-router-dom";
import Sidebar from './Sidebar';
import useFetch from './useFetch';


const BlogList = ({ blogs, title }) => {

  return (
    <div className='content'>
      <h2>{ title }</h2>
      {blogs.map((blog) => (
        <div className='blog-preview' key={blog.id}>
          <Link to={ `/blogs/${blog.id}` }>
          <h2>{ blog.title }</h2>
          <div className='blog-info'>
            <span className='difficulty-easy'>{ blog.difficulty }</span><span> · Written by { blog.user } · { blog.words_number } Words</span>
            <span className='cut-text'>{ blog.content }</span>
          </div>
          </Link>
        </div>
      ))}
    </div>
  );
}

export default BlogList;