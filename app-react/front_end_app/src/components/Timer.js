// Timer.js
import React from 'react';
import { useHistory } from 'react-router-dom';

const Timer = ({ category, tableNumber }) => {
  const history = useHistory();

  const handleDoneClick = () => {
    // Redirect to the ask ready question again
    history.push(`/ready-question-${category}-${tableNumber}`);
  };

  const handleChangeTableClick = (method) => {
    // Redirect to the set table page with the specified method
    history.push(`/set-table/${category}/${tableNumber}?method=${method}`);
  };

  return (
    <div>
      <h1>Timer Page</h1>
      <p>You have 60 seconds.</p>
      {/* Implement timer logic here */}
      <button>Pause</button>
      <button>Play</button>
      <button>Restart</button>

      <div>
        <h2>Change Table</h2>
        <button onClick={() => handleChangeTableClick('random')}>Random</button>
        <button onClick={() => handleChangeTableClick('nearby')}>Nearby</button>
      </div>

      <button onClick={handleDoneClick}>Done</button>
    </div>
  );
};

export default Timer;
