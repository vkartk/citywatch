

const dashTabs = () => {
    let tabTogglers = document.querySelectorAll('#tabsContainer li a');
    
    tabTogglers.forEach((toggler) => {
        toggler.addEventListener('click', () => {
            tabTogglers.forEach((toggler) => {
                toggler.classList.remove('text-blue-600', 'border-blue-600');
                toggler.classList.add('text-gray-600', 'border-transparent', 'hover:text-gray-600', 'hover:border-gray-300');
            });

            toggler.classList.remove('text-gray-600', 'border-transparent', 'hover:text-gray-600', 'hover:border-gray-300');
            toggler.classList.add('text-blue-600', 'border-blue-600');

            displayIssueTab(toggler.dataset.tab);

        })
    })

}
dashTabs();

const displayIssueTab = tabID => {
    let tabs = document.querySelectorAll('.issue-tab');
    tabs.forEach( tab => {
        tab.style.display = 'none';
    });

    document.getElementById(tabID).style.display = 'block';
}