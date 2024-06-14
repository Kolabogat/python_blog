import { useState } from "react";
import { useNavigate } from 'react-router-dom';

const Create = ({ categories, difficulties }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [image, setImage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    console.log(e.target.files[0]);
  } 

  const handleSubmit = (e) => {
    e.preventDefault();
    const blog = { title, content, category, difficulty };

    fetch('http://localhost:8000/api/blog/create/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(blog)
    }).then(() => {
      navigate('/')
    })

  }

  return (
    <div className="create">
        <h2>Add a New Blog</h2>
        <form onSubmit={ handleSubmit }>
          <input
            type='text'
            placeholder='Blog title...'
            required
            value={ title }
            onChange={ (e) => setTitle(e.target.value) }
          />

          <textarea
          required
          placeholder='Blog content...'
          value={ content }
          onChange={ (e) => setContent(e.target.value) }
          ></textarea>
          <select
            value={ category }
            onChange={ (e) => setCategory(e.target.value) }
          >
            <option value="" selected disabled hidden>Choose category...</option>
            { categories.map(( category ) => (
              <option value={ category.id }>{ category.category }</option>
            ))}
          </select>

          <select
            value={ difficulty }
            onChange={ (e) => setDifficulty(e.target.value) }
          >
            <option value="" selected disabled hidden>Choose difficulty...</option>
            { difficulties.map(( difficulty ) => (
              <option value={ difficulty.id }>{ difficulty.difficulty }</option>
            ))}

          </select>

          <button className='button-blue'>Add New Blog</button>
        </form>
    </div>
  );
}

export default Create;