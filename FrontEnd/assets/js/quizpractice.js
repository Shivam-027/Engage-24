let quizData = [];

async function getQuiz() {
    const subject = document.getElementById('subject').value;
    const level = document.getElementById('level').value;
    const questions = document.getElementById('questions').value;

    const response = await fetch('http://127.0.0.1:5000/get_quiz', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ subject, level, questions })
    });

    quizData = await response.json();
    renderQuiz(quizData);
}

function renderQuiz(quizData) {
    const quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = '';
    quizData.forEach((item, index) => {
        const questionElem = document.createElement('div');
        questionElem.classList.add('question');
        questionElem.innerHTML = `
                    <h3>Question ${index + 1}: ${item.question}</h3>
                    <ul class="options">
                        ${item.options.map((option, i) => `
                            <li>
                                <label>
                                    <input type="radio" name="question${index}" value="${i}"> ${option}
                                </label>
                            </li>
                        `).join('')}
                    </ul>
                `;
        quizContainer.appendChild(questionElem);
    });

    const submitButton = document.createElement('button');
    submitButton.innerText = 'Submit Quiz';
    submitButton.onclick = submitQuiz;
    quizContainer.appendChild(submitButton);
    button.setAttribute('id', 'submitbtn');
}

function submitQuiz() {
    const quizContainer = document.getElementById('quiz-container');
    const questions = quizContainer.querySelectorAll('.question');
    let score = 0;
    let allAnswered = true;

    questions.forEach((question, index) => {
        const selectedOption = question.querySelector('input[type="radio"]:checked');

        if (!selectedOption) {
            allAnswered = false;
        }
    });

    if (!allAnswered) {
        alert('Please answer all questions before submitting.');
        return;
    }

    questions.forEach((question, index) => {
        const selectedOption = question.querySelector('input[type="radio"]:checked');
        const correctAnswer = quizData[index].answer;

        if (selectedOption) {
            const answer = parseInt(selectedOption.value);
            if (answer === correctAnswer) {
                score++;
            }
        }

        const options = question.querySelectorAll('li');
        options.forEach((option, i) => {
            if (i === correctAnswer) {
                option.classList.add('correct');
                const arrow = document.createElement('span');
                arrow.classList.add('arrow');
                arrow.innerText = '✔';
                option.appendChild(arrow);
            }
        });
    });

    const resultContainer = document.getElementById('result');
    resultContainer.innerText = `You scored ${score} out of ${questions.length}`;
}

// Show dropdown on hover for Profile button
const profileButton = document.querySelector('.animated-button.link3');
const dropdownContent2 = document.getElementById('dropdown-content2');

// Show the dropdown when hovering over the profile button
profileButton.addEventListener('mouseenter', () => {
    dropdownContent2.style.display = 'block';
});

// Hide the dropdown when not hovering over the profile button
profileButton.addEventListener('mouseleave', () => {
    dropdownContent2.style.display = 'none';
});