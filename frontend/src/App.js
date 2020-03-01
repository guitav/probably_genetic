import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Form from "./Components/Form";
import axios from "./axios";
import Cookies from 'js-cookie'

class App extends Component {
  state = {
    value: "",
    entered_text: ""
  };
  handleSubmit(event) {
    event.preventDefault();
    var csrftoken = Cookies.get('csrftoken');
    let query = encodeURIComponent("?name")+"="+encodeURIComponent(this.state.value)
    axios.post('/api/v1/forms', {data : this.state.value},
    {headers: {
      common: {
        'X-CSRF-Token': csrftoken
      }
    }})
    .then(response => {
      console.log("HERE")
    })
    .catch(error => console.log(error));
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  render() {
    return (
      <div className="App">
        <Form
          handleSubmit={this.handleSubmit}
          handleChange={this.handleChange}
        />
      </div>
    );
  }
}

export default App;
