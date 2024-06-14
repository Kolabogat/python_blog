import { useParams } from "react-router-dom";
import useFetch from "./useFetch";
import Sidebar from "./inc/Sidebar";
import { useNavigate } from "react-router-dom";

const BlogDetail = () => {
  const { id } = useParams();
  const { data: blog, blog_error } = useFetch('http://localhost:8000/api/blog/' + id + '/');
  const { data: categories, categories_error } = useFetch('http://localhost:8000/api/blog/categories/')
  const navigate = useNavigate();

  return (
    <div className='container'>
      <div className='content'>
        <div className='blog-details'>
          { blog_error && (
            <div>
              Blog error: { blog_error }
            </div>
          )}
          { categories_error && (
            <div>
              Categories error: { categories_error }
            </div>
          )}
          { blog && (
            <div>
              <h1>{ blog.title }</h1>
              <span className='span-category'>{ blog.category.category }</span> · <span className={ blog.difficulty.class_name }>{ blog.difficulty.difficulty }</span><span> · Written by { blog.user }</span>
              <p>{ blog.content }</p>
              <p className='datetime'>Posted { blog.created_at }</p>
            </div>
          )}
        </div>
      </div>
      { categories && <Sidebar categories={ categories } title='Categories' /> }
    </div>
  );
}

export default BlogDetail;