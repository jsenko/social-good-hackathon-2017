// USAGE:
	// const sudoku = Sudoku(listOfLists);
	//
	// listOfLists = List([
	// 	List([val00, val01, .., val08]),
	// 	.
	// 	.
	// 	List([val80, val81, .., val88]),
	// )]
import { List, Range } from 'immutable';

const Sudoku = function(listOfLists) {
	const ImmutableSudoku = Object.create(listOfLists);
	const getRow = sudoku => i => {
		return sudoku.get(i);
	};
	const getColumn = sudoku => j => {
		return sudoku
							.map(x => x.get(j));
	};
	const getBox = sudoku => i => {
		return sudoku
			.skip(Math.trunc(i/3)*3).take(3)
			.map(x => x.skip((i%3)*3).take(3))
			.reduce((x,y) => x.concat(y));
	};
	//const getBox = sudoku => (i,j) => {
		//return sudoku
							//.skip(i*3).take(3)
							//.map(x => x.skip(j*3).take(3))
							//.reduce((x,y) => x.concat(y));
	//};
	const getField = sudoku => (i,j) => {
		return sudoku.get(i).get(j);
	};
	const rvrs = sudoku => {
		return Sudoku( List([0,1,2,3,4,5,6,7,8]).map(x => sudoku.getColumn(x)) ); 
	};
	const setField = sudoku => (fieldRow,fieldColumn) => value => {
		return sudoku.set(fieldRow, sudoku.get(fieldRow).set(fieldColumn, value));
	};
	const boxify = sudoku => {
		return Sudoku( Range(0,Infinity).take(9).map(x => sudoku.getBox(x)) );
	};
	ImmutableSudoku.getRow = getRow(ImmutableSudoku);
	ImmutableSudoku.getColumn = getColumn(ImmutableSudoku);
	ImmutableSudoku.getBox = getBox(ImmutableSudoku);
	ImmutableSudoku.getField = getField(ImmutableSudoku);
	ImmutableSudoku.rvrs = () => rvrs(ImmutableSudoku);
	ImmutableSudoku.boxify = () => boxify(ImmutableSudoku);
	ImmutableSudoku.setField = setField(ImmutableSudoku);
	//ImmutableSudoku.id = ImmutableSudoku.rvrs.rvrs;

	return ImmutableSudoku;
};

export {Sudoku};
