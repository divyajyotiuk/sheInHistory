import React from 'react';
import './Person.css'; 
function Person({ persons }) {
  persons= [
    {
      "name": "Marjory Stoneman Douglas",
      "wikipedia_link": "https://en.wikipedia.org/wiki/Marjory_Stoneman_Douglas"
    },
    {
      "name": "Suzie Zuzek",
      "wikipedia_link": "https://en.wikipedia.org/wiki/Suzie_Zuzek"
    }
  ]


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
