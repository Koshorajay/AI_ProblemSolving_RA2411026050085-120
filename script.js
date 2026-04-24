let board = ["","","","","","","","",""];
let gameOver = false;

const boardDiv = document.getElementById("board");
const status = document.getElementById("status");

// -------- CREATE BOARD --------
function createBoard() {
    boardDiv.innerHTML = "";
    for (let i = 0; i < 9; i++) {
        let cell = document.createElement("button");
        cell.classList.add("cell");
        cell.addEventListener("click", () => handleMove(i));
        boardDiv.appendChild(cell);
    }
}
createBoard();

// -------- CHECK WINNER --------
function checkWinner(b, player) {
    const winPatterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ];
    return winPatterns.some(pattern =>
        pattern.every(index => b[index] === player)
    );
}

// -------- MINIMAX --------
function minimax(newBoard, isMaximizing) {
    if (checkWinner(newBoard, "X")) return -1;
    if (checkWinner(newBoard, "O")) return 1;
    if (!newBoard.includes("")) return 0;

    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (newBoard[i] === "") {
                newBoard[i] = "O";
                let score = minimax(newBoard, false);
                newBoard[i] = "";
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (newBoard[i] === "") {
                newBoard[i] = "X";
                let score = minimax(newBoard, true);
                newBoard[i] = "";
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

// -------- BEST MOVE --------
function getBestMove() {
    let bestScore = -Infinity;
    let move = -1;

    for (let i = 0; i < 9; i++) {
        if (board[i] === "") {
            board[i] = "O";
            let score = minimax(board, false);
            board[i] = "";

            if (score > bestScore) {
                bestScore = score;
                move = i;
            }
        }
    }
    return move;
}

// -------- HANDLE PLAYER MOVE --------
function handleMove(index) {
    if (board[index] !== "" || gameOver) return;

    board[index] = "X";
    updateUI();

    if (checkWinner(board, "X")) {
        status.innerText = "🎉 You Win!";
        gameOver = true;
        return;
    }

    if (!board.includes("")) {
        status.innerText = "🤝 Draw!";
        gameOver = true;
        return;
    }

    status.innerText = "🤖 AI Thinking...";

    setTimeout(() => {
        let aiMove = getBestMove();
        board[aiMove] = "O";
        updateUI();

        if (checkWinner(board, "O")) {
            status.innerText = "😈 AI Wins!";
            gameOver = true;
        } else if (!board.includes("")) {
            status.innerText = "🤝 Draw!";
            gameOver = true;
        } else {
            status.innerText = "Your Turn";
        }
    }, 400); // delay for realism
}

// -------- UPDATE UI --------
function updateUI() {
    const cells = document.querySelectorAll(".cell");

    cells.forEach((cell, i) => {
        cell.innerText = board[i];

        // remove old styles
        cell.classList.remove("x", "o");

        // apply color classes
        if (board[i] === "X") {
            cell.classList.add("x");
        } else if (board[i] === "O") {
            cell.classList.add("o");
        }
    });
}

// -------- RESET GAME --------
function resetGame() {
    board = ["","","","","","","","",""];
    gameOver = false;
    status.innerText = "Your Turn";
    updateUI();
}
