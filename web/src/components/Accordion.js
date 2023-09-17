
import React, { useState } from 'react';
import './Accordion.css'; 
function Accordion({ data }) {
  const [expanded, setExpanded] = useState(false);

  const toggleAccordion = () => {
    setExpanded(!expanded);
  };
  data={"dates": [
    {
      "year": "2020",
      "title": "Suzie Zuzek for Lilly Pulitzer: the Artist Behind an Iconic American Fashion Brand, 1962-1985"
    },
    {
      "year": "1987",
      "title": "Marjory Stoneman Douglas: Voice of the River"
    }
  ],
  "events": [
    {
      "head": "Florida Commission on the Status of Women",
      "desc": "Florida Women’s Hall of Fame"
    },
    {
      "head": "Florida Division of Historical Resources",
      "desc": "Florida Women’s Heritage Trail (PDF)"
    }
  ],
  "persons": [
    {
      "name": "Marjory Stoneman Douglas",
      "wikipedia_link": "https://en.wikipedia.org/wiki/Marjory_Stoneman_Douglas"
    },
    {
      "name": "Suzie Zuzek",
      "wikipedia_link": "https://en.wikipedia.org/wiki/Suzie_Zuzek"
    }
  ]
}

  return (
    <div className={`accordion ${expanded ? 'expanded' : ''}`}>
      <div className="accordion-header" onClick={toggleAccordion}>
        <h3>{data.state}</h3>
      </div>
      <div className="accordion-content">
        <p>Important Dates:</p>
        <ul>
          {data.dates.map((date, index) => (
            <li key={index}>
              Year: {date.year}, Title: {date.title}
            </li>
          ))}
        </ul>

      </div>
    </div>
  );
}

export default Accordion;
