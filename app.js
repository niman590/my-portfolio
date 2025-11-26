document.addEventListener('DOMContentLoaded', () => {
    const contactSection = document.querySelector('#contact');
    contactSection.addEventListener('click', () => {
        alert("You can contact me via email at nimannethmika@gmail.com");
    });

    // Creating a chart for skills
    const ctx = document.getElementById('skills-chart').getContext('2d');
    const skillsChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Python', 'C++', 'Java', 'Dart', 'Ruby'],
            datasets: [{
                label: 'Skills Proficiency',
                data: [90, 80, 70, 75, 65],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
