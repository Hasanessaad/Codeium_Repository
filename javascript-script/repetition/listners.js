const createButtonListeners = (buttons, callback) => {
    buttons.forEach(button => button.addEventListener('click', callback));
}
