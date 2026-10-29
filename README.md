# Humanities Scholar · 人文学术研究 Skills

**2.1.0 · 针对 ChatGPT 防御性生成的修订。** 三个主要入口：研究、写作、审读。帮助哲学、宗教学、文学及交叉研究在具体材料中形成解释、发展论证，并完成所需正文。

This release addresses defensive generation in ChatGPT: repeated precautionary qualifications, author-auditing that displaces independent thought, and fragmented exposition after caveats are removed. It develops substantive interpretation during drafting and reviews the resulting text against its actual task.

## 三个入口

| 入口 | 工作 |
|---|---|
| [humanities-research](skills/humanities-research/SKILL.md) | 研究问题、检索、细读、概念工作及跨步骤研究 |
| [humanities-writing](skills/humanities-writing/SKILL.md) | 起草、翻译、论述展开及指定范围的编辑 |
| [humanities-review](skills/humanities-review/SKILL.md) | 判断已有稿件形成的认识、检查论证并执行获准修改 |

每个入口自带按需读取的模块和资源。共用内容从研究入口维护并同步，单个入口可以独立安装。另附七项可选技能：humanizer-zh、humanize-writing、voice-dna、figure-designer、drawio-reconstruction、benchmark-paper-template、tech-paper-template。

## 这次具体改了什么

ChatGPT 的防御性生成会让文章不断说明自己没有证明什么。这样的写法也会进入任务设计：个人讨论被固定为“作者最佳回应—剩余困难—限定结论”，自己的解释迟迟没有展开。仅删去这些句子，容易留下缺少联系的短段。

本版从生成目标入手：在材料中发展自己的解释，让例子、概念辨析与推论共同推进；阅读报告可以延展、重释、比较或反驳作者；段落按思考的实际转折组织。成形后的审读先辨认文章取得了什么认识，再检查其依据。真实否定、具体条件、来源归属及局部修改范围继续按原意处理。

方法与完整样例见 [argument-development.md](skills/humanities-research/resources/humanities-writing/references/argument-development.md)。

## 直接查看改进

- [新构造测试：材料、任务、原始输出与评阅](examples/defensive-generation/README.md)
- [已有通用案例：旧稿、问题定位和新技能改稿](examples/revisions/README.md)
- [版本变化](CHANGES.md)与[实际验证](VALIDATION.md)

测试材料由独立任务重新构造，或来自注明来源的公开原典练习；公开包不包含私人指令、声音档案、课程资料或个人论文。旧长文测试集已移除。

## 安装

从本仓库下载当前版本，或从对应 `skills/<入口名称>` 路径安装单个技能。完整安装需要 Python 3.10+，不需要第三方 Python 库：

```powershell
python validate.py
python install.py --destination "$env:USERPROFILE\.codex\skills"
```

macOS / Linux 使用 `python3` 和目标目录 `"$HOME/.codex/skills"`。安装器核对清单与哈希，拒绝覆盖已有同名目录；升级前整理自己的旧版与私人修改。保持三个现行入口，避免同时激活被其替代的旧独立入口。

## 维护

```text
python validate.py
python tests/test_install.py
python tests/test_publication.py
python skills/humanities-research/scripts/sync_shared.py
```

许可及上游署名见 [NOTICE.md](NOTICE.md)。
