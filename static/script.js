let questions = [];
let currentIdx = 0;
let timer;
let timeLeft = 0;
let isPaused = false; // Added state
const money = ["100 QP","200 QP","300 QP","500 QP","1,000 QP","2,000 QP","4,000 QP","8,000 QP","16,000 QP","32,000 QP","64,000 QP","125,000 QP","250,000 QP","500,000 QP","1 MILLION QP"];

const sfxLock = new Audio('/static/sounds/lock.mp3');
const sfxCorrect = new Audio('/static/sounds/correct.mp3');
const sfxWrong = new Audio('/static/sounds/wrong.mp3');

function initGame() {
    sfxLock.play().then(() => {
        sfxLock.pause();
        sfxLock.currentTime = 0;
    }).catch(e => console.log("Audio waiting"));

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
    
    isPaused = false; // Reset pause on new question
    document.getElementById('feedback-bar').classList.add('hidden');
    document.getElementById('game-viewport').classList.remove('blur-game');
    
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

// Updated startTimer to support Pause
function startTimer() {
    clearInterval(timer);
    timer = setInterval(() => {
        if (!isPaused) { // Only countdown if NOT paused
            timeLeft--;
            const display = document.getElementById('timer-text');
            display.innerText = timeLeft;
            if (timeLeft <= 10) display.style.color = "var(--neon-red)";
            if (timeLeft <= 0) {
                clearInterval(timer);
                showEndScreen(false, questions[currentIdx].answer);
            }
        }
    }, 1000);
}

// New Toggle Pause Function
function togglePause() {
    if (currentIdx >= 15) return;

    isPaused = !isPaused;
    const btn = document.getElementById('pause-toggle');
    const viewport = document.getElementById('game-viewport');
    const optionButtons = document.querySelectorAll('.opt-btn');

    if (isPaused) {
        btn.innerText = "RESUME";
        btn.classList.add('active');
        viewport.classList.add('blur-game');
        optionButtons.forEach(b => b.disabled = true);
    } else {
        btn.innerText = "PAUSE";
        btn.classList.remove('active');
        viewport.classList.remove('blur-game');
        optionButtons.forEach(b => b.disabled = false);
    }
}

function selectAnswer(i) {
    if (isPaused) return; // Prevent clicking while paused
    
    clearInterval(timer);
    const buttons = document.querySelectorAll('.opt-btn');
    const correctAns = questions[currentIdx].answer;
    const selectedAns = questions[currentIdx].options[i];

    sfxLock.play();
    buttons.forEach(b => b.disabled = true);
    buttons[i].style.borderColor = "orange";
    buttons[i].style.boxShadow = "0 0 15px orange";

    setTimeout(() => {
        if (selectedAns === correctAns) {
            sfxCorrect.play();
            buttons[i].style.background = "var(--neon-green)";
            buttons[i].style.color = "black";
            buttons[i].style.borderColor = "var(--neon-green)";
            showFeedbackBar();
        } else {
            sfxWrong.play();
            buttons[i].style.background = "var(--neon-red)";
            buttons.forEach(b => {
                if(b.innerText.includes(correctAns)) {
                    b.style.background = "var(--neon-green)";
                    b.style.color = "black";
                }
            });
            setTimeout(() => { showEndScreen(false, correctAns); }, 1500);
        }
    }, 1200);
}

function showFeedbackBar() {
    const bar = document.getElementById('feedback-bar');
    const text = document.getElementById('feedback-text');
    const viewport = document.getElementById('game-viewport');
    
    viewport.classList.add('blur-game');
    bar.classList.remove('hidden');
    text.innerHTML = `CORRECT!<br><span style="color:var(--neon-gold); font-size: 1.1rem;">PRIZE: ${money[currentIdx]}</span>`;
}

function loadNextQuestion() {
    currentIdx++;
    resetButtons();
    loadQuestion();
}

function showEndScreen(won, correctStr = "") {
    const screen = document.getElementById('end-screen');
    const viewport = document.getElementById('game-viewport');
    
    screen.classList.remove('hidden');
    viewport.classList.add('blur-game');

    if (won) {
        document.getElementById('result-title').innerText = "MILLIONAIRE!";
        confetti({ particleCount: 300, spread: 100, origin: { y: 0.6 } });
    } else {
        document.getElementById('result-title').innerText = "GAME OVER";
        document.getElementById('correct-reveal').innerText = correctStr;
        document.getElementById('wrong-reveal-box').classList.remove('hidden');
    }
    document.getElementById('final-prize').innerText = currentIdx > 0 ? money[currentIdx-1] : "0 QP";
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
    money.slice().reverse().forEach((m, i) => {
        const actualIdx = 14 - i; 
        const div = document.createElement('div');
        div.id = `step-${actualIdx}`;
        div.className = 'ladder-step';
        div.innerText = `${actualIdx + 1} • ${m}`;
        ladder.appendChild(div);
    });
}

function updateLadderUI() {
    document.querySelectorAll('.ladder-step').forEach((s) => {
        const stepIdx = parseInt(s.id.split('-')[1]);
        s.classList.remove('active', 'completed');
        if (stepIdx === currentIdx) s.classList.add('active');
        if (stepIdx < currentIdx) s.classList.add('completed');
    });
}