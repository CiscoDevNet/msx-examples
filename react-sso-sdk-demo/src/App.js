//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { Home } from "./Home";
import { Profile } from "./Profile";
import { Callback } from "./Callback";
import { Tenants } from "./Tenants";

import './App.css';

/**
 * simply setting up the routing
 * @returns {JSX.Element}
 * @constructor
 */
function App() {
  return (
    <Router basename="/reactSsoSdkDemo">
      <nav className="navbar navbar-expand navbar-dark bg-primary">
        <a className="navbar-brand" href="/">Msx SSO using React & AppAuth JS</a>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/profile">Profile</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/tenants">Tenants</Link>
            </li>
          </ul>
        </div>
      </nav>

      {/* setup routes*/}
      <div>
        <Route exact path={"/"} component={Home} />
        <Route exact path={"/profile"} component={Profile} />
        <Route exact path={"/callback"} component={Callback} />
        <Route exact path={"/tenants"} component={Tenants} />
      </div>
    </Router>
  );
}

export default App;
