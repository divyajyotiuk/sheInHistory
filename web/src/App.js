import React, { Component } from 'react';
import USAMap from "react-usa-map";
import axios from "axios";
 
class App extends Component {
  /* mandatory */
  mapHandler = (event) => {
    const stateName = event.target.getElementsByTagName('title')[0].innerHTML
    axios({
      url: "https://she-in-history.onrender.com/api/location",
      method: "post",
      mode: 'no-cors',
      headers: {
        'Content-Type':'application/json',
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true',
        'X-Requested-With': 'XMLHttpRequest',
        "Access-Control-Allow-Headers": "content-type"
      },

      // Attaching the form data
      data: {
        state: stateName
      },
  })

      // Handle the response from backend here
      .then((res) => {
        alert(res);
       })

      // Catch errors if any
      .catch((err) => { });
  };
 
  render() {
    return (
      <div className="App">
        <USAMap onClick={this.mapHandler} />
      </div>
    );
  }
}
 
export default App;