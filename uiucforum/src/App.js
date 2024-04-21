import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [showCreatePost, setShowCreatePost] = useState(false);
  const [username, setUsername] = useState('');
  const [classOptions, setClassOptions] = useState([]);
  const [numberOptions, setNumberOptions] = useState([]);
  const [dropdownValue1, setDropdownValue1] = useState('');
  const [dropdownValue2, setDropdownValue2] = useState('');
  const [title, setTitle] = useState('');
  const [postContent, setPostContent] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5000/data')
        .then(response => {
            setClassOptions(response.data.unique_classes);
            setNumberOptions(response.data.unique_numbers);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}, []);


  const toggleCreatePost = () => {
    setShowCreatePost(!showCreatePost);
  };

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleDropdownChange1 = (event) => {
    setDropdownValue1(event.target.value);
  };

  const handleDropdownChange2 = (event) => {
    setDropdownValue2(event.target.value);
  };

  const handlePostContentChange = (event) => {
    setPostContent(event.target.value);
  };

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  }

  const handleSubmit = () => {
    
    const postData = {
      username: username,
      class1: dropdownValue1,
      number: dropdownValue2,
      title: title,
      body: postContent
    };
  
    // Send a POST request to the backend
    fetch('http://localhost:5000/api/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postData)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to submit post');
      }
      return response.json();
    })
    .then(data => {
      console.log(data.message); // Log success message
      // Add further logic if needed
    })
    .catch(error => {
      console.error('Error submitting post:', error);
      // Handle error
    });
    

    console.log('Username:', username);
    console.log('Dropdown 1:', dropdownValue1);
    console.log('Dropdown 2:', dropdownValue2);
    console.log('Title', title)
    console.log('Post Content:', postContent);

    toggleCreatePost();

    // Add further logic to submit the data to a backend or perform other actions
  };

  return (
    
<body>
<header>
  <nav>
    <div class="search-bar"><input type="search" placeholder="Search..." aria-label="Search"/></div>
    <ul>
      <li><a href="home.js">Home</a></li>
      <li><a href="classes.js">Classes</a></li>
      <li><a href="subjects.js">Subjects</a></li>
      <li><a href="contact.js">Contact Us</a></li>
    </ul>
  </nav>
</header>
<div class="main">
  <h1>Trending Posts</h1>

  <h2>Top Comments</h2>
  <div class="top-comments">
    <div class="comment-box">
      <p>This is a top comment.</p>
      <p>Posted by: John Doe</p>
    </div>
    <div class="comment-box">
      <p>This is another top comment.</p>
      <p>Posted by: Jane Smith</p>
    </div>
  </div>

  <button className='square-button' onClick={toggleCreatePost}>+</button>
  
  {showCreatePost && (
        <div className="create-post">
          <h3>Create Post</h3>
          <div className="create-post-form">
            <input type="text" placeholder="User name" className="username-input" onChange={handleUsernameChange} />
            <select className="dropdown-menu" onChange={handleDropdownChange1}>
            <option value="">Select Class</option>
            {classOptions.map((class1, index) => (
              <option key={index} value={class1}>{class1}</option>
            ))}
            </select>
            <select className="dropdown-menu" onChange={handleDropdownChange2}>
            <option value="">Select Number</option>
            {numberOptions.map((number, index) => (
              <option key={index} value={number}>{number}</option>
            ))}
            </select>
            <input type="text" placeholder="Title" className="title-input" onChange={handleTitleChange} />
            <textarea placeholder="Post" className="post-textarea" onChange={handlePostContentChange} />
            <button className='submit-button' onClick={handleSubmit}>Submit</button>
          </div>
        </div>
      )}
</div>
</body>
  );
}

export default App;

