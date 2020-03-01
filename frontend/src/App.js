import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Form from "./Components/Form";
import axios from "./axios";
import Cookies from 'js-cookie'

class App extends Component {
  state = {
    value: "Obesity",
    entered_text: "",
    disorders: null
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
    .then(response => response)
    .then(data => {
      this.setState({
        disorders: data.data
      })
    })
    .catch(error => console.log(error));
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  render() {
    let view  = null
    if  (this.state.disorders){
        view = Object.keys(this.state.disorders).map(disorderkey => {
          return [...this.state.disorders[disorderkey].disorders__name]
        })
      }
    return (
      <div className="App">
        <Form
          value={this.state.value}
          handleSubmit={this.handleSubmit.bind(this)}
          handleChange={this.handleChange.bind(this)}
        />
        {view}
      </div>
    );
  }
}

export default App;
