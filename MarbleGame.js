/******************************************************************************\
|                                                                              |
|                                 Dependencies                                 |
|                                                                              |
\******************************************************************************/
const MARBLE = '🌎';
const GAP = '🔘';

var gameBoard =
[
    [MARBLE],
    [MARBLE,MARBLE],
    [MARBLE,MARBLE,MARBLE],
    [MARBLE,MARBLE,MARBLE,MARBLE],
    [MARBLE,MARBLE,MARBLE,MARBLE,MARBLE],
];
gameBoard[2][1] = GAP;  // Starting gap position

/******************************************************************************\
|                                                                              |
|                                 Main Script                                  |
|                                                                              |
\******************************************************************************/
module.exports = {
    run() 
    {
        printBoard(gameBoard);

        /* Find first gap */
        let gap = makeSpot(gameBoard.indexOf(gameBoard.find(row => row.indexOf(GAP) != -1)),
                            gameBoard.find(row => row.indexOf(GAP) != -1).indexOf(GAP));
        let jumpers = searchJumpers(gameBoard, gap);
        objPrint("Possible Jumps", jumpers);
        
        jumpFrom(jumpers[0], gap);
    }
}

/******************************************************************************\
|                                                                              |
|                                Local Functions                               |
|                                                                              |
\******************************************************************************/
const makeSpot = (row, index) => {
    return {row: row, index: index}
}
const objPrint = (title, object) => {
    process.stdout.write(title + ": ");
    console.log(object);
    console.log('');
}

/************************* printBoard(board) **********************************\
|
| Description: Prints the game board to the console
|
\******************************************************************************/
function printBoard(board)
{
    console.log('');
    let rowCount = board.length;
    for(var r = 0; r < rowCount; r++) 
    {
        let output = '';
        output += '  '.repeat(rowCount - r); // Center row
        for(var i = 0; i < board[r].length; i++) 
        {
            output += board[r][i] + '  '; // Add marble or gap
        }
        console.log(output);    // Print row 
    }
    console.log('');
}

/**************************** countMarbles() **********************************\
|
| Description: Returns how many marbles are on the game board
|
\******************************************************************************/
function countMarbles()
{
    let count = 0;
    for(let r = 0; r < gameBoard.length; r++)
    {
        for(let i = 0; i < gameBoard[r].length; i++)
        {
            if(gameBoard[r][i] === MARBLE) count++;
        }
    }
    return count;
}

/************************* searchJumpers(board) *******************************\
|
| Description: Returns an array containing all jumper marbles for a given gap
|
\******************************************************************************/
function searchJumpers(board, gap)
{
    /* Get possible jumpers */
    validJumps = [];
    [gap.row - 2, gap.row, gap.row + 2].forEach((row) => 
    {
        if(row >= 0 && row < board.length) // Only check rows inside the board
        {
            /* Add left jumpers */
            let leftIdx = (row > gap.row) ? gap.index : gap.index - 2;
            if(leftIdx >= 0 && board[row][leftIdx] == MARBLE) validJumps.push(makeSpot(row, leftIdx));

            /* Add right jumpers */
            let rightIdx = (row >= gap.row) ? gap.index + 2 : gap.index;
            if(rightIdx < board[row].length && board[row][rightIdx] == MARBLE) validJumps.push(makeSpot(row, rightIdx));
        }
    });
    return validJumps;
}

/************************** jumpFrom(jumper, target) **************************\
|
| Description: Attempts to jump from jumper to target, returns false if invalid jump
|
\******************************************************************************/
function jumpFrom(jumper, target)
{
    objPrint("Jumper", jumper);
    objPrint("Target", target);
    let jRow = (jumper.row + target.row) / 2;
    let jIdx = (jumper.index == target.index) ? jumper.index
            :  (jumper.index > target.index) ? jumper.index - target.index  // Difference if jumping up row
            :   jumper.index + target.index / 2;    // Average if jumping down row

    if(gameBoard[jRow][jIdx] === GAP) return false; // Check if there is a marble to jump
    else
    {   /* Make the jump and print new board */
        gameBoard[target.row][target.index] = MARBLE;
        gameBoard[jumper.row][jumper.index] = GAP;
        gameBoard[jRow][jIdx] = GAP;
        printBoard(gameBoard);
        return true;
    }
}

/******************************************************************************\
|                                                                              |
|                                  End of File                                 |
|                                                                              |
\******************************************************************************/