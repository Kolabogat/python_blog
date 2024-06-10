import { useState } from "react";
import { useNavigate } from 'react-router-dom';

const Create = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [category, setCategory] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const blog = { title, content, category, difficulty };

    fetch('http://localhost:8000/api/blog_create/', {
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
            onChange={(e) => setTitle(e.target.value)}
          />
          <textarea
          required
          placeholder='Blog content...'
          value={ content }
          onChange={(e) => setContent(e.target.value)}
          ></textarea>
          <select
            value={ category }
            onChange={(e) => setCategory(e.target.value)}
          >
            <option value="" selected disabled hidden>Choose category...</option>
            <option value='1'>Python</option>
            <option value='2'>Databases</option>
          </select>

          <select
            value={ difficulty }
            onChange={(e) => setDifficulty(e.target.value)}
          >
            <option value="" selected disabled hidden>Choose difficulty...</option>
            <option value='1'>Easy</option>
            <option value='2'>Hard</option>
          </select>

          <button className='button-blue'>Add New Blog</button>

        </form>
    </div>
  );
}

export default Create;