document.addEventListener('DOMContentLoaded', _ => {
    const anchors = document.querySelectorAll('svg a');

    anchors.forEach(anchor => {
        anchor.addEventListener('click', _ => {
            const url = anchor.getAttribute('xlink:href');
            window.parent.location.hash = url;
        });
    });
});
