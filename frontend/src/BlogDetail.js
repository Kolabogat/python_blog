import { useParams } from "react-router-dom";
import useFetch from "./useFetch";
import Sidebar from "./Sidebar";
import { useNavigate } from "react-router-dom";

const BlogDetail = () => {
  const { id } = useParams();
  const { data: blog, error } = useFetch('http://localhost:8000/api/blog/' + id + '/');
  const navigate = useNavigate();
  const { data: categories, cat_error } = useFetch('http://localhost:8000/api/categories/')

  return (
    <div className='container'>
      <div className='content'>
        <div className='blog-details'>
          { error && <div>Error: { error }</div>}
          { blog && (
            <div>
              { blog.image && <img className='image-field' src={ blog.image } alt="Paris" /> }

              <h1>{ blog.title }</h1>
              <span className='span-category'>{ blog.category.category }</span> · <span className={ blog.difficulty.class_name }>{ blog.difficulty.difficulty }</span><span> · Written by { blog.user }</span>
              <p>{ blog.content }</p>
              <p className='datetime'>Posted { blog.created_at }</p>
            </div>
          )}
        </div>
      </div>
      { categories && <Sidebar categories={ categories.results } title='Categories' /> }
    </div>
  );
}

export default BlogDetail;