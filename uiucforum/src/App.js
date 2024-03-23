import './App.css';
import React from 'react';

const UniqueCombinationsPage = ({ uniqueCombinations }) => {
  return (
    <div>
      <h1>All Classes</h1>
      <ul>
        {uniqueCombinations.map((combination, index) => (
          <li key={index}>
            <a href={`#${index}`}>{`${combination[0]} ${combination[1]}`}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

const CombinationDetailsPage = ({ combination }) => {
  return (
    <div>
      <h1>Combination Details</h1>
      <p>Subject: {combination[0]}</p>
      <p>Number: {combination[1]}</p>
      {/* Additional details can be added here */}
    </div>
  );
};

const App = () => {
  const uniqueCombinations = [
    ['AAS', '100'],
    ['AAS', '202'],
    ['BIO', '101'],
    // Add more unique combinations as needed
  ];

  return (
    <div>
      <UniqueCombinationsPage uniqueCombinations={uniqueCombinations} />
      {/* Render separate pages for each combination */}
      {uniqueCombinations.map((combination, index) => (
        <CombinationDetailsPage key={index} combination={combination} />
      ))}
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
           <code>src/App.js</code>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
