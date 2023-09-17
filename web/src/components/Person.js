import React from 'react';
import './Person.css'; 
function Person({ persons }) {
  return (
    <div className="person-cards">
      {persons.map((person, index) => (
        <div className="person-card" key={index}>
          <h3>{person.name}</h3>
          <a href={person.wikipedia_link} target="_blank" rel="noopener noreferrer">
            Wikipedia Link
          </a>
        </div>
      ))}
    </div>
  );
}

export default Person;
