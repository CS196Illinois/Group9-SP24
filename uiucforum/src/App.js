import logo from './logo.svg';
import './App.css';

function App() {
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
</div>
</body>
  );
}

export default App;
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UIUC Class Forum</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="classes.html">Classes</a></li>
                <li><a href="subjects.html">Subjects</a></li>
                <li><a href="search.html">Search</a></li>
                <li><a href="contact.html">Contact Us</a></li>
            </ul>
        </nav>
        <img src="logo.png" alt="UIUC Forum Logo" id="logo">
    </header>
    <main>
        <section id="trending-posts">
            <h2>Trending Posts</h2>
            <!-- Dynamic posts go here -->
        </section>
    </main>
    <footer>
        <!-- Footer content -->
    </footer>
</body>
</html>
*/
