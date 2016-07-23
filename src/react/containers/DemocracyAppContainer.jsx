import React from "react"
import Radium from "radium"

import { connect } from "react-redux"
import { Button, Menu, Value, Statistic, Label } from "semantic-react/radium";

import * as counterActions from "../actions/counterActions"
import Headline from "../components/Headline"
import MyMenuItem from "../components/TopHeader.jsx"


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
        <Menu menuValue={['test1','test3']}>
            <MyMenuItem menuValue="test1">Item 1</MyMenuItem>
            <MyMenuItem menuValue="test2">Item 2</MyMenuItem>
            <MyMenuItem menuValue="test3">Item 3</MyMenuItem>
        </Menu>
        <div className="row">
          <div className="col-sm-12">
            <Headline>Democracy App!</Headline>
            <div>
              {/* <a className="ui compact floating watch dropdown button">Dupa</a> */}
              <Button onClick={() => this.handleIncreaseClick()}>INCREASE</Button>
              <Button onClick={() => this.handleDecreaseClick()}>DECREASE</Button>
            </div>
            <Statistic>
              <Value>{counters.clicks}</Value>
              <Label>Clicks</Label>
            </Statistic>
            <p>{process.env.BASE_API_URL}</p>
          </div>
        </div>
      </div>
    )
  }
}
