// Home.js
import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';

const Home = () => {
  const [selectedCompany, setSelectedCompany] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [companies, setCompanies] = useState([]); // Fetch or set your company list here
  const history = useHistory();

  const handleCompanyChange = (event) => {
    setSelectedCompany(event.target.value);
  };

  const handleCategoryChange = (event) => {
    setSelectedCategory(event.target.value);
  };

  const handleSubmit = () => {
    if (selectedCompany && selectedCategory) {
      history.push(`/ready-question-${selectedCategory}`);
    }
  };

  useEffect(() => {
    // Fetch categories based on the selected company and update the state
    // You may need to implement an API call to fetch categories based on the selected company
    // Update the 'categories' state accordingly
    // const categories = fetchCategories(selectedCompany);
    // setCategories(categories);
  }, [selectedCompany]);

  return (
    <div>
      <label>Select Company:</label>
      <select onChange={handleCompanyChange} value={selectedCompany}>
        {companies.map((company) => (
          <option key={company} value={company}>
            {company}
          </option>
        ))}
      </select>

      {selectedCompany && (
        <div>
          <label>Select Category:</label>
          <select onChange={handleCategoryChange} value={selectedCategory}>
            {/* Map and render categories based on the selected company */}
          </select>
        </div>
      )}

      <button onClick={handleSubmit}>Next</button>
    </div>
  );
};

export default Home;
