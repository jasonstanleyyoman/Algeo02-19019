import React, { useState } from 'react';
import {
  BrowserRouter as Router, 
  Switch, 
  Route
} from 'react-router-dom';

import Home from './pages/Home';
import Searched from './pages/Searched';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route path="/searched/:query" component={Searched} />
        {/* /searched/<query> */}
      </Switch>
    </Router>
  ) 
}

export default App;

