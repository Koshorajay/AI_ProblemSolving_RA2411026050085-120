let board = ["","","","","","","","",""];
let gameOver = false;

const boardDiv = document.getElementById("board");
const status = document.getElementById("status");

// Create board
for (let i = 0; i < 9; i++) {
    let btn = document.createElement("button");
    btn.classList.add("cell");
    btn.onclick = () => playerMove(i);
    boardDiv.appendChild(btn);
}

// Check winner
function checkWinner(b, p) {
    const wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];
    return wins.some(c => c.every(i => b[i] === p));
}

// Minimax AI
function minimax(newBoard, isMax) {
    if (checkWinner(newBoard, "X")) return -1;
    if (checkWinner(newBoard, "O")) return 1;
    if (!newBoard.includes("")) return 0;

    if (isMax) {
        let best = -Infinity;
        for (let i=0;i<9;i++){
            if(newBoard[i]==""){
                newBoard[i]="O";
                best = Math.max(best, minimax(newBoard,false));
                newBoard[i]="";
            }
        }
        return best;
    } else {
        let best = Infinity;
        for (let i=0;i<9;i++){
            if(newBoard[i]==""){
                newBoard[i]="X";
                best = Math.min(best, minimax(newBoard,true));
                newBoard[i]="";
            }
        }
        return best;
    }
}

// Best move
function bestMove() {
    let bestVal = -Infinity;
    let move = -1;

    for (let i=0;i<9;i++){
        if(board[i]==""){
            board[i]="O";
            let val = minimax(board,false);
            board[i]="";

            if(val > bestVal){
                bestVal = val;
                move = i;
            }
        }
    }
    return move;
}

// Player move
function playerMove(i){
    if(board[i]!=="" || gameOver) return;

    board[i]="X";
    updateUI();

    if(checkWinner(board,"X")){
        status.innerText="You Win!";
        gameOver=true;
        return;
    }

    let ai = bestMove();
    board[ai]="O";
    updateUI();

    if(checkWinner(board,"O")){
        status.innerText="AI Wins!";
        gameOver=true;
    }
}

// Update UI
function updateUI(){
    document.querySelectorAll(".cell").forEach((c,i)=>{
        c.innerText = board[i];
    });
}

// Reset
function resetGame(){
    board = ["","","","","","","","",""];
    gameOver=false;
    status.innerText="Your Turn";
    updateUI();
}