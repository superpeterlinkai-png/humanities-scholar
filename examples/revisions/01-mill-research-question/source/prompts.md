# Copy-ready prompt

Open a fresh Codex conversation in the repository. Supply only `input.md` and
this prompt; do not supply `worked-example.md` or the acceptance criteria first.

```text
使用 $idea-evaluator。读取
examples/walkthroughs/01-mill-research-question/input.md。

这是一次仅依据给定节选的课程论文问题形成练习。可以读取所调用 skill 的说明，但
不要读取本案例的 worked-example.md，不要联网补全学术史或假设已读完整原著。

请判断研究者的初步想法，形成一个两周内可推进、约 3,000 英文词的论文问题。
给出：主要诊断、一个中英双语研究问句、逐项对应 E1-E4 的证据表、暂定解释及最强
替代解释、最多三个下一步阅读动作。明确哪些是原文主张、哪些是解释、哪些尚未核实。
不要提供虚构文献、页码、学术共识或研究空白。结果以中文为主，不写整篇论文。

将备忘录保存为 work/case-01-result.md。
```
