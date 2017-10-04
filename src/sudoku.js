import React, { Component } from 'react';
// import './sudoku.css';

var generateSudokuBoard = ()=>{
	return;
};
	
class Sudoku extends Component {
	constructor(){
		super();
		this.state = {
			history: [
				{
					board: generateSudokuBoard(),	
				}
			],
			value: 'ahaho',
		}
	}

  render() {
    return (
			<p>Sudoku {this.state.value}</p>
   );
  }
}

export default Sudoku;
