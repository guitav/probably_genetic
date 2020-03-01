import React from "react";
class Form extends React.Component {
  state = {
      value: 'Obesity'
    }

  render() {
  return (
    <form onSubmit={this.props.handleSubmit}>
      <label>
        Enter Symptoms:
        <textarea value={this.props.value}
        onChange={this.props.handleChange.bind(this)} />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
  }
}
export default Form;
