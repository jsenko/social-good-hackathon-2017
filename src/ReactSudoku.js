import React, { Component } from 'react';
import { List, fromJS } from 'immutable';
import {Sudoku} from './DataSudoku.js';
import './sudoku.css';

const JSON = {
	0: [1,2,3,4,5,6,7,8,9],
	1: [1,2,3,4,5,6,7,8,9],
	2: [1,2,3,4,5,6,7,8,9],
	3: [1,2,3,4,5,6,7,8,9],
	4: [1,2,3,4,5,6,7,8,9],
	5: [1,2,3,4,5,6,7,8,9],
	6: [undefined,2,3,4,5,6,7,8,9],
	7: [1,2,3,4,undefined,6,7,8,9],
	8: [1,2,3,4,5,6,7,8,undefined],
};

class SudokuGame extends Component {
	constructor(){
		super();
		const sudokuTemplate = Sudoku(fromJS(JSON).toList());
		console.log(sudokuTemplate.toJS());
		this.state = {
			history: List([sudokuTemplate.rvrs().boxify()]),
			pointInHistory: -1,	//negative indices in '.get' method of 'List' in immutableJS count from end of the list e.g. List([0,1,2,3]).get(-1) returns 3
		}
	}

	handleStepForward = () => {
		let newPointInHistory;
		if (this.state.pointInHistory === -1) {
			newPointInHistory = this.state.pointInHistory;
		}
		else {
			newPointInHistory = this.state.pointInHistory + 1;
		}

		this.setState(
			{
				history: this.state.history,
				pointInHistory: newPointInHistory,
			}
		);
	}

	handleStepBack = () => {
		let newPointInHistory;
		if (this.state.pointInHistory <= -this.state.history.size) {
			newPointInHistory = this.state.pointInHistory;
		}
		else {
			newPointInHistory = this.state.pointInHistory - 1;
		}

		this.setState(
			{
				history: this.state.history,
				pointInHistory: newPointInHistory,
			}
		);
	}

	handleInput = (i,j) => value => {
		const oldHistory = this.state.history;
		const now = this.state.pointInHistory;
		this.setState(
			{
				history: oldHistory.skipLast(-(now + 1)).push(oldHistory.get(-1).setField(i,j)(value)),
				pointInHistory: -1,
			}
		);
	}

  render() {
    return (
			<div id="SudokuGame">
				<h1>Sudoku Game</h1>	
				<HistoryNavigation 
					handleStepBack={this.handleStepBack}
					handleStepForward={this.handleStepForward}
				/>
				<SudokuBoard 
					board={this.state.history.get(this.state.pointInHistory)}
					handleInput={this.handleInput}
				/>
			</div>	
   );
  }
}

function SudokuBoard(props) {
	const renderRowOfBoxes = rowNum => {
		return (
			<div id={"boxRow"+rowNum} className="boxRow">
				<SudokuBox box={props.board.getBox(rowNum*3 + 0)} />
				<SudokuBox box={props.board.getBox(rowNum*3 + 1)} />
				<SudokuBox box={props.board.getBox(rowNum*3 + 2)} />
			</div>
		);
	};

	return (
		<div id="SudokuBoard">
				{renderRowOfBoxes(0)}
				{renderRowOfBoxes(1)}
				{renderRowOfBoxes(2)}
		</div>
	);
}

function SudokuBox(props) {
	const renderRowOfFields= rowNum => {
		return (
			<div id={"fieldRow"+rowNum}>
				<SudokuField value={props.box.get(rowNum*3+0)} />
				<SudokuField value={props.box.get(rowNum*3+1)} />
				<SudokuField value={props.box.get(rowNum*3+2)} />
			</div>
		);
	};

	return (
		<span className="SudokuBox">
			{renderRowOfFields(0)}
			{renderRowOfFields(1)}
			{renderRowOfFields(2)}
		</span>
	);
}

function SudokuField(props) {
	const renderField = function () {
		if (props.value === undefined) {
			return (
				<input className="SudokuField"></input>
			);
		}
		if (props.isInCollision){
			return (
				<div style={{color:"red",}}	className="SudokuField">{props.value}</div>
			);
		}

		return (
			<div className="SudokuField">{props.value}</div>
		);
	};

	return renderField();
}

function HistoryNavigation(props) {
	return (
		<div id="HistoryNavigation">
			<button onClick={props.handleStepBack}>Step back</button>
			<button onClick={props.handleStepForward}>Step forward</button>
		</div>
	);
}

export default SudokuGame;
