(function() {
    // Add CSS for search modal
    const style = document.createElement('style');
    style.innerHTML = `
        #site-search-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 999999;
            justify-content: center;
            align-items: flex-start;
            padding-top: 100px;
            backdrop-filter: blur(5px);
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        #site-search-modal.active {
            display: flex;
            opacity: 1;
        }
        .search-container {
            width: 90%;
            max-width: 600px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
            transform: translateY(-20px);
            transition: transform 0.3s ease;
        }
        #site-search-modal.active .search-container {
            transform: translateY(0);
        }
        .search-header {
            display: flex;
            align-items: center;
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
        }
        .search-header i {
            color: #888;
            font-size: 1.2rem;
        }
        .search-header input {
            flex: 1;
            border: none;
            outline: none;
            padding: 10px 15px;
            font-size: 1.2rem;
            color: #333;
        }
        .search-close {
            cursor: pointer;
            color: #888;
            font-size: 1.2rem;
            transition: color 0.2s;
            margin-left: 10px;
        }
        .search-close:hover {
            color: #e85d04;
        }
        .search-results {
            max-height: 400px;
            overflow-y: auto;
        }
        .search-result-item {
            display: block;
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
            text-decoration: none;
            transition: background 0.2s;
        }
        .search-result-item:hover {
            background: #f8f9fa;
        }
        .search-result-title {
            color: #174873;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 5px;
        }
        .search-result-snippet {
            color: #666;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        .search-result-highlight {
            background-color: #ffe0b2;
            color: #e85d04;
            font-weight: bold;
            padding: 0 2px;
            border-radius: 2px;
        }
        .search-empty {
            padding: 20px;
            text-align: center;
            color: #888;
        }
    `;
    document.head.appendChild(style);

    // Add Modal HTML
    const modalHTML = `
        <div id="site-search-modal">
            <div class="search-container">
                <div class="search-header">
                    <i class="fas fa-search"></i>
                    <input type="text" id="site-search-input" placeholder="Search across the site..." autocomplete="off">
                    <i class="fas fa-times search-close" id="site-search-close" title="Close"></i>
                </div>
                <div class="search-results" id="site-search-results"></div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const modal = document.getElementById('site-search-modal');
    const input = document.getElementById('site-search-input');
    const resultsContainer = document.getElementById('site-search-results');
    const closeBtn = document.getElementById('site-search-close');

    // Attach to all search icons directly
    const searchIcons = document.querySelectorAll('.fa-search');
    searchIcons.forEach(icon => {
        const link = icon.closest('a');
        if (link) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                openSearch();
            });
        }
    });

    function loadIndexAndSearch() {
        if (window.siteSearchIndex) {
            performSearch(input.value);
            return;
        }

        const scriptId = 'search-index-script';
        if (!document.getElementById(scriptId)) {
            const script = document.createElement('script');
            script.id = scriptId;
            script.src = 'js/search_index_data.js';
            script.onload = () => {
                performSearch(input.value);
            };
            document.head.appendChild(script);
        }
    }

    function openSearch() {
        modal.classList.add('active');
        input.value = '';
        resultsContainer.innerHTML = '';
        setTimeout(() => input.focus(), 100);
        // Preload index
        loadIndexAndSearch();
    }

    function closeSearch() {
        modal.classList.remove('active');
    }

    closeBtn.addEventListener('click', closeSearch);
    modal.addEventListener('click', function(e) {
        if (e.target === modal) closeSearch();
    });
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeSearch();
        }
    });

    input.addEventListener('input', function() {
        loadIndexAndSearch();
    });

    function performSearch(query) {
        query = query.trim().toLowerCase();
        if (query.length < 2) {
            resultsContainer.innerHTML = '';
            return;
        }

        if (!window.siteSearchIndex) return;

        const results = [];
        window.siteSearchIndex.forEach(page => {
            const titleMatch = page.title.toLowerCase().indexOf(query);
            const contentMatch = page.content.toLowerCase().indexOf(query);
            
            if (titleMatch !== -1 || contentMatch !== -1) {
                let snippet = '';
                if (contentMatch !== -1) {
                    const start = Math.max(0, contentMatch - 40);
                    const end = Math.min(page.content.length, contentMatch + query.length + 40);
                    snippet = (start > 0 ? '...' : '') + 
                              page.content.substring(start, end) + 
                              (end < page.content.length ? '...' : '');
                    
                    // Highlight query in snippet
                    const regex = new RegExp(query, 'gi');
                    snippet = snippet.replace(regex, match => `<span class="search-result-highlight">${match}</span>`);
                }

                results.push({
                    url: page.url,
                    title: page.title,
                    snippet: snippet || 'Matches in page title.',
                    score: (titleMatch !== -1 ? 100 : 0) + (contentMatch !== -1 ? 1 : 0)
                });
            }
        });

        results.sort((a, b) => b.score - a.score);

        if (results.length === 0) {
            resultsContainer.innerHTML = '<div class="search-empty">No results found for "' + query + '"</div>';
        } else {
            resultsContainer.innerHTML = results.map(r => `
                <a href="${r.url}" class="search-result-item">
                    <div class="search-result-title">${r.title}</div>
                    <div class="search-result-snippet">${r.snippet}</div>
                </a>
            `).join('');
        }
    }
})();
