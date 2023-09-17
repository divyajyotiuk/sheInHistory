
import React, { useState } from 'react';
import './Accordion.css'; 
function Accordion({ data }) {
  const [expanded, setExpanded] = useState(false);

  const toggleAccordion = () => {
    setExpanded(!expanded);
  };

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
