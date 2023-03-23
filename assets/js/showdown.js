function escrever() {
    document.getElementById("html").style = "display: none;"
    document.getElementById("markdown").style = "display: block;"
}
function visualizar() {
    document.getElementById("html").style = "display: block;"
    document.getElementById("markdown").style = "display: none;"
    var markdown = document.getElementById("markdown").value;
    var converter = new showdown.Converter();
    var html = converter.makeHtml(markdown);
    document.getElementById("html").innerHTML = html;
}