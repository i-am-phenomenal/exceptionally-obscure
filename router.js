
import React from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import App from './App';
function Index() {
  return <h2> Home </h2>;
}

function AnotherDummyPageView() {
  
  return (
    <div>
      <input type = "text" value = {this.state.userName} onChange = {this.handleUserNameChange} />
    </div>
  )
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
           <li>
           <Link to ="/anotherDummyPage"> Another Dummy Page </Link>
           </li>
           </ul>
           </nav>
        <Route path="/dummyPage" exact component={Index} />
        <Route path="/anotherDummyPage" exact component={AnotherDummyPageView} />
      </div>
    </Router>
  );
}

export default AppRouter
