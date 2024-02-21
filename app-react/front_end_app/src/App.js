// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import Ready from './Ready';
import GotoTable from './GotoTable';
import Timer from './Timer';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/ready-question-:category" exact component={Ready} />
        <Route path="/set-table/:category/:tableNumber" exact component={GotoTable} />
        <Route path="/timer/:category/:tableNumber" exact component={Timer} />
      </Switch>
    </Router>
  );
};

export default App;
