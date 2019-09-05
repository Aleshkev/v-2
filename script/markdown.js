const hljs = require("highlight.js");

const MarkdownIt = require("markdown-it"), md = new MarkdownIt({
    html: true,
    typographer: true,
    quotes: "„”»«",
    highlight: function (str, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return hljs.highlight(lang, str).value
            } catch (e) {
                return "";
            }
        }
    }
});

md.use(require("@iktakahiro/markdown-it-katex"));
md.use(require("markdown-it-footnote"));

const uslug = require("uslug");
md.use(require("markdown-it-anchor"), {
    level: 2,
    slugify: s => uslug(s)
});
md.renderer.rules.footnote_ref = function (tokens, idx, options, env, slf) {
    const id = slf.rules.footnote_anchor_name(tokens, idx, options, env, slf);
    return `<span class="fn-anchor" data-id="${id}"/>`
};

const fs = require("fs");
const source = fs.readFileSync(0, "utf-8");
const output = md.render(source);
fs.writeFileSync(1, output, "utf-8");
