import { Link } from "react-router-dom";
import Sidebar from './Sidebar';
import useFetch from './useFetch';


const BlogList = ({ blogs, title }) => {

  const handleIfEmpty = (e) => {
    if (e.count === 0) {
      return (
        <div className='blog-preview'>
          <Link to='/add_blog'>
            <h2 className='cut-text'>+ Add New Blog</h2>
          </Link>
        </div>
      )
    }
  }

  return (
    <div className='content'>
      <h2 className='capitalize'>{ title }</h2>

      { blogs.results.map((blog) => (
        <div className='blog-preview' key={ blog.id }>
          <Link to={ `/blog/${ blog.id }` }>
          <h2 className='cut-text'>{ blog.title }</h2>
          <div className='blog-info'>
            <span className='span-category'>{ blog.category.category }</span> · <span className={ blog.difficulty.class_name }>{ blog.difficulty.difficulty }</span><span> · Written by { blog.user } · { blog.words_number } Words</span>
            <span className='cut-text'>{ blog.content }</span>
          </div>
          </Link>
        </div>
      ))}
      <p>{ handleIfEmpty(blogs) }</p>
    </div>
  );
}

export default BlogList;