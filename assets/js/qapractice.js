 // Define global variables
 let questions = [];
 let answers = [];
 let currentQuestionIndex = 0;

 // Function to fetch questions from the server
 async function fetchQuestions() {
     const subject = document.getElementById('subject').value;
     const level = document.getElementById('level').value;
     const numQuestions = parseInt(document.getElementById('num_questions').value, 10);

     try {
         const response = await fetch('http://127.0.0.1:5000/get_questions', {
             method: 'POST',
             headers: {
                 'Content-Type': 'application/json',
             },
             body: JSON.stringify({
                 subject: subject,
                 level: level,
                 num_questions: numQuestions
             })
         });

         if (response.ok) {
             const data = await response.json();
             questions = data.questions;
             answers = data.answers;
             currentQuestionIndex = 0;
             displayQuestion();
         } else {
             console.error('Failed to fetch questions:', response.statusText);
         }
     } catch (error) {
         console.error('Error fetching questions:', error);
     }
 }

 // Function to submit an answer
 async function submitAnswer() {
     const question = questions[currentQuestionIndex];
     const correctAnswer = answers[currentQuestionIndex];
     const userAnswer = document.getElementById('user-answer').value;

     if (!userAnswer.trim()) {
         alert("Your answer is empty. Please write your answer to move to the next question.");
         return;
     }

     try {
         const response = await fetch('http://127.0.0.1:5000/verify_answer', {
             method: 'POST',
             headers: {
                 'Content-Type': 'application/json',
             },
             body: JSON.stringify({
                 question: question,
                 answer: correctAnswer,
                 user_answer: userAnswer
             })
         });

         if (response.ok) {
             const data = await response.json();
             displayResult(data.result);
         } else {
             console.error('Failed to verify answer:', response.statusText);
         }
     } catch (error) {
         console.error('Error verifying answer:', error);
     }
 }

 // Function to display the current question
 function displayQuestion() {
     if (questions.length > 0 && currentQuestionIndex < questions.length) {
         const questionElement = document.getElementById('question-text');
         const answerElement = document.getElementById('user-answer');
         const submitButton = document.getElementById('submitAnswerButton');

         questionElement.textContent = questions[currentQuestionIndex];
         answerElement.value = '';

         // Manage button visibility
         if (questions.length === 1) {
             document.getElementById('previousQuestionButton').classList.add('hidden');
             document.getElementById('nextQuestionButton').classList.remove('hidden');
             document.getElementById('refreshQuestionsButton').classList.add('hidden');
         } else if (currentQuestionIndex === 0) {
             document.getElementById('previousQuestionButton').classList.add('hidden');
             document.getElementById('nextQuestionButton').classList.remove('hidden');
             document.getElementById('refreshQuestionsButton').classList.add('hidden');
         } else if (currentQuestionIndex === questions.length - 1) {
             document.getElementById('previousQuestionButton').classList.remove('hidden');
             document.getElementById('nextQuestionButton').classList.add('hidden');
             document.getElementById('refreshQuestionsButton').classList.remove('hidden');
         } else {
             document.getElementById('previousQuestionButton').classList.remove('hidden');
             document.getElementById('nextQuestionButton').classList.remove('hidden');
             document.getElementById('refreshQuestionsButton').classList.add('hidden');
         }

         document.getElementById('questions-container').style.display = 'block';
     }
 }

 // Function to display the result of answer verification
 function displayResult(result) {
     const resultElement = document.getElementById('result');
     resultElement.innerHTML = `<div class="correct-answer">Correct Answer: ${answers[currentQuestionIndex]}</div>
                                <div class="result-text">Result: ${result}</div>`;
 }

 // Function to handle next question
 function nextQuestion() {
     if (currentQuestionIndex < questions.length - 1) {
         const userAnswer = document.getElementById('user-answer').value;
         if (!userAnswer.trim()) {
             alert("Your answer is empty. Please write your answer to move to the next question.");
             return;
         }
         currentQuestionIndex++;
         resetQuestionState();
         displayQuestion();
     }
 }

 // Function to handle previous question
 function previousQuestion() {
     if (currentQuestionIndex > 0) {
         currentQuestionIndex--;
         resetQuestionState();
         displayQuestion();
     }
 }

 // Function to refresh questions
 function refreshQuestions() {
     resetQuestionState();
     fetchQuestions();
 }

 // Function to reset the question state
 function resetQuestionState() {
     document.getElementById('user-answer').value = '';
     document.getElementById('result').innerHTML = '';
 }

 // Event listener for the Get Questions button
 document.getElementById('getQuestionsButton').addEventListener('click', fetchQuestions);


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