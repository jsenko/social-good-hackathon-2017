import React from 'react';
import ReactDOM from 'react-dom';
// import './index.css';
import Sudoku from './ReactSudoku.js';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Sudoku />, document.getElementById('root'));
registerServiceWorker();
