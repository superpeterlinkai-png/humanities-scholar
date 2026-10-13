# Humanities Scholar · 人文学术研究 Skills

**2.0.0 · 三个主要入口，按需配合专项模块。** 用于哲学、宗教学、文学、思想史及交叉研究的材料检索、文本解释、论证、成文和审读。中文指引也支持英文写作与翻译。

Three independently installable core skills for source-grounded humanities research, writing and review, with seven optional specialist skills. The public package contains no prefilled personal author profile.

## 选择入口

| 入口 | 适用工作 |
|---|---|
| [humanities-research](skills/humanities-research/SKILL.md) | 推进研究问题、来源核实、细读、概念、论证及跨步骤研究任务 |
| [humanities-writing](skills/humanities-writing/SKILL.md) | 起草、翻译、编辑、作者声音及限定词句修改 |
| [humanities-review](skills/humanities-review/SKILL.md) | 审查现成稿件的解释、证据、支持链、结构及执行已授权返修 |

每个入口自带所需内部模块，按当前问题读取；不用先走完固定流程。专项模块保留单独的职责和文件，便于针对性修改。内部资源在三个入口中有意复制，使单个入口也能安装使用。

> 用 $humanities-research 接续现有材料，检验暂定论点，补足必要检索与细读，完成研究正文和审读。沿用当前任务的证据范围、字数和已确认的写作要求。

> 用 $humanities-writing 检查这篇文章中的模板词句和防御性表达。先按编号列原句、拟改句和理由，保留原意、引文、章节及指定结尾，不直接修改文件。

> 用 $humanities-review 审读这篇长文，检查后文是否使用前文取得的认识，指出重复论证、游离材料和证据错误。保留有实质作用的否定和限定。

另有七项可选技能：`humanizer-zh`（一般中文编辑）、`humanize-writing`（一般英文或双语编辑）、`voice-dna`（日常声音适配）、`figure-designer`、`drawio-reconstruction`、`benchmark-paper-template`、`tech-paper-template`。学术写作优先用三个主要入口；可选项的触发边界见各自说明。

## 安装

下载 [v2.0.0 发布包](https://github.com/superpeterlinkai-png/humanities-scholar/releases/tag/v2.0.0) 并解压。完整包首次安装需要 Python 3.10+，安装与校验不需要第三方 Python 库：

```powershell
python validate.py
python install.py --destination "$env:USERPROFILE\.codex\skills"
```

macOS / Linux：

```sh
python3 validate.py
python3 install.py --destination "$HOME/.codex/skills"
```

也可让技能安装器从 `tree/v2.0.0/skills/humanities-research`、`humanities-writing` 或 `humanities-review` 路径安装所需入口。每个目录包含独立运行所需指引；实际使用文件、浏览器或格式工具仍取决于宿主环境提供的能力。

安装器先核对全部技能文件哈希和目标冲突，再写入并回读；拒绝覆盖同名目录。升级时先备份自己修改过的技能及私人偏好，明确处理旧目录后再安装。**旧版的十个 humanities-* 独立入口不应与本版重复激活。** 不需要的旧项应移到技能发现目录之外；不要直接用公开版覆盖私人档案。是否已被当前会话加载，以实际调用记录为准。

## 六个长文试验案例

[案例索引与方法](examples/longform/README.md) 包含六个主题、十四篇每篇约两万正文汉字的 AI 生成试验稿、八份匿名配对审读和稳定段落定位。

首次六题比较：一题原配置稍好，一题整合配置较好，四题各有优劣。随后修改长文接续、支持链审读和防御性表达指引，两题重新生成后均获小幅偏好。其余四题没有在最终配置下重测。已知重复、来源错误与推理缺口随评审保留，不能把这轮结果写成整合版全面胜出或可靠的作者身份判别。

私人来源原文件、个人经历、课程身份、作者档案和本地执行路径不随案例公开。公开内容保留论证与实际读取限制；部分来源无法公开使完整材料条件不能直接复现。

## 校验与维护

```sh
python validate.py
python tests/test_install.py
python tests/test_publication.py
```

[VALIDATION.md](VALIDATION.md) 说明结构校验和试验范围；[CHANGES.md](CHANGES.md) 记录版本变化。项目保留原有许可及上游署名，分项适用范围见 [NOTICE.md](NOTICE.md)。
