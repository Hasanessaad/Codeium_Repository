const validateForm = (form) => {
    const errors = {};

    if (!form.name || form.name.trim() === '') {
        errors.name = 'Nome é obrigatório.';
    }

    if (!form.email || !/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(form.email)) {
        errors.email = 'E-mail é obrigatório e deve estar no formato correto.';
    }

    if (!form.password || form.password.trim() === '') {
        errors.password = 'Senha é obrigatória.';
    }

    return errors;
};
