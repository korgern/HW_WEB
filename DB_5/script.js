document.addEventListener("DOMContentLoaded", function() {
    const schedule = [
        { time: "09:00 - 10:30", subject: "Математика" },
        { time: "10:45 - 12:15", subject: "Физика" },
        { time: "12:30 - 14:00", subject: "Химия" },
        { time: "14:15 - 15:45", subject: "История" }
    ];

    const scheduleContainer = document.getElementById("schedule");
    const scheduleList = document.createElement("ul");

    schedule.forEach(item => {
        const listItem = document.createElement("li");
        listItem.textContent = `${item.time} - ${item.subject}`;
        scheduleList.appendChild(listItem);
    });

    scheduleContainer.appendChild(scheduleList);
});