
import React from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';

function Index() {
  return <h2> Home </h2>;
}

function AppRouter() {
  return (
    <Router>
      <div>
        <nav>
         <ul>
           <li>
           <Link to="/dummyPage"> Dummy Page </Link>
           </li>
           </ul>
           </nav>
        <Route path="/dummyPage" exact component={Index} />
      </div>
    </Router>
  );
}

export default AppRouter
