const applyStyles = (selectors, styles) => {
    selectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        elements.forEach(element => {
            Object.entries(styles).forEach(([key, value]) => {
                element.style[key] = value;
            });
        });
    });
};
