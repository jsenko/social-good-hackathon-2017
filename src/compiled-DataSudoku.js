'use strict';

Object.defineProperty(exports, "__esModule", {
	value: true
});
exports.Sudoku = undefined;

var _immutable = require('immutable');

const Sudoku = function (JSON) {
	const ImmutableSudoku = (0, _immutable.fromJS)(JSON).toList();
	const getRow = sudoku => i => {
		return ImmutableSudoku.get(i);
	};
	const getColumn = sudoku => i => {
		return sudoku.map(x => x.splice(0, i).setSize(1)).reduce((x, y) => x.concat(y));
	};
	const getBox = sudoku => (i, j) => {
		return sudoku.skip(i * 3).take(3).map(x => x.skip(j * 3).take(3)).reduce((x, y) => x.concat(y));
	};
	const getField = sudoku => (i, j) => {
		return sudoku.get(i).get(j);
	};
	const reverse = sudoku => {
		return (0, _immutable.List)((0, _immutable.Range)(0, Infinity).take(9).map(x => sudoku.getColumn(x)));
	};
	const setField = sudoku => (i, j) => value => {
		return sudoku.set(i, sudoku.get(i).set(j, value));
	};
	ImmutableSudoku.getRow = getRow(ImmutableSudoku);
	ImmutableSudoku.getColumn = getColumn(ImmutableSudoku);
	ImmutableSudoku.getBox = getBox(ImmutableSudoku);
	ImmutableSudoku.getField = getField(ImmutableSudoku);
	ImmutableSudoku.reverse = reverse(ImmutableSudoku);
	ImmutableSudoku.setField = setField(ImmutableSudoku);

	return ImmutableSudoku;
}; // USAGE:
// const sudoku = Sudoku(JSON);
//
// JSON = {
// 	0: [val00, val01, .., val08],
// 	.
// 	.
// 	8: [val80, val81, .., val88],
// }

exports.Sudoku = Sudoku;
