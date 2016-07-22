import React from "react"
import Radium from "radium"

import { connect } from "react-redux"

import * as counterActions from "../actions/counterActions"
import Headline from "../components/Headline"
// import CustomModal from "../components/Modal"

const styles = {
  button: {
    cursor: "pointer",
    padding: "8px 10px",
    background: "blue",
    float: "left",
    "margin-bottom": "10px",
  },
  counter: {
    clear: "both",
    color: "blue",
    fontSize: "20px",
  }
}

@connect(state => ({
  counters: state.counters,
}))
@Radium
export default class DemocracyAppContainer extends React.Component {
  handleIncreaseClick() {
    let {dispatch} = this.props;
    dispatch(counterActions.increaseCounter())
  }

  handleDecreaseClick() {
    let {dispatch} = this.props;
    dispatch(counterActions.decreaseCounter())
  }

  render() {
    let {counters} = this.props
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Democracy App!</Headline>
            <div>
              {/* <CustomModal /> */}
              {/* <a className="ui compact floating watch dropdown button">Dupa</a> */}
              <div style={[styles.button]} onClick={() => this.handleIncreaseClick()}>INCREASE</div>
              <div style={[styles.button]} onClick={() => this.handleDecreaseClick()}>DECREASE</div>
            </div>
            <p style={[styles.counter]}>{counters.clicks}</p>
            <p>{process.env.BASE_API_URL}</p>
          </div>
        </div>
      </div>
    )
  }
}
