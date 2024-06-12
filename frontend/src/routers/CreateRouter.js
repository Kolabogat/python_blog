import Create from '../Create';
import useFetch from '../useFetch';

const CreateRouter = () => {
  const { data: categories } = useFetch('http://localhost:8000/api/categories/')
  const { data: difficulties } = useFetch('http://localhost:8000/api/difficulties/')

  return (
    <div className="Home">
      <div className='container'>
        { categories && <Create categories={ categories } difficulties={ difficulties } /> }
      </div>
    </div>
  );
}

export default CreateRouter;