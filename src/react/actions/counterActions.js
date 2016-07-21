export const INCREASE = "INCREASE"
export const DECREASE = "DECREASE"

export function increaseCounter() {
    return {type: INCREASE}
}

export function decreaseCounter() {
    return {type: DECREASE}
}
