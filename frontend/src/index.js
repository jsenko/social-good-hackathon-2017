import React from 'react';
import ReactDOM from 'react-dom';
import './style.css';
import Container from './componenets_advocateInfo.js';
import registerServiceWorker from './registerServiceWorker';
//import { Highcharts} from 'highcharts';

ReactDOM.render(<Container />, document.getElementById('root'));
registerServiceWorker();
