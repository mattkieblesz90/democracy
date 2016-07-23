import React from "react"

import { MenuItem, Icon } from "semantic-react/radium";


export default class MyMenuItem extends React.Component {
    render() {
    const {active, children, ...other} = this.props;
    return (/* Do not forget to pass other properties */
        <MenuItem {...other}>
            {active && <Icon name="checkmark"/>}
            {children}
        </MenuItem>);
    }
}