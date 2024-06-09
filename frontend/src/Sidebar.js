import useFetch from './useFetch';

const Sidebar = ({categories, title}) => {

  return (
    <div className='sidebar'>
      <h2>{ title }</h2>
      <div className='categories'>
      {categories.map((category) => (
        <div className='category' key={category.id}>
            <p>{category.category}</p>
        </div>
      ))}

      </div>
    </div>

  );
}

export default Sidebar;