document.addEventListener('DOMContentLoaded', () => {

    dashTabs();
    switchTabByHash();
    navigateToTab();

    getCategoryData().then(data => {
        chartMaker(data);
    });

    let issueStatusButtons = document.querySelectorAll('.issue-status');
    issueStatusButtons.forEach(button => {
        button.addEventListener('click', () => {
            let issueID = button.dataset.issueid;
            let status = button.dataset.status;
            handleIssueStatus(issueID, status);
        });
    });

    let issueDeleteButtons = document.querySelectorAll('.issue-delete');
    issueDeleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            let issueID = button.dataset.issueid;
            handleIssueDelete(issueID);
        });
    });

    let issueEditButtons = document.querySelectorAll('.issue-edit');
    issueEditButtons.forEach(button => {
        button.addEventListener('click', () => {
            let issueID = button.dataset.issueid;
            let dropDown = document.getElementById(`issueEditDropDown-${issueID}`);
            dropDown.classList.toggle('hidden');
        });
    });
});

const getCategoryData = async () => {
    const response = await fetch('/api/categories');
    const data = await response.json();
    return data;
}

const chartMaker = data => {
    const ctx = document.querySelector('#categoryChart').getContext('2d');

    const labels = data.map(category => category.name);
    const issueCounts = data.map(category => category['Open']);

    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Open Issues',
                data: issueCounts,
                backgroundColor: '#edf1f6',
                borderColor: 'gray',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            scales: {
                x: {
                    grid: {
                      display: false
                    }
                },
                y: {
                    grid: {
                      display: false
                    }
                }
            }
            
        }
    });
}


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



const displayIssueTab = tabID => {
    let tabs = document.querySelectorAll('.dash-tab');
    tabs.forEach( tab => {
        tab.style.display = 'none';
    });

    document.getElementById(tabID).style.display = 'block';
}

const getCookie = name => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const handleIssueStatus = (issueID, status) => {
    console.log('issueID: ', issueID);

    const csrftoken = getCookie('csrftoken');
    let data = {
        status: status
    };

    fetch(`/api/issue/${issueID}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    }).then(response => {
        return response.json();
    }).then(data => {
       localStorage.setItem('navTab', 'Issues');
        location.reload();
    });
};

const handleIssueDelete = issueID => {
    const csrftoken = getCookie('csrftoken');
    fetch(`/api/issue/${issueID}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    }).then(response => {
        return response.json();
    }).then(data => {
        localStorage.setItem('navTab', 'Issues');
        location.reload();
    });
};

const switchTabByHash = () => {
    let hash = window.location.hash;
    if (hash) {
        let tab = document.querySelector(`a[href="${hash}"]`);
        tab.click();
    }
};

const navigateToTab = () => {
    const tab = localStorage.getItem('navTab');
    if (tab) {
        let tabButton = document.querySelector(`a[href="#${tab}"]`);
        tabButton.click();
        localStorage.removeItem('navTab');
    }
}