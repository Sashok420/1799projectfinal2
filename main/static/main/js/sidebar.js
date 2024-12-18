// Получаем элементы кнопки и сайдбара
const sidebarToggle = document.getElementById('sidebar-toggle');
const sidebar = document.getElementById('sidebar');

// Добавляем обработчик события для кнопки открытия/закрытия сайдбара
sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
});