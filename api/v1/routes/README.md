#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

function generateReadme() {
  const template = `
  # Frontend App

  ## Table of Contents
  * [Introduction](#introduction)
  * [Features](#features)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Contributing](#contributing)
  * [License](#license)
  * [Acknowledgments](#acknowledgments)

  ## Introduction
  This is a high-quality frontend application built with cutting-edge technologies.

  ## Features
  * This application has a clean and responsive design.
  * It has a user-friendly interface.

  ## Installation
  This application requires Node.js to be installed on your system. Run the following command in your terminal:
  ```bash
  npm install
  ```
  Then run the application using:
  ```bash
  npm start
  ```

  ## Usage
  Open your web browser and navigate to http://localhost:3000.

  ## Contributing
  Please see our contribution guidelines for more information.

  ## License
  This project is licensed under the MIT License.

  ## Acknowledgments
  We would like to thank our contributors for their hard work.
  ```
  fs.writeFile('README.md', template, (err) => {
    if (err) throw err;
    console.log('README.md generated successfully');
  });
}

generateReadme();