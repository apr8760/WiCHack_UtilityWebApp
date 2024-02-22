// Ready.js
import React from 'react';
import { useHistory } from 'react-router-dom';

const Ready = ({ category }) => {
  const history = useHistory();

  const handleYesClick = () => {
    // Redirect to the set table page
    history.push(`/set-table/${category}/0?method=random`);
  };

  const handleNoClick = () => {
    // Redirect to the ready question page again
    history.push(`/ready-question-${category}`);
  };

  return (
    <div>
      <h1>Are you ready for a table?</h1>
      <button onClick={handleYesClick}>Yes</button>
      <button onClick={handleNoClick}>No</button>
    </div>
  );
};

export default Ready;
