import Create from '../Create';
import useFetch from '../useFetch';

const CreateRouter = () => {
  const { data: categories } = useFetch('http://localhost:8000/api/blog/categories/')
  const { data: difficulties } = useFetch('http://localhost:8000/api/blog/difficulties/')

  return (
    <div className="Home">
      <div className='container'>
        { categories && difficulties && <Create categories={ categories } difficulties={ difficulties } /> }
      </div>
    </div>
  );
}

export default CreateRouter;