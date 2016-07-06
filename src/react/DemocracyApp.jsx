import React from 'react'
import { render } from 'react-dom'
import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers
} from 'redux'
import { Provider } from 'react-redux'
import thunk from 'redux-thunk'

import * as reducers from './reducers'
import DemocracyAppContainer from './containers/DemocracyAppContainer'

let finalCreateStore = compose(
  applyMiddleware(thunk)
  // window.devToolsExtension ? window.devToolsExtension() : f => f
)(createStore)
let reducer = combineReducers(reducers)
let store = finalCreateStore(reducer)

export default class DemocracyApp extends React.Component {
  render () {
    return (
      <Provider store={store}>
        <DemocracyAppContainer />
      </Provider>
    )
  }
}

if (typeof window !== 'undefined') {
  render(<DemocracyApp/>, document.getElementById('DemocracyApp'))
}
