import React from "react"
import { Button, Icon, Header, Content, Description, Actions, LabeledButton, Modal } from "semantic-react/radium";
import { spring } from '../utils/animationUtils';

export default class CustomModal extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            active: false
        }
    }

    onCloseModal = () => {
        this.setState({
            active: false
        });
    }

    onAnimationStyle = (interpolatedStyle, dimensions, active) => {
        return {
            transform: `translateY(${interpolatedStyle.y}px)`
        };
    }

    render() {
        return (
            <div>
                <Button onClick={() => this.setState({ active: true })}>Open modal</Button>
                <Modal onRequestClose={this.onCloseModal}
                       active={this.state.active}
                >
                    <Icon name="close" onClick={this.onCloseModal.bind(this)}/>
                    <Header>Select a photo</Header>
                    <Content image>
                        <Description>
                            <Header>Default profile image</Header>
                            <p>
                                We've found the following gravatar image associated with your e-mail address.
                            </p>
                            <p>
                                Is it okay to use this photo?
                            </p>
                        </Description>
                    </Content>
                    <Actions>
                        <Button emphasis="negative" onClick={this.onCloseModal.bind(this)}>Nope</Button>
                        <LabeledButton emphasis="positive"
                                       label="checkmark"
                                       labelType="icon"
                                       onClick={this.onCloseModal.bind(this)}
                        >
                            Yep, that's me
                        </LabeledButton>
                    </Actions>
                </Modal>
            </div>
        );
    }
}