import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Form from "./Components/Form";
import axios from "./axios";
import Cookies from 'js-cookie'

class App extends Component {
  state = {
    value: "Obesity",
    disorders: null
  };
  handleSubmit(event) {
    event.preventDefault();
    axios.post('server/api/v1/search', {data : this.state.value})
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
          return <ul>{this.state.disorders[disorderkey].disorders__name}</ul>
        })
        if (!view.length){
          view = <h3>No results</h3>
        }
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
