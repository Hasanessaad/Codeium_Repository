const requestAPI = (url, callback) => {
    fetch(url)
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.error(error))
}

const getUserInfo = (userId, callback) => requestAPI(`https://api.example.com/users/${userId}`, callback)

const getProductInfo = (productId, callback) => requestAPI(`https://api.example.com/products/${productId}`, callback)

const getOrders = (callback) => requestAPI('https://api.example.com/orders', callback)
