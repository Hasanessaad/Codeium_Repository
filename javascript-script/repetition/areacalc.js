const calculateArea = (shape, ...args) => {
    switch (shape) {
        case 'rectangle':
            return args[0] * args[1];
        case 'circle':
            return Math.PI * (args[0] ** 2);
        case 'triangle':
            return (args[0] * args[1]) / 2;
        default:
            throw new Error('Invalid shape');
    }
};
