const path = require("path");

const config = {
    entry: "./src/index.js",
    output: {
        path: path.resolve(__dirname, "static/frontend/js/"),
        filename: "bundle.js",
    },
    module: {
        rules: [
            {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader",
            },
            },
        ],
    },
    devServer: {
        writeToDisk: true,
    }
};

module.exports = config;