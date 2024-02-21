// GotoTable.js
import React from 'react';

const GotoTable = ({ category, tableNumber }) => {
  return (
    <div>
      <h1>Your table number is: {tableNumber}</h1>
      <p>You have 120 seconds to get to the table.</p>
      {/* Implement timer logic here */}
      <button>Here!</button>
    </div>
  );
};

export default GotoTable;
