
function realignAsides() {
    document.getElementsByTagName("body")[0].setAttribute("class", window.innerWidth < 992 + 32 ? "unified" : "split");

    let lastBottom = 0;
    for (let aside of document.getElementsByTagName("aside")) {
        const id = aside.getAttribute("data-id");
        const anchor = document.querySelector(`span[data-id="${id}"]`);
        aside.setAttribute("style", `top: ${Math.max(anchor.offsetTop - 5, lastBottom)}px`);
        lastBottom = aside.offsetTop + aside.offsetHeight;
    }
}

window.addEventListener('resize', realignAsides);
document.addEventListener('DOMContentLoaded', realignAsides);
// Because fonts may load and text may reflow.
for(let i = 200; i <= 2000; i += 200) {
    window.setTimeout(realignAsides, i);
}
