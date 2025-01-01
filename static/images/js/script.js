const outputDiv = document.getElementById('output');
let eventSource;
const timeDiv = document.getElementById('time');
const dateDiv = document.getElementById('date');
const locationDiv = document.getElementById('location');
const weatherDiv = document.getElementById('weather');

// OpenWeather API Key (Replace with your API key)
const apiKey = '4a55ed1973c7bd7587d913b9a3656921';
const weatherApiUrl = 'https://api.openweathermap.org/data/2.5/weather?appid=' + apiKey;

// Function to get the current time and date
function updateTimeAndDate() {
    const now = new Date();
    const time = now.toLocaleTimeString();
    const date = now.toLocaleDateString();

    timeDiv.textContent = time;
    dateDiv.textContent = date;
}

// Function to get the location and weather
function updateLocationAndWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            // Get location info
            fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${apiKey}`)
                .then(response => response.json())
                .then(data => {
                    const city = data.name;
                    const region = data.sys.country;
                    locationDiv.textContent = `${city}, ${region}`;

                    const weatherDescription = data.weather[0].description;
                    const temperature = (data.main.temp - 273.15).toFixed(1);
                    weatherDiv.textContent = `${temperature}°C, ${weatherDescription}`;
                });
        });
    } else {
        locationDiv.textContent = "Location access denied";
        weatherDiv.textContent = "Weather data unavailable";
    }
}

// Update time and date every second
setInterval(updateTimeAndDate, 1000);

// Fetch location and weather once
updateLocationAndWeather();

// List of random statements
const statements = [
    "Welcome to Jarvis, your personal assistant.",
    "Jarvis is powered by artificial intelligence.",
    "Created with ❤️ by Sameer, an aspiring developer.",
    "Jarvis learns and evolves with time.",
    "Your requests are my command!",
    "Jarvis will assist you in managing your tasks effortlessly.",
    "Jarvis is ready to serve you!",
    "Every task is an opportunity for Jarvis to shine.",
    "Jarvis, your personal assistant, always at your service.",
    "You are just a command away from Jarvis's help.",
    "With Jarvis, your productivity reaches new heights.",
    "Feel free to ask Jarvis anything. I'm always here.",
    "Jarvis will handle it for you.",
    "Your personal AI assistant, powered by Jarvis.",
    "Jarvis is more than just a voice—it's a revolution.",
    "Everything is possible with Jarvis on your side.",
    "Jarvis: A blend of intelligence and innovation.",
    "Jarvis adapts to your needs with every interaction.",
    "Your digital companion is ready to assist—just ask.",
    "Jarvis is the future of personal assistance.",
    "With Jarvis, managing tasks has never been easier."
];

// Function to show a random statement
function randomStatement() {
    const randomIndex = Math.floor(Math.random() * statements.length);
    document.getElementById('random-statement').textContent = statements[randomIndex];
}

// Update statement every 4 seconds
setInterval(randomStatement, 4000);

function startJarvis() {
    fetch("/start", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            startLogStream();
        });
}

function stopJarvis() {
    fetch("/stop", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            stopLogStream();
        });
}

function startLogStream() {
    if (eventSource) eventSource.close();
    eventSource = new EventSource("/logs");
    eventSource.onmessage = function (event) {
        outputDiv.innerHTML += `<p>${event.data}</p>`;
        outputDiv.scrollTop = outputDiv.scrollHeight;
    };
}

function stopLogStream() {
    if (eventSource) {
        eventSource.close();
        eventSource = null;
    }
}

function pauseJarvis() {
    fetch("/pause", { method: "POST" })
        .then(response => response.json())
        .then(data => console.log(data.status));
}

function resumeJarvis() {
    fetch("/resume", { method: "POST" })
        .then(response => response.json())
        .then(data => console.log(data.status));
}

function simulateEnter() {
    fetch("/enter", { method: "POST" })
        .then(response => response.json())
        .then(data => console.log(data.status));
}

randomStatement();
