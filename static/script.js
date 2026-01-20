let questions = [];
let currentIdx = 0;
let timer;
let timeLeft = 0;
const money = ["$100","$200","$300","$500","$1,000","$2,000","$4,000","$8,000","$16,000","$32,000","$64,000","$125,000","$250,000","$500,000","$1 MILLION"];

function initGame() {
    document.getElementById('start-screen').style.display = 'none';
    startGame();
}

async function startGame() {
    try {
        const response = await fetch('/api/questions');
        questions = await response.json();
        setupLadder();
        loadQuestion();
    } catch (e) {
        document.getElementById('q-text').innerText = "Database Connection Error.";
    }
}

function loadQuestion() {
    if (currentIdx >= 15) return showEndScreen(true);
    
    const currentQ = questions[currentIdx];
    timeLeft = currentQ.difficulty === 'easy' ? 45 : (currentQ.difficulty === 'medium' ? 75 : 90);
    
    document.getElementById('timer-text').innerText = timeLeft;
    document.getElementById('timer-text').style.color = "var(--neon-gold)";
    document.getElementById('q-text').innerText = currentQ.text;
    document.getElementById('prize-tag').innerText = `CURRENT PRIZE: ${money[currentIdx]}`;
    
    currentQ.options.forEach((opt, i) => {
        document.getElementById(`opt${i}`).innerText = opt;
    });
    
    updateLadderUI();
    startTimer();
}

function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
        timeLeft--;
        const display = document.getElementById('timer-text');
        display.innerText = timeLeft;
        if (timeLeft <= 10) display.style.color = "var(--neon-red)";

        if (timeLeft <= 0) {
            clearInterval(timer);
            showEndScreen(false, "Time Expired!");
        }
    }, 1000);
}

function selectAnswer(i) {
    clearInterval(timer);
    const buttons = document.querySelectorAll('.opt-btn');
    const correctAns = questions[currentIdx].answer;
    const selectedAns = questions[currentIdx].options[i];

    buttons.forEach(b => b.disabled = true);
    buttons[i].style.borderColor = "orange";

    setTimeout(() => {
        if (selectedAns === correctAns) {
            buttons[i].style.background = "var(--neon-green)";
            buttons[i].style.color = "black";
            setTimeout(() => {
                currentIdx++;
                resetButtons();
                loadQuestion();
            }, 1200);
        } else {
            buttons[i].style.background = "var(--neon-red)";
            setTimeout(() => {
                showEndScreen(false, correctAns);
            }, 1200);
        }
    }, 1000);
}

function showEndScreen(won, correctStr = "") {
    const screen = document.getElementById('end-screen');
    const viewport = document.getElementById('game-viewport');
    
    screen.classList.remove('hidden');
    viewport.classList.add('blur-effect');

    if (won) {
        document.getElementById('result-title').innerText = "MILLIONAIRE!";
        confetti({ particleCount: 300, spread: 100, origin: { y: 0.6 } });
    } else {
        document.getElementById('result-title').innerText = "GAME OVER";
        document.getElementById('correct-reveal').innerText = correctStr;
        document.getElementById('wrong-reveal-box').classList.remove('hidden');
    }
    document.getElementById('final-prize').innerText = currentIdx > 0 ? money[currentIdx-1] : "$0";
}

function resetButtons() {
    document.querySelectorAll('.opt-btn').forEach(b => {
        b.style = "";
        b.disabled = false;
    });
}

function setupLadder() {
    const ladder = document.getElementById('ladder');
    ladder.innerHTML = '';
    money.forEach((m, i) => {
        const div = document.createElement('div');
        div.id = `step-${i}`;
        div.className = 'ladder-step';
        div.innerText = `${i+1} • ${m}`;
        ladder.appendChild(div);
    });
}

function updateLadderUI() {
    document.querySelectorAll('.ladder-step').forEach((s, i) => {
        s.classList.remove('active', 'completed');
        if (i === currentIdx) s.classList.add('active');
        if (i < currentIdx) s.classList.add('completed');
    });
}