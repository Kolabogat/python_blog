import { useParams } from "react-router-dom";
import useFetch from "./useFetch";
import { useNavigate } from "react-router-dom";

const BlogDetail = () => {
  const { id } = useParams();
  const { data: blog, error } = useFetch('http://localhost:8000/api/blog/1/');
  const navigate = useNavigate();

  return (
    <div className='blog-details'>
      {console.log('Data: ' + error)}
      { error && <div>Error: { error }</div>}
      { blog && (
        <div>
          <h1>{ blog.title }</h1>
          <span className='span-category'>{ blog.category.category }</span> · <span className='difficulty-easy'>{ blog.difficulty.difficulty }</span><span> · Written by { blog.user } · { blog.words_number } Words</span>
          <p>{ blog.content }</p>
        </div>
      )}
    </div>
  );
}

export default BlogDetail;